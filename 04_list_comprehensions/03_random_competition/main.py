import random

team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners = [team_1[i] if team_1[i] > team_2[i] else team_2[i] for i in range(20)]

print('Team 1 scores:', team_1)
print('Team 2 scores:', team_2)
print('Round winners:', winners)
