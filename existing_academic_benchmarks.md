# Existing Public Benchmarks

## A) SecBench

**Paper** - [SecBench Paper](https://arxiv.org/abs/2412.20787)

### Novel Approach
- Organized a large-scale Cybersecurity Question Design Contest where humans submitted high-quality questions.
- These questions spanned multiple-choice questions answers (MCQA) and short-answer questions (SAQ).
- Questions covered multiple cybersecurity domains.

### Drawbacks
- Only **2.6%** of the Short Answer Question dataset is in English, which amounts to only **80 questions**.  
- This is an extremely small dataset to conduct evaluations on.

---

## B) CTIBench

**Paper** - [CTIBench Paper](https://arxiv.org/pdf/2406.07599)

### Novel Approach  
CTIBench goes beyond MCQA to include additional evaluation benchmarks:

- **CTI-RCM: Root Cause Mapping Benchmark**  
  - Root Cause Mapping (RCM) identifies the underlying causes of vulnerabilities by linking **CVEs to CWE** entries.  
  - This is a highly nuanced task requiring deep understanding of **CVE descriptions** and the **CWE taxonomy** to make accurate mappings.  
  - **Evaluation Metric:** Accuracy (since it’s equivalent to a multi-class classification problem).  

- **CTI-ATE: Attack Technique Extraction Benchmark**  
  - This task involves identifying specific attack patterns from a given threat behavior description and mapping them to the corresponding **MITRE ATT&CK** technique IDs.  
  - **Evaluation Metric:** Micro-F1 score.  

- **CTI-VSP: Vulnerability Severity Prediction Benchmark**  
  - The **Vulnerability Severity Prediction** task aims to predict the **Common Vulnerability Scoring System (CVSS)** vector string from a given vulnerability description.  
  - **Evaluation Metric:** Mean Absolute Deviation (MAD) between the **CVSS v3.1 scores** of the ground truth and the model’s predictions.
