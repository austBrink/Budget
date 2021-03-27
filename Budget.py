import pickle
import os  
###############################################################################################
###############################################################################################
class Account:
    def __init__(self, name):
        self.name = name 
        self.balance = 0.0 
        self.negative = 0.0

    def deposit(self, sum: float):
        self.balance = self.balance + sum 

    def withdraw(self, sum: float):
        self.negative = self.balance - sum 
        if(sum <= self.balance):
            self.balance = self.balance - sum 
            return 0 
        elif(sum > self.balance):
            return -1

    def getBalance(self):
        return self.balance 

    def getNegative(self):
        return self.negative

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

 ###############################################################################################
 ###############################################################################################
 # Checking class 
 ###############################################################################################
 ###############################################################################################

class Checking(Account):
    def __init__(self, name):
        self.name = name 
        self.balance = 0.0 
        self.boa = 0.0
        self.catagories = []
        self.tag = ""
################################################################################################
    def updateBoa(self, sum):
        self.boa = self.boa + sum 
################################################################################################
    def getBoa(self):
        return self.boa
################################################################################################
    def showCatagories(self):
        if not self.catagories:
            return -1
        else:
            for i in self.catagories:
                print(str(i.getName()) + " : " + str(i.getBalance()))
 ###############################################################################################
    def payBoa(self, sum):
        self.boa = self.boa - sum
 ###############################################################################################
# adds an account to the list in the checking account.
# RETURN: -1 if that's already a catagory. 0 if added.  
    def createCatagory(self, catagoryName):
        catagoryName = catagoryName.lower().strip()
        for i in self.catagories:
            if (i.getName() == catagoryName):
                return -1
        catagory = Account(catagoryName)
        self.catagories.append(catagory)
        return 0 
###############################################################################################
# this function checks to see if a catagory is valid. 
# RETURNS... -1) no catagories -2) not found 0) found / valid  
    def isCatagory(self, catagoryName):
        for i in self.catagories:
            if (i.getName() == catagoryName):
                return i 
        return False
###############################################################################################
# option for removing a catagory....coming soon
    def deleteCatagory(self, nameTag):
        pass
###############################################################################################
# getCatagory returns the catagory object if found./
# RETURN 
# account object) if found 
# -1) if catagory list was empty 
# -2) if not found in catagory list  
    def getCatagory(self, nameTag):
        if not self.catagories:
            return -1 
        else: 
            for i in self.catagories:
                if i.getName() == nameTag:
                    return i  
        return -2  
###############################################################################################
 # 'deposit' checks if the passed catagoryName exists in catagory list and deposits given float sum. Does not use isCatagory and getCatagory to avoid two loop executions.
 # RETURN: 
 # 0) If found and deposited 
 # -1) if no catagories 
 # -2) if no such catagory exists (DNE) Any exit code other than 0 does not execute the deposit
    def deposit(self, sum, catagoryName):
        if not self.catagories:
            return -1 
        else: 
            for i in self.catagories:
                if (i.getName() == catagoryName):
                    i.deposit(sum)
                    self.balance = self.balance + sum 
                    return 0 
            return -2 
 ###############################################################################################
    # removes float variable sum from the balance of catagory in self.catagories. 
    # RETURNS 0 for success -1) for empty catagory list -2) for TOTAL CHECKING overdraft -3) for catagory overdraft -4) no such catagory exists in catagorylist   
    # me from the future.... this is a really crap function. 
    def withdraw(self,sum,catagoryName):
        if (not self.catagories):
            return -1
        # now see if the user's catagory is in the list 
        catagory = self.getCatagory(catagoryName)
        if(catagory != -2):
            if(self.balance < sum):
                return -2
            elif(catagory.getBalance() < sum):
                return -3
            else:
                catagory.withdraw(sum)
                self.balance = self.balance - sum
                return 0
        else:
            return -4
# create a function to remove catagory. It must exist and must be zero balance.
# RETURNS: 
# -1) if no catagories -2) if catagory is not in list -3) if it's not balance 0. and 0 exited noramlly and executed user objective. 
    def removeCatagory(self, catagoryName):
        if (not self.catagories):
            return -1 
        elif(self.isCatagory(catagoryName) == False):
            return -2 
        else:
            catagory = self.getCatagory(catagoryName)
            if(catagory.getBalance() != 0):
                return -3
            else:
                self.catagories.remove(catagory)
                return 0
###########################################################################################     



###########################################################################################
# MAIN PROGRAM #  
###########################################################################################


###############################################################################################
def header():
    print("_______________________________________")
    print("_______________________________________")
    print("\n             B U D G E T ")
    print("_______________________________________")    
    print("_______________________________________")
 ###############################################################################################
def menu():
    print("E N T E R   A  V A L I D   C H O I C E: \n\n show) s h o w \n\n in) d e p o s i t \n\n out) w i t h d r a w \n\n trans) t r a n s f e r \n\n mkcat) c r e a t e  c a t a g o r y \n\n rmcat) r e m o v e   c a t a g o r y \n\n opt) o p t i o n s \n\n q) q u i t \n\n p) p a y   b o a  \n")
 ###############################################################################################
def showDashboard():
    print("Accounts and Categories:")
    print("checking: " + str(myChecking.getBalance()))
    for i in myChecking.catagories:
        accountName = i.getName()
        print("* " + accountName + ": " + str(i.getBalance()))
    print("Bank of America: " + str(myChecking.getBoa()))
    print("Savings: " + str(Savings.getBalance())) 
 ###############################################################################################
def transfer():
    notDone = True
    sum = 0.0 
    while(notDone):
        print("\n  T R A N S F E R   M E N U  ")  
        print("_______________________________________________________________________")
        print("\n E N T E R   A   V A L I D   C H O I C E: \n\n A) c h e c k i n g   t o   s a v i n g s \n\n B) s a v i n g s   t o   c h e c k i n g \n\n C) c a t a g o r y   t o   c a t a g o r y \n\n Q) q u i t")
        print("_______________________________________________________________________")
        userChoice = input("-->>").strip().upper()
    # CASE ONE : tranfer from checking to savings 
        if(userChoice == "A"):
            accountName = input("withdraw from-->>").strip().lower()
            fail = True
            while(fail):
                try:
                    sum = float(input("amount-->>"))
                    fail = False
                except:
                    print("error: enter numerical values only")
            retVal = myChecking.withdraw(sum, accountName) 
            if(retVal == -1):
                print("error: no categories available")
            elif(retVal == -2):
                print("error: attempted checking overdraft") 
            elif(retVal == -3):
                print("error: attempted category overdraft") 
            elif(retVal == -4):
                print("error: " + accountName + " is not a valid category")
            # now deposit to the Savings ONLY if checking exited normally.  
            elif(retVal == 0):
                Savings.deposit(sum)
                notDone = False
                print("success :  $" + str(sum) + " from " + accountName + " to Savings")
    # CASE TWO : transfer from savings to checking
        elif(userChoice == "B"):
            accountName = input("to category-->>").strip().lower()
            fail = True
            while(fail):
                try:
                    sum = float(input("amount-->>"))
                    fail = False
                except:
                    print("error: enter numerical values only")
            # THIS LINE IS NOT ALLOWED TO EXECUTE NORMALLY IF NO DESTINATION CATAGORY. Check destinations first! 
            if(myChecking.isCatagory(accountName)!= False):
                retVal = Savings.withdraw(sum)
                if (retVal == -1):
                    print("error: attempted savings overdraft")
            # deposit into the choice catagory if savings withdraw exited normally. 
                elif(retVal == 0):
                    myChecking.deposit(sum, accountName) 
                    notDone = False 
                    print("success :  $" + str(sum) + " from savings to " + accountName)
            else:
                print("error: " +  accountName +   " is not a valid category")
    # CASE THREE : tranfer from catagory to another catagory. 
        elif(userChoice == "C"):
            fromHere = input("from category-->>").strip().lower()
            toHere = input("to category-->>").strip().lower() 
            fail = True
            while(fail):
                try:
                    sum = float(input("amount-->>"))
                    fail = False
                except:
                    print("error: enter numerical values only")
                # devise an "isCatagory" method to simplify checking. Once they both exist all we need to worry about is overdrafting when pulling from the first... 
                if (myChecking.isCatagory(fromHere)):
                    if(myChecking.isCatagory(toHere)):
                        retVal = myChecking.withdraw(sum, fromHere)
                        if(retVal == 0):
                            myChecking.deposit(sum,toHere)
                            notDone = False
                            print("success: " + str(sum) + " from " + fromHere + " to " + toHere)
                        elif(retVal == -3):
                            print("error: attempted category overdraft") 
                    else:
                        print("error "  + toHere +   " is not a valid category")
                else:
                    print("error: "  + fromHere +   "  is not a valid category") 
        elif(userChoice == "Q"):
            print("returning you to main")
            notDone = False

            
######################################################################################################################
######################################################################################################################
            #program entry 
######################################################################################################################
######################################################################################################################

# look before we leap and check to see if the file exists someplace
# if this  pickle load does not run, we will be attmepting to access null objects. 

#myChecking = Checking("Checking")
#Savings = Account("Savings") 

if(os.path.isfile('account_data.pkl')):
    with open('account_data.pkl', 'rb') as readMe:
        myChecking = pickle.load(readMe)
        Savings = pickle.load(readMe)  
    readMe.close() 

# print out initial displays      
header() 
menu() 

# initialize user choice
userChoice = "" 
sum = 0.0 
# MENU LOOP 
while(userChoice != "q"):
    userChoice = input("-->>").strip().lower()
    if(userChoice == "show"):
        showDashboard()
# user makes deposit 
    elif(userChoice == "in"):
        accountName = input("to account-->>").strip().lower()
        if (accountName == "savings"):
            fail = True
            while(fail):
                try:
                    sum = float(input("amount-->>"))
                    fail = False
                except:
                    print("error: enter numerical values only")
            Savings.deposit(sum)
            print("s u c c e s s  :  $" + str(sum) + " deposited to savings")
        elif(accountName == "checking"):
            showDashboard()
            accountName = input("to category-->>").strip().lower()
            fail = True
            while(fail):
                try:
                    sum = float(input("amount-->>"))
                    fail = False
                except:
                   print("error: enter numerical values only")
            retVal = myChecking.deposit(sum, accountName) 
            if(retVal == -1):
                print("error: no categories available")
            elif(retVal == -2):
                print("error: " + accountName + " is not a valid category")  
            elif(retVal == 0):
                print("success: $" + str(sum) + " deposited to " + accountName)
        else:
            print("error: choose either checking or savings to deposit")     
# user makes withdraw 
    elif(userChoice == "out"):
        accountName = input("from category-->>").strip().lower()
        isCredit = False 
        fail = True
        while(fail):
            credit = input("was this purchase on credit?-->>(y/n)").strip().lower() 
            if(credit == "y"):
                isCredit = True
                fail = False
            elif(credit == "n"):
                fail = False   
        fail = True
        while(fail):
            try:
                sum = float(input("amount-->>"))
                fail = False
            except:
                print("error: enter numerical values only")
        retVal = myChecking.withdraw(sum, accountName) 
        if(retVal == -1):
            print("error: no categories available")
        elif(retVal == -2):
            print("error: attempted checking overdraft") 
        elif(retVal == -3):
            print("error: attempted category overdraft") 
        elif(retVal == -4):
            print("error: " + accountName + " is not a valid category") 
        elif(retVal == 0):
            if(isCredit):
                myChecking.updateBoa(sum) 
            print("success:  $" + str(sum) + " withdrawn from " + accountName)
            
# user makes transfer..... 
    elif(userChoice=="trans"):
        transfer()
# user creates a catagory...
    elif(userChoice == "mkcat"):
        accountName = input("name-->>").strip()
        retVal = myChecking.createCatagory(accountName)
        # myChecking.createCatagory(accountName)
        if(retVal == -1):
            print("error: " + accountName + " already exists, man")
        elif(retVal == 0):
            print("success: created "  + accountName + " as category")

# user attempts to remove catagory 
# -1) if no catagories -2) if catagory is not in list -3) if it's not balance 0. and 0 exited normally and executed user objective. 
    elif(userChoice == "rmcat"):
        accountName = input("remove-->>").strip().lower()
        retVal = myChecking.removeCatagory(accountName)
        if(retVal == -1):
            print("error: no categories available")
        elif(retVal == -2):
            print("error: " + accountName + " is not a valid category") 
        elif(retVal == -3):
            print("error: category balance must be zero to remove")
        elif(retVal == 0):
            print("success: removed " + accountName)  
# options print 
    elif(userChoice == "opt"):
        menu()       
# quit 
    elif(userChoice == "q"):
        # need stuff like "save changes?"
        # gets us asking do we want auto saves with version control. if yes, how?
        try:
            with open('account_data.pkl', 'wb') as output:
                pickle.dump(myChecking, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(Savings, output, pickle.HIGHEST_PROTOCOL)
                output.close()
                print("saved your data")
        except:
            print("error: could not save")
            userChoice = ""
    elif(userChoice == "p"):
        print("BOA current balance-->>" + str(myChecking.getBoa()))
        fail = True
        while(fail):
            try:
                sum = float(input("How much to pay down?-->>"))
                fail = False
            except:
                print("error: enter numerical values only")
        myChecking.payBoa(sum)
    else: 
        print(userChoice + "  is not a recognized command")