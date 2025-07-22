# Task 1: The Scary Code

You were helping a friend who just started learning Python.  
Their task seemed simple — list manipulations and counting specific numbers.  
But the code… was terrifying 😱

Your mission: rewrite the code using better style and proper list methods — and without creating additional lists.

---

## 🧟‍♂️ The Original "Scary" Code

```python
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
t = 0
for i in a:
    if i == 5:
        t += 1
print(t)
d = []
for i in a:
    if i != 5:
        d.append(i)
for i in c:
    d.append(i)
t = 0
for i in d:
    if i == 3:
        t += 1
print(t)
print(d)
```
## 💡 Task Description

Given three lists:

```python
main_list = [1, 5, 3]  
side_list_1 = [1, 5, 1, 5]  
side_list_2 = [1, 3, 1, 5, 3, 3]
```
Write a program that:

- Extends the main list with side_list_1.

- Counts how many 5s are in the extended list and prints the count.

- Removes all 5s from the main list.

- Extends the list again with side_list_2.

- Counts how many 3s are in the final list and prints the count.

- Prints the final list.

❗ Do not use any additional lists — everything must happen in-place.

## 🧾 Expected Output
```SQL
Number of 5s after first merge: 3  
Number of 3s after second merge: 4  
Final list: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]
```
## ✅ Requirements
- No extra lists (in-place only).

- Use meaningful variable names — no a, b, c.

- Output format must match the example.

- Use Python list methods effectively (extend, count, remove, etc.).

📌 Topics Covered
- List methods

- In-place data manipulation

- Loops and conditions

- Clean and readable code

---
Clean up the scary code 👻🧹




