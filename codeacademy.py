# def factorial(num):
#    if num == 1:
#        return 1
#    else:
#        return num * factorial(num-1)
   
# results = factorial(4)
# print(results)    # example is recursion 


# def Seth(num):
#     if num == 2:
#         return 10 
#     else: 
#         return num * Seth(num-2)
# results = Seth(8)
# print(results)




# results = lambda a, b: a * b
# print(results(3, 4))

# numbers = [1, 2, 3, 4, 5] 

# squared = list(map(lambda x: x ** 2, numbers)) 

# print(squared)  # Output: [1, 4, 9, 16, 25] 


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# squared = list(map(lambda x: x ** 2, numbers))

# print(squared)

# from colorama import Fore, Style, init # for styling. 
# # pip install colorama from your terminal. may need to restart code editor for installation to complete. 

# init()

# def start_adventure(): # functions - covered by William in lecture # 4
#     print(Fore.GREEN + "Welcome to A Very Python Christmas " + Style.RESET_ALL) # if you don't reset the style, colouring will continue
#     print()
#     print()
#     print("The snow falls softly outside, blanketing the town of Hollybrooke in a thick layer of white.  You're curled up by the fire, sipping hot cocoa, when suddenly, there's a rustling at the door. You open it to find a small, green Python named Pythius shivering in the cold.")
#     print("'Hello,' he whispers, his voice barely audible over the wind. 'My name is Pythius, and I need your help! Santa's sleigh has been stolen!'")
#     print("(A) Help Pythius find Santa's sleigh without delay?")
#     print("(B) Offer Pythius some hot cocoa and have him sit down first?")
#     print()
#     print(Fore.RED + "Press A or B to continue" + Style.RESET_ALL)

#     choice = input("Enter A or B: ") # user input - was covered in the first lecture! 

#     if choice.lower() == "a":
#         find_sleigh()
#         print()
#     elif choice.lower() == "b":
#         hot_cocoa()
#         print()
#     else:
#         print(Fore.RED + "Invalid choice. Try again!" + Style.RESET_ALL)
#         print()
#         start_adventure()

# def find_sleigh(): 
#     print("You decide to help Pythius. 'Don't worry,' you say,'We'll find Santa's sleigh!'")
#     print("'Thank you! I know it was the Grinch,' he says with a shudder. 'He hates Christmas and always tries to ruin it.")
#     print("'Well, we can't let that happen,' you say resolutely.") 
#     print("Pythius tells you that Santa usually stores his sleigh in a hidden cave on Mount Evergreen.") 
#     print()
#     print(Fore.RED + "Choose A or B: " + Style.RESET_ALL)
#     print("(A) Take Pythius directly to Mount Evergreen? You know the way.")
#     print("(B) Ask Pythius if he knows any other clues about where the Grinch might have taken the sleigh?")
#     print(Fore.RED + "Press A or B to continue" + Style.RESET_ALL)
    
#     choice = input("Enter A or B: ") # user input - was covered in the first lecture! 
    
#     if choice.lower() == "a":
#         go_to_mountain()
#     elif choice.lower() == "b":
#         hot_cocoa()
#     else:
#         print("Invalid choice. Try again!")
#         find_sleigh()
    
# def hot_cocoa():
#     print("You decide to gather more information before heading straight to Mount Evergreen. 'Pythius,' you ask, 'do you know anything else about where the Grinch might have taken Santa's sleigh?'")
#     print("Pythius sips his cocoa thoughtfully. 'Hmm,' he says, stroking his chin. 'The Grinch loves shiny things, and he's always complaining about how boring Hollybrooke is. Maybe he took the sleigh to a place with lots of sparkle and excitement!'")
#     print("He pauses for a moment, then adds, 'Oh! And I heard him muttering something about a stage where everything shines bright. Could it be...the Ice Palace?'")
#     print("The Ice Palace is a famous winter festival in Hollybrooke, known for its dazzling ice sculptures and glittering decorations.")
#     print("Do you:")
#     print("(A) Head straight to the Ice Palace? It sounds like the Grinch's style.")
#     print("(B) Ask Pythius if he knows anything else about the Grinch's plans or possible hiding places? You don't want to jump to conclusions.")
    
#     choice = input("Enter A or B: ") # user input - was covered in the first lecture! 
    
#     if choice.lower() == "a":
#         go_to_ice_palace()
#     elif choice.lower() == "b":
#         more_info()
#     else:
#         print("Invalid choice. Try again!")
#         hot_cocoa()
    
# def go_to_mountain():
#     print("You have reached the end of this tutorial.")

# def go_to_ice_palace():
#     print("You have reached the end of this tutorial.")

# def more_info():
#     print("You have reached the end of this tutorial.")

# # this helps start the game, needs to be at the bottom of the script
# # to start game, navigate to your local folder
# # in my case, cd OneDrive/Desktop/projects/"Choose your own adventure"/revised 
# # open a terminal, pipenv shell, then hit enter

# if __name__ == "__main__":
#     start_adventure()


