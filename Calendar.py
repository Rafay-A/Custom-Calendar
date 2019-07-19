#This is the main function where the program will execute:

def calendar(n,d):
    #This will print the base of the calendar.
    print("     Sun     Mon     Tue     Wed     Thu     Fri     Sat")
    
    #The first while loop here is used to add number of spaces before the starting day.
    i=1
    while i<d:
        print("    ",end="\t")
        i=i+1
        
    #This second loop will print the number of days, the user will enter along with the spaces required between them.
    for j in range(1,n+1):
        print("    ",j,end="\t")
        
        #This if condition will print the number on the next line after the seventh day.
        if (j+d-1)%7==0:
            print("\n")

    print()
    input()

###The program Starts from here:

n=int(input("Enter the number of days you want in a month(28-31):"))
d=int(input("Enter from which day you want to start?(1=Sun,7=Sat):"))

if 28>n>31:
    print("Invalid Input")
elif 1>d>7:
    print("Invalid Input")
else:
    calendar(n,d)





