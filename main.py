print("Welcome to my computer quiz!")

playing = input("Do you wanna play?")

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")

answer1 = input("What does CPU stand for?")
score = 0
if answer1.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer2 = input("What does GPU stand for?")
if answer2.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer3 = input("What does RAM stand for?")
if answer3.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer4 = input("What does PSU stand for?")
if answer4.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

print(f'You got : {score} right answers ')
print(f"That's {(score / 4) * 100} %")
