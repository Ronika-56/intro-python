from python_classes3 import Account


def add(x,y):
    return x/y

def avg(numbers):
    return sum(numbers)/len(numbers)


def printDetails(details:dict):
    for key, value in details.items():
        print(f"{key}: {value}")

def daysOfTheWeek(weekdays: set):
    for item in weekdays:
        print(item)



def sides(data: tuple):
    print(data)


def show_balance(account : Account):
    """Takes in an account and displays its balance."""
    print(account.balance)


acc1= Account("001" ,"Jim Chang" ,2000)
show_balance(acc1)

print(avg([1 ,2 ,3 ,4 ,5 ,6]))
daysOfTheWeek({"Monday" , "Tuesday" , "Wednesday" , "Thursday"})