# Cyber LLM Benchmarks Hackathon

Three (3) different contests:

## A) Short Answer Question (SAQ) Contest

**Goal** 
– Generate a high-quality dataset of 2000 Short Answer Questions (SAQs) spanning multiple cybersecurity domains.

**Domains**  
- Security compliance and certifications  
- Product security guidelines  
- Data security  
- Cloud security  
- Infrastructure security  
- Network security  
- Endpoint security  
- Identity & Access Management (IAM) Security  
- API security  
- Application Security Testing  
- Vulnerability management  
- Threat Intelligence & monitoring  
- Offensive security (Red-teaming and penetration testing)  

### Contest Theme  
**“Stump the AI – CyberSecurity Edition”**  

### Contest Description  
The core concept of the challenge is to discover the toughest cybersecurity questions that Large Language Models (LLMs) currently fail to answer accurately. Participants compete to craft these “stumpers,” ensuring the final dataset is both high-quality and wide-ranging across the specified domains.

### Deliverables  

- **Question**: A concise, specific query that touches on one or more cybersecurity sub-domains.  
- **Correct Answer**: A short, fact-checked answer.  
- **Reference/Explanation**: Source or rationale that proves correctness (e.g., link to official documentation, academic papers, CVE details, etc.).  
- **Evaluation Outcome**: Evidence of how ChatGPT fails or partially fails to answer (e.g., a screenshot, text, or log of ChatGPT’s incorrect response).  

### Awards  

- **Grand Prize**: Best “Stumper” question overall (the question that confuses ChatGPT the most).  
- **Category Prizes**: Best question in each cybersecurity domain (e.g., Best Cloud Security Stumper).
- **WTF Prize**: Most confusing question (a valid question that produces the most non-sensical and/or funny response from ChatGPT).

---

## B) Reasoning Models Contest  

**Goal** 
- We have curated a Multiple Choice Question and Answer (MCQA) dataset of cybersecurity questions, answers, and potential explanations. The task is to find any discrepancies between the question, answers, and explanations. Be careful: you're competing against ChatGPT!

### Contest Theme  
**“Explanations Under Fire—Fact-Check the MCQA”**  

### Contest Description  
Each participant becomes a **“Security Explanation Detective”**, investigating the reasoning behind multiple-choice answers. Participants earn points for accurate, detailed validations—and for catching mistakes in the questions, answers, and explanations that can lead to a confusing question, invalid answer, or non-sensical explanation. 

### Deliverables  

1. **Review** the official “correct answer” and its explanation.  
2. **Assess** whether the explanation is valid, fully correct, and clearly stated.  
3. **Validate or Correct**:  
   - If correct, mark as **“Validated”**  
   - If incorrect or incomplete, explain why and provide an improved (concise) explanation referencing credible sources  

### Awards  

- **Most Insightful Detective**: Individual or team recognized for the best “catch” of a subtle or critical error.  
- **Speedy Validator**: Team that completes their review block both accurately and fastest.
- **Beating ChatGPT**: Team with the most accurate score that beats ChatGPT.

---

## C) Unique Dataset Contest  

**Goal** 

– Create benchmarks reflecting tasks currently performed by cybersecurity professionals. Each dataset should contain **20-100 examples** for a task that participants find particularly challenging.  

### Example  
The **CTI-ATE** benchmark dataset focuses on **Attack Technique Extraction**. The task involves identifying specific attack patterns from a given threat behavior description and mapping them to the corresponding **MITRE ATT&CK** technique IDs. The **Micro-F1 score** is used as the evaluation metric for this task.  

### Contest Theme  
**“Nightmare Tasks No More—Building Mini-Benchmarks for Cybersecurity Pain Points”**  

### Contest Description  
Participants are encouraged to identify repetitive, dull, or particularly vexing tasks they face in their daily cybersecurity work (e.g., mapping threat reports to MITRE ATT&CK techniques, analyzing repetitive log data, summarizing lengthy compliance documents, etc.). They then synthetically create a small (**20-100 examples**) benchmark dataset replicating that task’s typical input-output structure.  

### Deliverables  

- **Dataset**: 20-100 well-structured examples.  
- **Task Description**: A concise explanation of why the task is painful in real-world scenarios, how the data was created, and any domain references (e.g., MITRE IDs, compliance standards, typical logs).  
- **Suggested Evaluation**: Guidance on how an LLM or other AI tool might be evaluated on these examples (including the chosen metric and any special scoring criteria).  

### Awards  

- **Grand Prize**: Best overall mini-benchmark—checks all the boxes (realism, utility, clarity).  
- **Most Innovative**: A creative or less-discussed pain point that could spark new solutions.  


## Hosts and Participants
- Hosts: Omar Santos, Dhruv Kedia, Paul Kassianik, Baturay Saglam, Casey Hall, and Naveen Sanku (Cisco / Robust Intelligence)
- Participants: Cisco S&TO and wider Cybersecurity community
- Data: Public and open-source.
