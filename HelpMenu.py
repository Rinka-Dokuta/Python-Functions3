def HelpMenu():
    choice = input("type p to pause, q to quit, s to summon")
    if choice == "p":
        print("pausing,,,")
    elif choice == "q":
        print("quiting")
    else:
        print("summoning...")
        
HelpMenu()        
