# Task 7: The Counting-Out Game
N people numbered from 1 to N stand in a circle.
They play a counting-out game where every K-th person is eliminated from the circle, and counting continues from the next person after the eliminated one.

## ✅ What You Need to Do
Write a program that:

- Takes input for the number of people N and the counting number K.

- Simulates the elimination process step by step.

- Prints which person is eliminated each round, the current circle, and from which number counting starts.

- In the end, outputs the number of the last person remaining.

## 🧪 Example
```markdown
Number of people: 5  
Counting number K: 7  
So, every 7th person is eliminated.

Current circle: [1, 2, 3, 4, 5]  
Counting starts at number 1  
Person number 2 is eliminated.

Current circle: [1, 3, 4, 5]  
Counting starts at number 3  
Person number 5 is eliminated.

Current circle: [1, 3, 4]  
Counting starts at number 1  
Person number 1 is eliminated.

Current circle: [3, 4]  
Counting starts at number 3  
Person number 3 is eliminated.

Last remaining person is number 4.
```
## ✅ Requirements
- The elimination logic must be correct.

- Inputs must have clear prompts as shown.

- Output formatting must exactly match the example.

- Use meaningful variable names (no random letters).

## 📌 Topics Covered
- Lists and indexing

- Simulation with loops

- Modulo arithmetic for circular counting
---
Survive the counting-out and be the last one standing! 🏆🌀