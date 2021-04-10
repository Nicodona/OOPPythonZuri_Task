# class Yowa:
#     eleven = 12
#
#     def onLine(self):
#         print('hello world')
#
#
#
#
# print(Yowa.eleven)
# print(Yowa.onLine)


class Budget:
    def __init__(self, categories: str, amount: int=0):
        self.categories = categories
        self.amount = amount

    def deposite(self):
        # option = input('which category do you want to deposite money from')
        deposite_to = int(input('how much do you want to deposite from '))
        self.amount = self.amount + deposite_to
        return self.amount
        #
        # if option == 'food':
        #     food.amount = food.amount + deposite_to
        #     return food.amount
        #
        # elif option == 'clothing':
        #     clothing.amount = clothing.amount + deposite_to
        #     return clothing.amount
        #
        # elif option == 'entertainment':
        #     entertaintment.amount = entertaintment.amount + deposite_to
        #     return entertaintment.amount
        # else:
        #     print('invalid otption')
        #     return None

    def withdraw(self):
        withdraw_from = int(input('how much do you want to withdrwa from '))
        self.amount = self.amount - withdraw_from
        return self.amount

    def transferTo(self):
        transfer = int(input('How much do you want to transfer from this account'))
        self.amount = self.amount - transfer
        return transfer

    def transferFrom(self):

        recieved = self.transferTo()
        print(recieved)
        # self.amount = self.amount + recieved
        # return self.amount





    def computeBalance(self):
        deposit = self.deposite()
        withdraw = self.withdraw()
        fund = self.amount + deposit - withdraw
        return fund


food = Budget('food', 20000)
clothing = Budget('clothing', 10000)
entertaintment = Budget('entertainment', 5000)


print('what do you want to do with a category')
choice = int(input('enter choice to either\n 1 to deposite\n or 2 to withdraw\n or 3 to trannsfer fundfrom one category to another\n'))
if choice == 1:
    obj = int(input('what category do you want to work with?\n enter 1 for food category\n enter 2 for clothing category\n enter 3 for entertainments category\n'))
    if obj == 1:
       food.deposite()
       print(food.amount)
    elif obj == 2:
        clothing.deposite()
        print(clothing.amount)
    elif obj == 3:
        entertaintment.deposite()
        print(entertaintment.amount)
    else:
        print('invalid object selection')
elif choice == 2:
    obj = int(input('what category do you want to work with?\n enter 1 for food category\n enter 2 for clothing category\n enter 3 for entertainments category\n'))
    if obj == 1:
       food.withdraw()
       print(food.amount)
    elif obj == 2:
        clothing.withdraw()
        print(clothing.amount)
    elif obj == 3:
        entertaintment.withdraw()
        print(entertaintment.amount)
    else:
        print('invalid object selection')

elif choice == 3:
    obj = int(input( 'what category do you want to work with?\n enter 1 for food category\n enter 2 for clothing category\n enter 3 for entertainments category\n'))
    if obj == 1:
        print(' enter 1 to transfer to clothing category ')
        print(' enter 2 to transfer to entertainment category ')
        food.transferTo()
        print(food.amount)
        trans = int(input('which category are you traffering cash to?'))
        if trans == 1:
            clothing.transferFrom()
            print(clothing.amount)
        elif trans == 2:
            entertaintment.transferFrom()
            print(entertaintment.amount)
        else:
            print('invalid object selection')



    elif obj == 2:
        print(' enter 1 to transfer to food category ')
        print(' enter 2 to transfer to entertainment category ')
        clothing.transferTo()
        print(clothing.amount)


        trans = int(input('which category are you traffering cash to?'))
        if trans == 1:
            food.transferFrom()
            print(food.amount)

        elif trans == 2:
            entertaintment.transferFrom()
            print(entertaintment.amount)
        else:
            print('invalid object selection')


    elif obj == 3:
        print(' enter 1 to transfer to food category ')
        print(' enter 2 to transfer to clothing category ')
        entertaintment.transferFrom()
        print(entertaintment.amount)
        trans = int(input('which category are you traffering cash to?'))


        if trans == 1:
            food.transferFrom()
            print(food.amount)
        elif trans == 2:
            clothing.transferFrom()
            print(clothing.amount)
        else:
            print('invalid object selection')
    else:
        print('invalid object selection')


# elif choice == 2:
#     food.withdraw()
# else:
#     pass


