userreply = input('Do you want us to ship the package? (yes or no)')
if userreply == "yes":
    print('We can definitely help you :)')
    userAns = input("Would you like to buy stamps, an envelope, or make a copy? (Type stamps, envelope, or copy)")
    if userAns == 'stamps':
        print('We have plenty of stamp designs to choose from')
    elif userAns == 'envelope':
        print('We have plenty of enelope to choose from')
    elif userAns == 'copy':
        copies = input("How many copies would you like? (Type a number)")
        print(f"Here are {copies} copies.")
    
else:
    print('please come back if you wish to ship your package. Thank you!')