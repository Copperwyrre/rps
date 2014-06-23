def choice():
    """returns choice in lowercase"""
    choice = raw_input("Enter a choice: ")
    return choice.lower()

def compare(choice1, choice2):
    """Decides winner of rock, paper, scissors"""
    if choice1 == "rock" and choice2 == "scissors":
        print ("Rock smashes Scissors!")
    elif choice1 == "rock"and choice2 == "paper":
        print ("Paper covers Rock!")
    elif choice1 == "scissors" and choice2 == "paper":
        print ("Scissors cut Paper!")
    elif choice1 == "scissors" and choice2 == "rock":
        print ("Rock smashes Scissors!")
    elif choice1 == "paper" and choice2 == "rock":
        print ("Paper covers Rock!")
    elif choice1 == "paper" and choice2 == "scissors":
        print ("Scissors cut Paper!")        
    elif choice1 == choice2:
        print ("Tie!")

rounds = int(raw_input("enter number of rounds: ")        
for x in range(3):
    choice1 = choice()
    choice2 = choice()
    compare(choice1, choice2)
    
        
    

