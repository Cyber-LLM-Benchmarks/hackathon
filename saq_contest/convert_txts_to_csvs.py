import os
import glob
import tqdm
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def process_file(file_path):
    # Read the text file content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Define the prompt to instruct the model to convert the content into CSV format.
    prompt = f"""
You are given a text file containing 10 questions in various formats. Please extract these questions and convert them into a CSV format with three columns:
- id: a unique sequential number for each question (starting at 1),
- question: the question text,
- answer: the answer text (if available; leave blank if not).

Include a header row in the CSV with the column names "id", "question", and "answer". Only output the CSV file and nothing else.

Here is the file content:
{content}
"""

    # Use OpenAI's ChatCompletion API (you can change the model name if needed)
    response = client.chat.completions.create(model="gpt-4o",  # Replace with your desired model (e.g., "o3" if applicable)
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.0  # Use deterministic output
    )

    # Extract the CSV text from the response
    csv_text = response.choices[0].message.content

    # Write the CSV output to a file with the same name but .csv extension
    csv_file_path = os.path.splitext(file_path)[0] + ".csv"
    with open(csv_file_path, "w", encoding="utf-8") as f:
        f.write(csv_text)

    print(f"Processed {file_path} -> {csv_file_path}")

def main():
    # Find all .txt files in the current directory
    txt_files = list(glob.glob("*.txt"))
    if not txt_files:
        print("No .txt files found in the current directory.")
        return

    for txt_file in tqdm.tqdm(txt_files):
        try:
            process_file(txt_file)
        except Exception as e:
            print(f"Error processing {txt_file}: {e}")

if __name__ == "__main__":
    main()

