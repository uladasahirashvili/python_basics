# 🐞 Task 4: Buggy IPs and Filenames Fixer
At the tech company TechSolutions, each department stores files on a server with a unique IP address. Recently, a developer named Brian updated the auto-save system... but accidentally introduced a few bugs 🧠💥

Some of the IP addresses were malformed, and a few filenames came out just plain wrong — especially the longest ones. Our mission: clean up the data and return a fixed structure that only includes valid entries.

## ✅ Task
We’re given a list of records, where each record contains:

- An IP address

- A list of filenames (all mashed into one string)

## Write a program that:

- Validates the IP address — it must consist of four integers between 0 and 255, separated by dots

- Filters filenames so that only valid ones are kept:

- No special characters at the start (@, №, $, %, ^, &, *, ()

- Ends with .txt or .docx

- Return a new list of valid records, preserving only the clean data.

## 🧪 Example
```markdown
Initial record:
["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]]

Filtered version:
[skipped due to invalid IP or invalid filenames]
```
```markdown
Output:
[
    ['128.0.0.255', ['file_1.txt document_2024.docx notes2022.txt']],
    ['192.168.1.10', ['file_432.txt  important_info.txt notes1900.txt']],
    ['10.20.30.40', ['file_432.txt  analysis_results.txt notes1998.txt']]
]
```

## ✅ Requirements
- IPs must follow standard IPv4 rules (4 numbers, each from 0 to 255)

- Filenames must:

- Not start with any forbidden special characters

- End with .txt or .docx

- Output must be in the same structure as the input

- Preserve the order of valid records

## 📌 Topics Covered
- String and list manipulation

- Input validation

- Nested data structures

- Conditionals and filtering logic
---

🧹 Clean up the digital mess — and restore order to the TechSolutions network!