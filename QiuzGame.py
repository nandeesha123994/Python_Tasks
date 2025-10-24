print("Welcome to my Compter quiz!")

playing=input("Do you want play? ")

if playing.lower()!="yes":
    quit()

print("Okay! let's Play: ")

score=0                                                # for caluculating the score//
wrong=0
anwer=input("what does cpu mean? ")
if anwer.lower() == "central processing unit":
    print("correct!")
    score+=1
else:
    print("Incorrect!")
    wrong+=1

anwer=input("what does gpu mean? ")
if anwer.lower() == "graphical processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

anwer=input("what does ram mean? ")
if anwer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

anwer=input("what does rom mean? ")
if anwer.lower() == "read only memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

anwer=input("what does hdd mean? ")
if anwer.lower() == "hard disk drive":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

anwer=input("what does ssd mean? ").lower()
if anwer == "solid state drive":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

anwer=input("what does os mean? ")
if anwer.lower() == "operating system":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

anwer=input("what does lan mean? ")
if anwer.lower() == "local area network":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

anwer=input("what does ai mean? ")
if anwer.lower() == "artificial intelligence":
    print("correct!")
    score += 1
else:
    print("Incorrect!")
    wrong += 1

print("You got " + str(score) + " questions correct")
print("You got " + str((score/9)*100) + "%.")
print("You got " + str(wrong) + " questions wrong")
print("You got " + str((wrong/9)*100) + "%.")



