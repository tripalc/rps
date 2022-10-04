import random

def main():
    
    n = 0


    print("")
    print("Rock Paper Scissors")
    input("Press Enter key continue...")
        
    n = random.randint(0,2)
        
    if n == 0:
        print("I chose Rock...")

    elif n == 1:
        print("I chose Paper...")
        
    elif n == 2:
        print("I choose Scissors...")

if __name__ == "__main__":
    main()