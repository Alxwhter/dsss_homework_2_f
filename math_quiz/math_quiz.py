import random


def random_number(min, max):
    """
    Returns random number between min and max. No floats!
    
    Parameters
    ------------------
    min :   integer
        Minimal possible Number
    
    max :   integer
        Maximal possible Number
    
    Returns
    -----------------
    output  :   integer
        Random number between min and max value.
    """
    return random.randint(min, max)


def random_mathsymbol():
    """
    Returns +, - or *
    
    Parameters
    ------------------
    
    Returns
    -----------------
    output  :   string
        Random value between "+", "-" or "*"
    """
    return random.choice(['+', '-', '*'])


def calculate_solution(n1, n2, o):
    """
    Returns first the string of the calculation
    and secondly the solution of the calculation
    The function can differentiate between +, - and *
    
    Parameters
    ------------------
    n1 :   integer
        Number 1
    
    n2 :   integer
        Number 2
    
    o  :   string
        mathmatic symbol; only +, - and * is allowed
    
    Returns
    -----------------
    output1  :   string
        a string with the calculation 
    output2  :   integer
        the solution of the calculation
    """
    try:
        p = f"{n1} {o} {n2}"
        if o == '+': a = n1 + n2
        elif o == '-': a = n1 - n2
        elif o == '*': a = n1 * n2
        #else: a = n1 * n2
        return p, a
    except ValueError:
        print("Invalid input for summation")
    else:
        print("Invalid inputs of numbers")

def math_quiz():
    #Initialize Values
    counter_correct = 0
    n_games = 10

    #Print Welcome-Messages
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #Iterate through games
    for _ in range(n_games):
        #Create two random numbers and one random mathsymbol
        n1 = random_number(1, 10); n2 = random_number(1, 5); mathsymbol = random_mathsymbol()

        #Calculate Solution and print it out and ask for Solution
        PROBLEM, ANSWER = calculate_solution(n1, n2, mathsymbol)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except ValueError:
            print("Invalid number")
            

        #Compare Useranswer with Solution -> in Case of correct solution increase counter_correct
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            counter_correct += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    #Print final Score
    print(f"\nGame over! Your score is: {counter_correct}/{n_games}")

if __name__ == "__main__":
    math_quiz()
