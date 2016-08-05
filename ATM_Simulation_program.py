import threading


class ATM_Operation(object):
    def __init__(self):
        self.bank_user = {1234789: 111111,
                          1111111: 111101
                         }
        self.format_money = 0
        self.count_money = 0
        self.login_count = 0

# the return value
# return 1  login in successful
# return 2  user name does not exist
# return 3  user input of Number
# return 4  wrong password more than three times
    def login_return(self,username,password):
        if self.login_count >= 3:
            return 4
        try:
            if int(password) == self.bank_user[int(username)]:
                return 1
            else:
                self.login_count +=1
                print "User name password wrong "
        except KeyError:
            print "user name does not exist", username
            return 2
        except ValueError:
            return 3

    def view_bank_balance(self):
        if thread.acquire(2):
            print "Hello , your account have %d RMB now" % self.count_money
            thread.release()
            return self.count_money

# a deposit status code
# return 0  login in successful
# return 1  user input error
    def deposit(self, money):
        format_money = self.amount_format_processing(money)
        if format_money < 0:
            return 1
        else:
            if thread.acquire(2):
                old_money = self.count_money
                try:
                    self.count_money += format_money
                    print "Hello , your account have %d RMB now" % self.count_money
                    thread.release()
                    return 0
                except Exception:
                    self.count_money = old_money

# a withdrawal status code
# return 0  User input amount is too large
# return 1  login in successful
# return 2  ser input error
    def withdrawals(self,money):
        old_money = self.count_money
        try:
            format_money = self.amount_format_processing(money)
            if format_money < 0:
                return 2
            else:
                if thread.acquire(2):
                    if format_money < self.count_money:
                        self.count_money -= format_money
                        thread.release()
                        return 1
                    return 0
        except Exception:
            self.count_money = old_money

    def amount_format_processing(self, money):
        try:
            self.format_money = int(money)
        except ValueError:
            self.format_money = -1
        if '.' in str(money):
            self.format_money = -2
        elif self.format_money < 0:
            self.format_money = -3
        return self.format_money

thread = threading.Lock()



atm = ATM_Operation()
print atm.login_return(1234789,111111)