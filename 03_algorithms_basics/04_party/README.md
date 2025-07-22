# Task 4: The Birthday Party
Your friend James decided to throw a birthday party at his countryside house.
He didn't send formal invitations, just told everyone: "If you want to come, bring your friends too."
People came and went during the party, and not everyone stayed overnight.
Also, the house isn't that big — it can fit only six people at a time.

## ✅ What You Need to Do
Given an initial guest list — the people who arrived at the start:
```python
guests = ['Tom', 'Anna', 'Mike', 'Lisa', 'Kate']
```
Write a program that:

- Asks the user whether a guest has arrived or left.

- Then asks for the guest's name.

- If the guest arrived and there’s space (max 6 guests), add their name to the list and greet them.

- If the guest arrived but there’s no space, politely refuse entry.

- If the guest left, remove them from the list and say goodbye.

- Keep repeating this until the user types "Time to sleep".

- At each step, print the current number of guests and their names.

## 🧪 Example
```markdown
Currently at the party: 5 people — ['Tom', 'Anna', 'Mike', 'Lisa', 'Kate']
Did a guest arrive or leave? arrive
Guest's name: Alex
Hi, Alex!

Currently at the party: 6 people — ['Tom', 'Anna', 'Mike', 'Lisa', 'Kate', 'Alex']
Did a guest arrive or leave? arrive
Guest's name: George
Sorry, George, there’s no room.

Currently at the party: 6 people — ['Tom', 'Anna', 'Mike', 'Lisa', 'Kate', 'Alex']
Did a guest arrive or leave? leave
Guest's name: Anna
Bye, Anna!

Currently at the party: 5 people — ['Tom', 'Mike', 'Lisa', 'Kate', 'Alex']
Did a guest arrive or leave? Time to sleep

The party is over, everyone went to sleep.
```
## ✅ Requirements
- Correctly update the guest list based on arrivals and departures.

- Limit the number of guests to six.

- Use clear and meaningful variable names.

- Input prompts and output messages must match the example format.

## 📌 Topics Covered
- Lists and list operations (add, remove)

- Input and output formatting

- Loops and conditionals

---
Keep the party fun and under control! 🥳🛋️