# main.py file

import os
import hashlib

clear = lambda: os.system('cls')

users = []
address = []
loggedin = False
loggedin_user = ""
transcact_last = ""

def user_registration(username, password):
    clear()
    if(username not in users):
        username_hash = hashlib.sha256(bytes(username, 'utf-8')).hexdigest()
        password_hash = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        users.append(username)
        address.append([username, username_hash, password_hash, "Address", 0])
        print("-------------------")
        print("Success! User created")
        print("---Save your credentials")
        print("-------------------")
        print("Username:",username)
        print("Private Key:")
        print("Public Key:")
        print("Address:",username_hash)
        print("-------------------")
        return True
    else: 
        print("Failed! Try again")
        return False

def user_login(username, password):
    clear()
    username_hash = hashlib.sha256(bytes(username, 'utf-8')).hexdigest()
    password_hash = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
    # print(username, password, username_hash, password_hash)
    # print(address)
    loggedin = False
    for user in address:
        # print(user)
        if((username_hash == user[1]) and (password_hash == user[2])):
            loggedin = True
            return user[0]
            break
    if(not loggedin):
        return False

def user_list():
    for i in range(len(users)):
        print(users[i],address[i][1])

def user_find(to):
    for user in address:
        # print(user)
        if((to == user[0])):
            return True
            break

def address_list():
    for i in range(len(address)):
        print(i,"-",address[i][1])

def user_balance(loggedin_user):
    for user in address:
        # print(user)
        if((loggedin_user == user[0])):
            return user[4]
            break

def user_create_hane():
    hane_list = [["hane", "123"],["h4n3h","321"]]
    for i in hane_list:
        user_registration(i[0],i[1])

user_create_hane()

def user_add_balance(to, value):
    for user in address:
        # print(user)
        if((to == user[0])):
            user[4] += value
            break

user_add_balance("hane", 5)

def user_rem_balance(to, value):
    for user in address:
        # print(user)
        if((to == user[0])):
            user[4] -= value
            break

def user_transaction(ufrom, to, value):
    global transcact_last
    user_rem_balance(ufrom, value)
    user_add_balance(to, value)
    this_transaction = ufrom+" send SC$"+str(value)+" to "+to
    myblockchain.create_block_from_transaction([transcact_last, this_transaction])
    transcact_last = this_transaction
    return True

class SociCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(SociCoinBlock("0", ['Genesis Block']))
    
    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(SociCoinBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]

# t1 = "George sends 3.1 GC to Joe"
# t2 = "Joe sends 2.5 GC to Adam"
# t3 = "Adam sends 1.2 GC to Bob"
# t4 = "Bob sends 0.5 GC to Charlie"
# t5 = "Charlie sends 0.2 GC to David"
# t6 = "David sends 0.1 GC to Eric"

myblockchain = Blockchain()

# myblockchain.create_block_from_transaction([t1, t2])
# myblockchain.create_block_from_transaction([t3, t4])
# myblockchain.create_block_from_transaction([t5, t6])

while True:
    clear()
    print("SociCoin Wallet")
    print("-------------------")
    if(loggedin_user):
        print("Hello,",loggedin_user)
        print("Your balance is: SC$",user_balance(loggedin_user))
        balance = user_balance(loggedin_user)
    else:
        print("Hello, Anonymous")
    print("-------------------")
    print("1- List Transaction Chain")
    print("2- List Addresses")

    if(loggedin_user):
        print("3- Create Transaction")
    
    if(not loggedin_user):
        print("8- Login")
        print("9- Register")
    if loggedin_user: print("0- Exit")
    print("Insert one option:",end=" ")
    m = input()

    try:
        m = int(m)
    except ValueError:
        print("-------------------")
        print("Invalid option! Try again")
        print("-------------------")
        input()

    clear()

    if(m==1):
        print("List Transaction Chain")
        myblockchain.display_chain()
        input()

    if(m==2):
        print("Addresses List")
        address_list()
        input()

    if(loggedin_user):
        if(m==3):
            print("Create transaction")
            balance = user_balance(loggedin_user)
            print("Your balance:",balance)
            print("To Address:",end=" ")
            toaddress = input()
            if(user_find(toaddress)):
                print("Value:",end=" ")
                toaddress_value = int(input())
                if(toaddress_value <= balance):
                    print("Are you sure? (Type Y to Yes)")
                    sure = input()
                    if(sure == "Y"):
                        if(user_transaction(loggedin_user, toaddress, toaddress_value)):
                            print("Success! Transaction done!")
                    else: print("Transaction canceled!")
                else: print("You d'ont have balance enough to do this transaction! Try again")
            else: print("Failed to find this user! Try again")
            input()

        if(loggedin_user == "hane"):
            if(m==100):
                print("User List")
                user_list()
                print("Last transaction")
                print(transcact_last)
                input()
        

    if(not loggedin_user):

        if(m==8):
            print("Login")
            print("Username:",end=" ")
            login_username = input()
            print("Password:",end=" ")
            login_password = input()
            loggedin_user = user_login(login_username, login_password)
            if(loggedin_user):
                print("-------------------")
                print("Success! Loggen in,",loggedin_user)
                print("-------------------")
            else:
                print("Failed! Try again")
            input()

        if(m==9):
            print("Registration")
            print("Insert your username:",end=" ")
            regi_username = input()
            print("Insert your password:",end=" ")
            regi_password = input()
            user_registration(regi_username, regi_password)
            # if(Registration(regi_username, regi_password)):
            #     print("Success! User created")
            # else:
            #     print("Failed! Try again")
            input()

    if(m==0):
        print("Logged out")
        loggedin_user = 0
        input()

# myblockchain.display_chain()
