## Talking.py
## This is a program to accurately simulate conversations with Sharky Jeff.
print("Welcome to the Sharky Jeff Conversation Simulator 1000, the advanced artificial intelligence model to fulfill all your Sharky Jeff needs.")
for x in range(5):
    message = input("Type here: ")
    count = 0
    for char in message:
        if char == " ":
            count = count + 1
    if count > 9:
        print("too long didn't read 🥱")
    else:
        import random
        response = random.randint(1,5)
        if response < 2:
            print("ur cute")
        else:
            print("ur a fag")

print("I'm going to go do homework now byebye")