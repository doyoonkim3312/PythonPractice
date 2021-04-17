################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 16, 2021
# Description This program simulates transactions occurred in bank using customize
# class Account and Saving, which is subclass of Account
################################################################################

class Account:
    # Private Balance Value
    __balance: float

    # default Constructor
    def __init__(self, balance: float):
        self.__balance = balance
        print(f"New account balance: ${self.__balance:.2f}")

    def get_balance(self):
        return self.__balance

    def deposit(self, amount: float):
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            return False
        else:
            self.__balance -= amount
            return True



class Saving(Account):
    interest_rate: float

    # Default Constructor
    def __init__(self, balance: float, interest_rate: float):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def accrue_interest(self):
        interestPayment = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interestPayment)
        return interestPayment


def main():
    testInstance: Saving = Saving(200, 10)
    print(f"Balance: ${testInstance.get_balance():.2f}")

    print("Deposit: $12.34")
    testInstance.deposit(12.34)
    print(f"Balance: ${testInstance.get_balance():.2f}")

    print("Withdraw: $40.00")
    if testInstance.withdraw(40.00):
        print(f"Balance: ${testInstance.get_balance():.2f}")
    else:
        print("Insufficient funds. Withdrawal canceled.")

    print("Withdraw: $200.00")
    if testInstance.withdraw(200.00):
        print(f"Balance: ${testInstance.get_balance():.2f}")
    else:
        print("Insufficient funds. Withdrawal canceled.")

    print(f"Balance: ${testInstance.get_balance()}")
    print(f"Interest payment: ${testInstance.accrue_interest():.2f}")
    print(f"Interest payment: ${testInstance.accrue_interest():.2f}")
    print(f"Interest payment: ${testInstance.accrue_interest():.2f}")

    print("Withdraw: $200.00")
    if testInstance.withdraw(200.00):
        print(f"Balance: ${testInstance.get_balance():.2f}")
    else:
        print("Insufficient funds. Withdrawal canceled.")


if __name__ == '__main__':
    main()
