# 🔁 Task 3: Cyclic Shift Checker

You're given two strings. One of them might be just a rotated (cyclically shifted) version of the other. Your job? Figure out if that’s the case — and if yes, by how many characters 🕵️‍♀️💫

## ✅ Task
Write a program that:

- Takes two strings as input from the user

- Checks if the first string can be obtained by cyclically shifting the second one to the right

- If it can — print the shift value

- If it can’t — let the user know that transformation is not possible

## 🧪 Examples
```markdown
First string: abcd  
Second string: cdab  
Result: The first string can be obtained from the second with a shift of 2
```

``` markdown
First string: hello  
Second string: lohel  
Result: The first string can be obtained from the second with a shift of 3
```
``` markdown
First string: abcd  
Second string: cdba  
Result: The first string cannot be obtained from the second via a cyclic shift
```

## ✅ Requirements
- Shift must be cyclic — after the end, the string wraps around

- Output must match the examples exactly

- Use clear logic and descriptive variable names

- Edge cases (like different-length strings) should be handled gracefully

## 📌 Topics Covered
- String slicing and rotation

- Comparison and conditionals

- Input handling

- Looping logic

---
🔄 Strings on the move!