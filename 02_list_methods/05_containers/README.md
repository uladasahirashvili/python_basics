# Task 5: Containers

This Python program simulates the placement of a new container into a warehouse row where all containers are sorted in **non-increasing** order by weight.

## 💡 Task Description

You're given:
- A number of containers already in the warehouse, each with a weight (max 200 kg).
- The weight of a new container.

Your program must:
- Place the new container **after** all containers with the same or greater weight.
- Output the 1-based index of the position the new container will take.

If any entered weight exceeds 200 kg, an error message is printed.

## 🧾 Example
```markdown
Number of containers: 8
Enter container weight: 165
Enter container weight: 163
Enter container weight: 160
Enter container weight: 160
Enter container weight: 157
Enter container weight: 157
Enter container weight: 155
Enter container weight: 154

Enter the new container weight: 162

The new container will be placed at position: 3
```

## ✅ Requirements

- Input validation: no container may exceed 200 kg.
- Output format should match the example.
- Variable names should be meaningful.
- The container should be placed **after all containers of the same weight**.

## 📌 Topics Covered

- List iteration
- Conditional logic
- Insertion index calculation
- User input handling

---

Stack like a pro 📦✨
