from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        user_balance = {i+1: balance[i] for i in range(len(balance))}
        self.user_balance = user_balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.user_balance.keys() and self.user_balance[account1] >= money\
                and account2 in self.user_balance.keys():
            self.user_balance[account1] -= money
            self.user_balance[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.user_balance.keys():
            self.user_balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.user_balance.keys() and self.user_balance[account] >= money:
            self.user_balance[account] -= money
            return True
        else:
            return False

if __name__ == '__main__':
    bank = Bank([10, 100, 20, 50, 30])
    op1 = bank.withdraw(3, 10)
    op2 = bank.transfer(5, 1, 20)
    op3 = bank.deposit(5, 20)
    op4 = bank.transfer(3, 4, 15)
    op5 = bank.withdraw(10, 50)
    print([op1, op2, op3, op4, op5])