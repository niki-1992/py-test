# mystring = "this is my string"
# print(mystring)
# print(type(mystring))
# print(mystring + " is of data type" + str(type(mystring)))

# firststring = "water"
# secondstrinf = "fall"
# total = firststring + " " +  secondstrinf
# print(total)
# print(type(total))

# name = input("what is your name?")
# print(f"my name is { name}")

# colour= input("what is your favorite colour? ")
# animal =input(" what is your favorite animal")
# print(f"My favorite colour is {colour} and my favorite animal is {animal} ")

# username = input("What is your username?")
# password = input("what is your password?")
# pass_len = len(password)
# hidden_pass = '*' * pass_len
# print(f"{username} your password is {hidden_pass} and the lenght of ur password is {pass_len}")

word = 'reviver'
p = bool(word.find(word[::-1])+1)
print(p)