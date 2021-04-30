# myfruit= ['apple', 'bananna', 'orange']
# myfruit[1]= 'cherry'

# print(myfruit.extend('tomato'))

# print(myfruit)
# print(type(myfruit))
# print(len(myfruit))
# print(myfruit[0])
# print(myfruit[1:])
# print(myfruit[-1])
# print(myfruit[0:2:1])


#tuple- immutable
# mytuple= ('apple', 'bananna', 'pineapple')
# print(mytuple)
# print(mytuple[2])


myDict = {
  "Adam" : "apple",
  "Ben" : "banana",
  "Penny" : "pineapple"
}
print(myDict)
print(type(myDict))
print(list(myDict.keys()))
print(list(myDict.items()))
print(list(myDict.values()))
print(myDict.get('Ben'))
print(myDict['Penny'])