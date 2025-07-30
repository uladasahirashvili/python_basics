# ⚔️ Task 7: Random Competition Simulator
You’re helping test an electronic scoreboard for a competition between two teams. Each team has 20 participants, and each participant has a score — a floating-point number with two decimals, between 5 and 10.

Each participant from Team 1 faces off against the participant with the same index in Team 2. Your job? Generate the teams’ scores randomly, then find out who won each matchup.

## ✅ Task
Write a program that:

- Generates two lists of 20 random floating-point numbers each, ranging from 5.00 to 10.00 (inclusive)

- Each number represents a participant’s score

- Compares participants pairwise by index (1st vs 1st, 2nd vs 2nd, etc.)

- Creates a third list with the winners’ scores from each pair (the higher score wins)

- Prints all three lists clearly

## 🧪 Example
```markdown
Team 1 scores: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1, 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
Team 2 scores: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8, 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
Winners: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8, 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]
```
## ✅ Requirements
- Use the random module to generate scores (e.g. random.uniform)

- Scores must be floating-point with two decimals

- Compare participants index-by-index correctly

- Output format must follow the example exactly

- Use meaningful variable names

## 📌 Topics Covered
- Random number generation

- List operations and comprehensions

- Pairwise comparison

- Formatting output
---

⚡ A perfect intro to simulations, competitions, and practical Python list handling!