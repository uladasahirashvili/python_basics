# 🧬 Task 2: String Compression Tool
Your client is dealing with a flood of data and wants to reduce the size of repeated symbols — without losing any actual information. A custom compression method has been proposed to solve this: represent each group of identical, consecutive characters by the character itself and the number of times it appears.

Simple, clever, and saves space 📦💡

## ✅ Task
Write a program that:
- Takes a string as input

- Compresses it using the following logic:
"aaaabbcaa" → "a4b2c1a2"

- Outputs the compressed version of the string

- Preserves the case of each character (i.e. 'a' and 'A' are treated differently)

## 🧪 Example
```markdown
Enter your string: aaAAbbсaaaA  
Encoded string: a2A2b2с1a3A1
```

## ✅ Requirements
- The program should treat lowercase and uppercase letters as distinct

- Compression should only affect consecutive identical characters

- The output format must exactly match the example

- Use clear variable names and keep the code easy to follow

📌 Topics Covered
- String traversal

- Character grouping

- Counters and iteration

- Output formatting
---

🔒 Save storage, save time — compress like a pro!