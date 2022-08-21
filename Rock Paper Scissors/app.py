# %%
import pandas as pd
gameData = pd.DataFrame(columns=['Player', 'Computer', 'Result'])


# %%
import random

winMatrix = [{"rock": "scissors", "paper": "rock", "scissors": "paper"}]

choice = input("Rock, Paper, Scissors")
computer = random.choice(["Rock", "Paper", "Scissors"])
result = "Tie"

# Determine the winner
if choice.lower() != computer.lower():
    # find the item in winMatrix that matches the choices
    for item in winMatrix:
        if item.get(choice.lower()) == computer.lower():
            result = "Win"
        else:
            result = "Lose"

print(f'You chose {choice}, computer chose {computer}. You {result}!')
gameData.loc[len(gameData.index)] = [choice, computer, result]

# %%
gameData.plot()

# %%
gameData.Result.value_counts().plot(kind='bar')
# %%
