# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


strategy = 0
winners_side = {'R': 'P', 'P': 'S', 'S': 'R'}


def player(prev_play, opponent_history=None):
    global strategy
    if not prev_play:
        strategy += 1
        opponent_history = []

    if len(opponent_history) == 0 and not prev_play:
        return random.choice(['R', 'P', 'S'])

    opponent_history.append(prev_play)

    if strategy == 2:
        return quick_think_strategy(prev_play, opponent_history)

    return logic_strategy(prev_play, opponent_history)


def quick_think_strategy(prev_play, opponent_history):
    if len(opponent_history) > 2 and opponent_history[-1] == opponent_history[-2]:
        return winners_side[prev_play]

    return winners_side[winners_side[winners_side[prev_play]]]


def logic_strategy(prev_play, opponent_history):
    if len(opponent_history) > 2 and opponent_history[-2] == opponent_history[-3] == prev_play:
        return winners_side[winners_side[winners_side[prev_play]]]

    return winners_side[prev_play]
