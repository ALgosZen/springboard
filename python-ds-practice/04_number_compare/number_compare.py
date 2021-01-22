def number_compare(a, b):
    if a > b:
        print ("First is greater")
    elif b > a:
        print ("Second is greater")
    else:
        print ("Numbers are equal")

x = int(input("Input something: "))
y = int(input("Input something: "))
number_compare(x,y)