print("Welcone to my game")
playing=input("Do you want to play? ")

if (playing.lower()!="yes"):
    quit()

print("okey lets play!")

answer = input("what does cpu stand for ")
if answer.lower() == "central processing unit":
    print("correct")
else:
    print("incorrect!")
    quit()
answer = input("what does RAM stand for ")
if answer.lower() == "random access memory":
    print("correct")
else:
    print("incorrect!")
    quit()
answer = input("what does ROM stand for")
if answer.lower() == "read only memory":
    print("correct")
else:
    print("incorrect!")
    quit()
answer = input("what does GPU stand for ")
if answer.lower() == "graphic processing unit":
    print("correct")
else:
    print("incorrect!")
    quit()

print("you won the game!")