import random
score = 0

def play(choices):
    if choices[0] == choices[1]:
        return None
    return choices in (['r','s'],['s','p'],['p','r'])


while True:
    user_choice = input("choose (r)ock, (p)aper or (s)cissors. (e) to exit the game: ")
    if user_choice == "e":
        break
    if user_choice not in ('r','p','s'):
        print("You have to choose r,p,s or e")
        continue
    computer_choice = random.choice(['r','p','s'])
    computer_wins = play([computer_choice,user_choice])
    if computer_wins is None:
        print(f"I chose the same, noone wins. The score is {score}")
        continue
    if computer_wins:
        score = score - 1
        print(f"I chose {computer_choice}. I win. The score is {score}")
        continue

    score = score + 1
    print(f"I chose {computer_choice}. You win. The score is {score}")
