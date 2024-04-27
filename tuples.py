isTubles = (92,'vijay',{'name':'arra'},90,67,'hjh')


issecondtuple = (32,54,89)

addtuple = isTubles + issecondtuple
multipletuple = isTubles *2

# print(multipletuple)
# print(addtuple)

# (vijay,raj,*athi)= isTubles

# print(vijay)
# print(raj)
# print(athi)


# naan_tuble= (1,"9802",0,90,"878",{id:"namo"},["okok","okok"])
# print(naan_tuble.insert(),id(5))
# newTubles = isTubles.count(92)

# print(isTubles,'lpo')
# print(newTubles,'lpo')

# changeArr = list(isTubles)
# print(changeArr) 
# changeArr.insert(2,'vijay')
# changeArr.insert(5,'jay')
# changeArr.insert(0,'shri')

# convertTuble = tuple(changeArr)
# print(convertTuble)

# number = 10
# assert (number < 5), f"The number should not exceed 5. ({number=})"
# print(number)

while True:
    try:
        # x = int(input("Please enter a number: "))
        Numer = 1
        diname = 2
        if(diname != 0):
            result = Numer/ diname
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

some = "I am Vijay, Hello ,okk"
get = some.split(",")
print(get.pop())