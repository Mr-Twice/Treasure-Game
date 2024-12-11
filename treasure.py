name = input("Enter your name: ")
print("hello, " + name + "!")
would_you_play = input("Would you like to play this game? ").lower() 
#play = would_you_play == "yes"

if would_you_play == "yes":
    print("Let the fun begin")   
    
    direction = input("Do you want to go left or right? ").lower()
    if direction == "left":
        print("We went to the left, and fell in a ditch. You die!")
    elif direction == "right":
        choice = input("Ok, you see a bridge now, do you want to swim under it or cross it?(swim or cross) ").lower()
        if choice == "swim":
            print("You got eaten by a crocodile. You die!")
        elif choice == "cross":
            print("You found the treasure and YOU WON")    
    else:
        print("Sorry, invalid response. you die")    
else:
    print("Goodbye")
