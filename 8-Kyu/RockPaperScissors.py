# You have to return which player won! In case of a draw return Draw!.
# 
# Examples(Input1, Input2 --> Output):
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

def rps(p1, p2):
    l1 = p1.lower()
    l2 = p2.lower()

    win1 = "Player 1 won!"
    win2 = "Player 2 won!"

    if (l1 == l2):
        return "Draw!"
    elif (l1 == "scissors"):
        return win1 if l2 == "paper" else win2
    elif (l1 == "paper"):
        return win1 if l2 == "rock" else win2
    else:
        return win1 if l2 == "scissors" else win2


# Solution
# EXCELLENT solution using dictionary

def rps_Solution(p1, p2):
    beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

    if (beats[p1] == p2):
        return "Player 1 won!"
    if (beats[p2] == p1):
        return "Player 2 won!"
    
    return "Draw!"