# Your can add more and more qustion and answer as yourself 
#This is a kind of super basic if/else logic quiz game 

print("Welcome to quiz game!")

playing = input("Do you want to play this game? yes/no? ")

if playing.lower() != 'yes':
     quit()

print("Okay!Lets play the game! ")

score = 0
mark = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
     print("Correct!")
     score += 1
     mark += 5
else:
     print("Incorrect!")


answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
     print("Correct!")
     score += 1
     mark += 5
else:
     print("Incorrect!")


answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
     print("Correct!")
     score += 1
     mark += 5

else:
     print("Incorrect!")


answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
     print("Correct!")
     score += 1
     mark += 5

else:
     print("Incorrect!")


print("You got " + str(score) + " qustions correct!!")

if mark > 15:
     print("Congratulations you got " + str(mark) + " mark!!")
else:
     print("Ohh!! sad best of luck for next time your mark " + str(mark) + "  is too low! ")


