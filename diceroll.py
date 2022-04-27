import random

def rolldice(min,max):
    while True:
        print("Rolling dice...")
        rolnum= random.randint(min,max)
        print(f"Your Number : {rolnum}")
        choice = input("Do you want to Roll again? (y/n): ")
        if choice.lower() == 'n':
            break

rolldice(1,6)

