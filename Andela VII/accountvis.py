class Account(object):
    counter = 0
    
    def __init__(self, holder, number, balance,credit_line=1500):
        Account.counter += 1
        self.__Holder = holder
        self.__Number = number
        self.__Balance = balance
        self.__CreditLine = CreditLine

    def __del__(self):
        Account.counter =Account.counter - 1
