class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f'book\'s title is {self.title}, book\'s author is {self.author}, {self.year}')

book2 = Book('Harry Potter', 'J.K.Rowling', '1997')
book2.info()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        self.x = float(input('enter x coordinate: '))
        self.y = float(input('enter y coordinate: '))
        print(((point2.x) ** 2 + (point2.y) ** 2) ** 0.5)
    
point2 = Point('', '')
point2.distance_to_zero()

value = 0
class Counter:

    def __init__(self, value):
        self.value = value
    
    def increment(self):
        global value
        value += 1      
        print(value)

    def decrement(self):
        global value
        value -= 1      
        print(value)

    def reset(self):
        global value
        value = 0      
        print(value)

while True:
    ques1 = input('choose the operation(+, -, 0): ')
    if ques1 == '+':
        value2 = Counter(0)
        value2.increment()
    elif ques1 == '-':
        value2 = Counter(0)
        value2.decrement()
    elif ques1 == '0':
        value2 = Counter(0)
        value2.reset()
    else:
        break

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('ljfdljsdlfjldsfjl')
    
class Dog(Animal):
    def speak(self):
        return 'Woof'
    
class Cat(Animal):
    def speak(self):
        return 'Meow'
    
dog = Dog('Whiskers')
cat = Cat('Buddy') 
print(dog.speak())
print(cat.speak())

balance = 0
class BankAccount:

    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self):
        global balance
        ammount = int(input('enter the ammount of money, you want to add: '))
        balance += ammount      
        print(balance)

    def withdraw(self):
        global balance
        ammount = int(input('enter the ammount of money, you want to substruct: '))
        balance -= ammount      
        print(balance)

    def reset(self):
        global balance     
        print(balance)

while True:
    ques1 = input('choose the operation(+, -, 0): ')
    if ques1 == '+':
        balance2 = BankAccount(0)
        balance2.deposit()
    elif ques1 == '-':
        balance2 = BankAccount(0)
        balance2.withdraw()
    elif ques1 == '0':
        balance2 = BankAccount(0)
        balance2.reset()
    else:
        break

items = []
class Store:
    def __init__(self, name):
        self.name = name
        

    def add_items(self):
        global items
        nme = input('Enter the name of the item: ')
        items.append(nme)

    def remove_item(self):
        global items
        nme = input('Enter the name of the item: ')
        if nme in items:
            items.remove(nme)
        else:
            print('There is no such item')
    
    def list_items(self):
        global items
        print(items)

while True:
    ques1 = input('choose the operation(+, -, 0): ')
    if ques1 == '+':
        item2 = Store('')
        item2.add_items()
    elif ques1 == '-':
        item2 = Store('')
        item2.remove_item()
    elif ques1 == '0':
        item2 = Store('')
        item2.list_items()
    else:
        break









    

    








    

