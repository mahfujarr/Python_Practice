
questions = [

            ["Who discovered gravity?",
              "Einstein", "Max Plank", "Newton", "Alfred Nobel", 3],

            ["The World's Largest desert is ?",
              "Thar", "Sahara", "Gobi", "Kalahari", 2],

            ["The hottest planet in the solar system ?",
              "Earth", "Mars", "Jupiter", "Venus", 4],

            ["Which particle is not a fundamental particle?",
              "Deuteron", "Electron", "Proton", "Neutron", 1]

]
No = [1,2,3,4,5,6,7,8,9]

i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f'***Question no.{No[i]} is:\n')
    print(f"{question[0]}")
    print(f"a. {question[1]}                b. {question[2]}")
    print(f"c. {question[3]}                d. {question[4]}")
    reply = int(input("Enter your answer:(1-4): "))
    if(reply == question[-1]):
        print(f"Correct answer!\n")
    else:
        print("Wrong Answer!\n")
        break