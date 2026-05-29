import os
import re
import csv
import sys

def parse_qa(data):
    # Remove introductory text before the first header (either "Question X:" or "X.")
    m = re.search(r'^(?:Question\s+\d+:|\d+\.)', data, flags=re.MULTILINE)
    if m:
        data = data[m.start():]

    # Define candidate regex patterns.

    # Candidate Pattern 1:
    # For formats with "Question X:" headers (Formats A and D)
    pattern1 = r"""
        ^Question\s+(?P<num>\d+):\s*              # Header: "Question <number>:" at beginning of line
        (?P<question>.*?)(?:\r?\n)+                # Lazily capture question text until newline(s)
        Answer:\s*(?P<answer>.*?)(?=              # Then literal "Answer:" and capture answer text until...
            ^Question\s+\d+:|                     # next header "Question X:" at start of line,
            ^\d+\.\s|                            # or a numbered header ("X.") at start,
            ^─{5,}|                             # or a horizontal bar (line of 5+ dashes),
            $)                                   # or end-of-file.
    """

    # Candidate Pattern 2:
    # For numbered headers with an optional "Answer:" label (Formats B and C)
    pattern2 = r"""
        ^(?P<num>\d+)\.\s*                        # Header: "<number>." at beginning of line
        (?P<question>.*?)(?:\r?\n)+                 # Lazily capture question text until newline(s)
        (?:Answer:\s*)?                           # Optionally match "Answer:" literal
        (?P<answer>.*?)(?=                         # Capture answer text until lookahead:
            ^(?:\d+\.|Question\s+\d+:)|            # next header ("X." or "Question X:") at beginning of line,
            ^─{5,}|                              # or a horizontal bar,
            $)                                   # or end-of-file.
    """

    # Candidate Pattern 3:
    # For numbered headers without an explicit "Answer:" label (Format E)
    pattern3 = r"""
        ^(?P<num>\d+)\.\s*                        # Header: "<number>." at beginning of line
        (?P<question>.*?)(?:\r?\n){2,}              # Capture question text until at least 2 newlines (separator)
        (?P<answer>.*?)(?=                         # Capture answer text until lookahead:
            ^\d+\.\s|                             # next numbered header at beginning,
            ^─{5,}|                              # or a horizontal bar,
            $)                                   # or end-of-file.
    """

    # List of candidate patterns (order matters)
    candidates = [pattern1, pattern2, pattern3]
    qa_pairs = None

    for pat in candidates:
        regex = re.compile(pat, flags=re.DOTALL | re.MULTILINE | re.VERBOSE)
        matches = list(regex.finditer(data))
        if len(matches) == 10:
            qa_pairs = []
            for m in matches:
                qid = m.group("num").strip() if m.group("num") else ""
                question = m.group("question").strip()
                answer = m.group("answer").strip()
                qa_pairs.append({
                    "id": qid,
                    "question": question,
                    "answer": answer
                })
            break

    return qa_pairs

def convert_file_to_csv(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = f.read()

    qa_pairs = parse_qa(data)
    if qa_pairs is None or len(qa_pairs) != 10:
        print(f"WARNING: {input_file} did not yield exactly 10 questions (found {len(qa_pairs) if qa_pairs else 0}).")
    else:
        print(f"{input_file} parsed correctly with 10 questions.")

    # Write out whatever was parsed (even if not 10) to the CSV file.
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "question", "answer"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        if qa_pairs:
            for pair in qa_pairs:
                writer.writerow(pair)

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            input_file = os.path.join(directory, filename)
            basename, _ = os.path.splitext(filename)
            output_file = os.path.join(directory, f"{basename}.csv")
            print(f"Processing {input_file} -> {output_file}")
            convert_file_to_csv(input_file, output_file)
    print("All files processed.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_directory.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Provided path is not a valid directory.")
        sys.exit(1)
    process_directory(directory)

if __name__ == "__main__":
    main()

