print(''' 𝓠𝓤𝓘𝓩 𝓒𝓗𝓐𝓛𝓛𝓔𝓝𝓖𝓔𝓡
          1. Automobiles
          2. Smart phones
          3. Sports
          4. Health
          5. Games \n''')

print("Choose any one of the above topic for quiz.\n")


# a = input("Enter the topic: ").lower()
def Automobiles():
    import random
    auto = ["What year was the first car invented? ", "Who invented the first car?",
            "What fuel was used for the first car? "]
    n = 1
    auto1 = random.choices(auto,k=n)
    auto2 = ' '.join(auto1)
    print(auto2)
    # auto_check =
    if auto2 == "What year was the first car invented? ":
        # auto_check = 0
        auto_check = int(input("Enter your answer: "))
        if auto_check == 1885:
            print("Correct answer!")
        else:
            print("Oops! It's 1885, BETTER LUCK NEXT TIME!")
    elif auto2 == "Who invented the first car?":
        auto_check = input("Enter the name: ").lower()
        if auto_check == "karl benz":
            print("WOW! You got it right!")
        else:
            print("OOPS! It's Karl benz")
    else:
        auto_check = input("Enter the fuel type: ").lower()
        if auto_check == "gas":
            print("WOW! You got it right!")
        else:
            print("OOPS! It's GAS.")


a = input("Enter the topic: ").lower()
if a == "automobiles":
    Automobiles()