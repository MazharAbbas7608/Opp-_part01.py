# while loop ka simple tarika
i = 1
while i < 11:
    print("hello world -while")
    i += 1



num =int(input("enter table number"))
count =int(input("enter count number"))
i = 0
inputlist=[10,20,19,18,30,40,50,255,333]
evencount = 0
oddcount = 0
print("befor while")
while i < len(inputlist):
    if inputlist[i] % 2 == 0:
        evencount = evencount + 1
    else:            
        oddcount = oddcount + 1
    i += 1
print("even count:", evencount)
print("odd count:" , oddcount)



num =int(input("enter table number"))
count =int(input("enter count number"))
i = 0
inputlist=[10,20,19,18,30,40,50,255,333]
evensum = 0
oddsum = 0
print("befor while")
while i < len(inputlist):
    if inputlist[i] % 2 == 0:
        evensum = evensum + inputlist[i]
    else:            
        oddsum = oddsum + inputlist[i]
    i += 1
print("even sum:", evensum)
print("odd sum:" , oddsum)


