#Question1
def years():
    num=int(input("enter the days:"))
    years = num//365
    months = (num-years*365)//30
    days =(num- years*365-months*30)
    print(num,"days=",years,"years",months,"months",days,"days")
years()



#Question2
a, b = 1, 1
print("Fibonacci sequence:")
while a < 20:
    print(a)
    c = a + b   
    a = b
    b = c


#Question3
player1=input("Enter Player name 1:")
player2=input("Enter Player name 2:")
p1,p2=0,0
choice1=input("Enter Player 1 Choice:").lower()
choice2=input("Enter Player 2 Choice:").lower()
if(choice1==choice2):
    print("Tie")
elif(choice1=="rock"):
    if(choice2=="scissor"):
        p1=1
    else:
        p2=1
elif(choice1=="scissor"):
    if(choice2=="paper"):
        p1=1
    else:
        p2=1
elif(choice1=="paper"):
    if(choice2=="rock"):
        p1=1
    else:
        p2=1
if(p1==1):
    print(player1, "with choice",choice1,"wins")
    print(player2, "with choice",choice2,"lose")
elif(p2==1):
    print(player2, "with choice",choice2,"wins")
    print(player1, "with choice",choice1,"lose")


#Question4

def allowances():
    allowance=(22/100)*salary+(18/100)*salary+(10/100)*salary
    #print(allowance)
    return allowance

def deductions():
    if(salary>8000):
        profitTax=200
    else:
        profitTax=150
    deduction=profitTax+((12/100)*salary)+((8/100)*salary)
    #print(deduction)
    return deduction
    

    
def grossSalary(basicsalary):
    allowance=allowances()
    gross_salary = basicsalary + allowance
    print("Gross salary is :",gross_salary)
    netsalary(gross_salary)
    

def netsalary(grosssalary):
    deduction=deductions()
    net_salary = grosssalary - deduction
    print("Net salary is :",net_salary)


salary=int(input("enter your basic salary:"))
grossSalary(salary)

#Question5

string="""
Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code"""
string.lower()
consonants=0
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in string:
    if i in vowels:
        vowels[i]+=1
    elif(i.isalpha()):
        consonants+=1
for key in vowels:
    print(key,":",vowels[key])
print("consonants:",consonants)

#Question6
string1=input("Enter the string:")
if(string1==string1[::-1]):
    print(string1,"is palindrome")
else:
    print(string1,"is not palindrome")

#Question7
email=input("Enter email:")
counta=0
countd=0
if(email[0]=='@' or email[0]=='.' or email[-1]=='@' or email[-1]=='.' ):
    print("email not valid")
else:
    for i in email:
        if(i=='@'):
           counta+=1
        elif(i=='.'):
            countd+=1
    if(counta==1 and countd==1):
        print("email valid")
    else:
        print("Email not valid")
    
#Question 8

def rental_car_cost(days):
    if days >= 7:
        car_cost = (40*days)-50
    elif days >= 3:
        car_cost = (40*days)-20
    else:
        car_cost = 40*days
    return car_cost

def hotel_cost(night):
    return 140*night

def plane_ride_cost(city):
    if city == 'charlotte':
        return 183
    elif city == 'tampa':
        return 220
    elif city == 'pittsburgh':
        return 222
    elif city == 'los angeles':
        return 475
    else:
        print("Invalid ")



def trip_cost(city,days,spending_money):
    cost= int(rental_car_cost(days)+ plane_ride_cost(city) + hotel_cost(days)+spending_money)
    print ("Total Cost : ",cost)

city = input("Enter the city (charlotte,tampa,pittsburgh,los Angeles) : ").lower()
days = int(input("Enter no. of days : "))
spending_money = int(input("Enter the amount : "))
trip_cost(city,days,spending_money)


#Question9
bakery_items={"bread":40,"butter":120,"jam":200,"cheese":220,"crossiant":60}
cart={}
def display():
    print(bakery_items)
    

def add():
    item=input('''Enter the item:
                  Bread
                  Butter
                  jam
                  Cheese
                  crossiant
                  :''').lower()
          
    if(item not in bakery_items):
        print("wrong item")
    elif item not in cart:
        cart[item]=1
    else:
        print("already in cart")
        

def view_cart():
    print(cart)

def update():
    item=input('''Enter the item:
                  Bread
                  Butter
                  jam
                  Cheese
                  crossiant
                  :''').lower()
    if(item not in bakery_items):
        print("wrong item")
    elif item in cart:
        qt=int(input("Enter Quantity:"))
        cart[item]=qt    
def remove():
    item=input('''Enter the item:
                  Bread
                  Butter
                  jam
                  Cheese
                  crossiant
                  :''').lower()
    if(item not in bakery_items):
        print("wrong item")
    elif item in cart:
        del cart[item]
def bill():
    print("-------Bill information-------")
    print("item \t","cost\n")
    cost=0
    for item in cart:
          print(item,"\t",cart[item]*bakery_items[item],"\n")
          cost=cost+cart[item]*bakery_items[item]
    print("Total cost:",cost)        
flag=0
while(flag==0):
    print("-------------Shopping Cart--------------")
    choice=int(input('''Enter the choice
                   1. View the bakery items
                   2. Add the item into the cart
                   3. View the cart
                   4. Update item in the cart
                   5. Remove item from the cart
                   6. Checkout and generate bill
                   :
            '''))

    if(choice==1):
        display()
    elif(choice==2):
        add()
    elif(choice==3):
        view_cart()
    elif(choice==4):
        update()
    elif(choice==5):
        remove()
    elif(choice==6):
        bill()
        flag=1
    


         
