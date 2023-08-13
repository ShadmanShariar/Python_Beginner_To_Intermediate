# Author - Shadman Shariar
# Email - shadmanshariar007@gmail.com
# Github - https://github.com/ShadmanShariar

import math
import random

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(entry):

    # Use a breakpoint in the code line below to debug your script.

    print(f'Hello, {entry}')  # Press Ctrl+F8 to toggle the breakpoint.

def datatype():
    print('Single Quote')
    print("Double Quote")
    num = 10
    rating = 4.5
    complex = 4 + 5j
    bol = True
    list = ["a","b","c","d","e"]
    name = "Masterpiece"
    print(num,type(num))
    print(name,type(name))
    print(rating, type(rating))
    print(complex, type(complex))
    print(list, type(list))
    print(bol,type(bol))
    print("Side by",end=" ")
    print("Side")

def arithmetic():
    a = 5
    b = 3
    print(a + b) #Plus
    print(a - b) #Minus
    print(a * b) #Multiply
    print(a / b) #Divide Double
    print(a // b) #Divide Int
    print(a % b)  # Mod
    print(a ** b) #Power
    print(min(a,b))
    print(max(a,b))
    print(abs(-19))
    print(a ^ b) #XOR
    print(a & b) #AND
    print(a | b) #OR
    print(round(4.567554,2)) #4.57
    print(round(4.567554)) # 5
    print(math.floor(23.11))
    print(math.ceil(23.11))

def operators():
    a = 5
    b = 3
    print("a =",a,"b =",b)
    print("a > b", (a > b))
    print("a < b", (a < b))
    print("a >= b", (a >= b))
    print("a <= b", (a <= b))
    print("a == b", (a == b))
    print("a != b", (a != b))
    x = True
    y = False
    print(x and y) #False
    print(x or y) #True
    print(not y) #True

def condition():
    age = 18
    if(age >= 18):
        print("You can vote")
    else:
        print("You can not vote")

    num = -17
    if (num > 0):
        print("Positive")
    elif (num < 0):
        print("Negative")
    else:
        print("It's Zero")

def rangefunc():
    li = list(range(1,10,2))
    print(li)

def loop():
    for i in range(1,11,1):
        print(i,end=" ")
    print()
    print("10 "*10)
    list = ["anik","shadman","shariar"]
    for i in list:
        print(i)
    a = 1
    while(a<=5):
        print(a)
        a+=1
    for i in range(1,20,1):
        if(i==10):
            continue
        if(i%2==0):
            print("Even",i)
        i+=1
        if(i>10):
            break

def stringtheory():
    ex = "Shadman Shariar"
    print(ex)
    print(ex[0])
    print(len(ex))
    print(ex.split(" "))
    print(ex.count('S')) #2
    print(ex.index("man")) #4
    print(ex.endswith("iar")) #True
    print(ex[1:5]) #Substring
    print(ex[1:10:2]) #skip like increament

    for i in ex.split(" ")[0]:
        print(i)

    ex = ex.upper() #SHADMAN SHARIAR
    print(ex)
    print("213123".isdigit())
    print("sdasASd".isalpha())
    print("AB".isupper())
    s = " dffdsf fds  df ds fds "
    print(s.lstrip()) #dffdsf fds  df ds fds
    print(s.rstrip()) # dffdsf fds  df ds fds

def listtheory():
    list = [1,2,6,4,"Shadman"]
    print(list[1])
    print(list[4]*list[1]) #ShadmanShadman
    print(list.index(4)) #3
    list[0] = "Anik"
    print(list[0]) #Mutable

    # List Filtering
    #expresion - for item in list of range - if/else condition
    tmp = [i**2 for i in range(1,5,1) if(i%2==0)]
    print(tmp)

    #Create List
    ans = []
    ans.append(12)
    print(ans)
    ans.append(10) # 12,10
    print(ans)
    ans.insert(1,100) #positon - number
    print(ans) # 12,100,10
    ans.sort()
    #10,12,100
    ans.reverse()
    #100,12,10
    print(ans)
    print(ans.count(100)) #1
    print(ans.index(100)) #100
    print(len(ans)) #3
    print(max(ans)) #100
    print(min(ans)) #10
    # x = "Shadman"
    # print(list(x))
    print(sum(ans)) #122
    for ele in ans:
        print(ele)

    #Tupple Immutable and list Mutable
    # Tupple -> tp = (1,2,2,43,4)

def inputandoutput():
    name = input("Enter Your Name : ")
    print("Your name is :",name)
    num1 = int(input("Enter A Number : "))
    num2 = int(input("Enter Another Number : "))
    print("Sum is",(num1+num2))

def setfunc():
    arr= {1,1,2,24,2,43,43,2}
    arr = sorted(arr)
    print(arr) #1,2,24,43
    arr = sorted(arr,reverse=True)
    print(arr) #43,24,21,1

def mapfunc():
    map = {"Shadman":10,"Anik":12,"Shariar":16}
    print(map)
    # map = sorted(map.items())
    # print(map)
    #Sort map
    map2 = sorted(map.items())
    print(map2)
    if(map.__contains__("Shadman")):
        print("Found")
    else:
        print("Not Found")

def modulesys():
    print(random.randint(1, 10))
    print(round(math.pi, 2))
    print(dir(math))
    # print(math.gcd(1,2))
    # print(math.lcm(2,4))

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi("? Shadman is here !")
    datatype()
    arithmetic()
    operators()
    condition()
    rangefunc()
    loop()
    stringtheory()
    listtheory()
    setfunc()
    mapfunc()
    modulesys()
    #inputandoutput()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
