
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
        self.negative = 0.0
        self.catagories = []
        self.tag = ""
################################################################################################   
    def showCatagories(self):
        if not self.catagories:
            return -1
        else:
            for i in self.catagories:
                print(str(i.getName()) + " : " + str(i.getBalance()))
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
##########################################
class Format(object):
    @staticmethod
    def extend(subject):
        subject = subject.strip()
        retSubject = ""
        for i in subject:
            retSubject = retSubject + i + " "
        return retSubject
##########################################
########################################################################################### 

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
    print("E N T E R   A  V A L I D   C H O I C E: \n\n show) s h o w \n\n in) d e p o s i t \n\n out) w i t h d r a w \n\n trans) t r a n s f e r \n\n mkcat) c r e a t e  c a t a g o r y \n\n delcat) r e m o v e   c a t a g o r y \n\n opt) o p t i o n s \n\n q) q u i t")
 ###############################################################################################
def showDashboard():
    print("_______________________________________")
    print("\n          D A S H B O A R D ")
    print("_______________________________________")   
    print("\n\t C H E C K I N G : " + str(myChecking.getBalance()))
    for i in myChecking.catagories:
        cataName = Format.extend(i.getName())
        print("\n\t   * " + cataName + ": " + str(i.getBalance()))
    print("\n\t S A V I N G S : " + str(Savings.getBalance())) 
 ###############################################################################################
def transfer():
    notDone = True
    sum = 0.0 
    while(notDone):
        print("\n\t\t  T R A N S F E R   M E N U  ")  
        print("_______________________________________________________________________")
        print("\n\t E N T E R   A   V A L I D   C H O I C E: \n\n\t A) c h e c k i n g   t o   s a v i n g s \n\n\t B) s a v i n g s   t o   c h e c k i n g \n\n\t C) c a t a g o r y   t o   c a t a g o r y \n\n\t Q) q u i t")
        print("_______________________________________________________________________")
        userChoice = input("\t -->>").strip().upper()
    # CASE ONE : tranfer from checking to savings 
        if(userChoice == "A"):
            print(" \t f r o m   w h a t   c a t a g o r y   s h a l l   y o u   w i t h d r a w ? ")
            cataName = input("\t-->>").strip().lower()
            fail = True
            while(fail):
                try:
                    print("\t a m o u n t ?")
                    sum = float(input("\t-->>"))
                    fail = False
                except:
                    print("e r r o r  :  e n t e r   n u m e r i c a l   v a l u e s   o n l y ")
            retVal = myChecking.withdraw(sum, cataName) 
            if(retVal == -1):
                print("\te r r o r  :  n o   c a t a g o r i e s   a v a i l a b l e")
            elif(retVal == -2):
                print("\te r r o r  :  C H E C K I N G   O V E R D R A F T ") 
            elif(retVal == -3):
                print("\te r r o r  :  C A T A G O R Y   O V E R D R A F T ") 
            elif(retVal == -4):
                print("\te r r o r  :  c a t a g o r y   d. n. e. ")
            # now deposit to the Savings ONLY if checking exited normally.  
            elif(retVal == 0):
                Savings.deposit(sum)
                notDone = False
                print("\ts u c c e s s  :  $" + str(sum) + "  f r o m   " + Format.extend(cataName) + "  t o   s a v i n g s ")
    # CASE TWO : transfer from savings to checking
        elif(userChoice == "B"):
            print("\tt o   w h a t   c a t a g o r y   s h a l l   y o u   d e p o s i t  ? ")
            cataName = input("\t-->>").strip().lower()
            fail = False
            while(fail):
                try:
                    print("\t a m o u n t ?")
                    sum = float(input("\t-->>"))
                except:
                    print("e r r o r  :  e n t e r   n u m e r i c a l   v a l u e s   o n l y ")
            # THIS LINE IS NOT ALLOWED TO EXECUTE NORMALLY IF NO DESTINATION CATAGORY. Check destinations first! 
            if(myChecking.isCatagory(cataName)!= False):
                retVal = Savings.withdraw(sum)
                if (retVal == -1):
                    print("\te r r o r :  S A V I N G S   O V E R D R A F T")
            # deposit into the choice catagory if savings withdraw exited normally. 
                elif(retVal == 0):
                    myChecking.deposit(sum, cataName) 
                    notDone = False 
                    print("\ts u c c e s s  :  $" + str(sum) + " f r o m   s a v i n g s "  + " t o " + Format.extend(cataName))
            else:
                print("\te r r o r  :  c a t a g o r y   "  + Format.extend(cataName) +   "   d. n. e. ")
    # CASE THREE : tranfer from catagory to another catagory. 
        elif(userChoice == "C"):
            print("\tf r o m   w h a t   c a t a g o r y   s h a l l   y o u   w i t h d r a w ? ")
            fromHere = input("\t-->>").strip().lower()
            print("\tt o  w h a t   c a t a g o r y   s h a l l   y o u   d e p o s i t ? ")
            toHere = input("\t-->>").strip().lower() 
            fail = True
            while(fail):
                try:
                    print("\t a m o u n t ?")
                    sum = float(input("\t-->>"))
                    fail = False
                except:
                    print("e r r o r  :  e n t e r   n u m e r i c a l   v a l u e s   o n l y ") 
                # devise an "isCatagory" method to simplify checking. Once they both exist all we need to worry about is overdrafting when pulling from the first... 
                if (myChecking.isCatagory(fromHere)):
                    if(myChecking.isCatagory(toHere)):
                        retVal = myChecking.withdraw(sum, fromHere)
                        if(retVal == 0):
                            myChecking.deposit(sum,toHere)
                            notDone = False
                            print("\ts u c c e s s  :   " + str(sum) + "  f r o m   " + Format.extend(fromHere) + "  t o   " + Format.extend(toHere))
                        elif(retVal == -3):
                            print("\te r r o r  :  C A T A G O R Y   O V E R D R A F T ") 
                    else:
                        print("\te r r o r  :  c a t a g o r y  "  + Format.extend(toHere) +   "  d. n. e. ")
                else:
                    print("\te r r o r  :  c a t a g o r y  "  + Format.extend(fromHere) +   "  d. n. e. ") 
        elif(userChoice == "Q"):
            print("\tr e t u r n i n g   t o   m a i n")
            notDone = False

            
######################################################################################################################
######################################################################################################################
            #program entry 
######################################################################################################################
######################################################################################################################


# look before we leap and check to see if the file exists someplace
# if this  pickle load does not run, we will be attmepting to access null objects. 
if(os.path.isfile('account_data.pkl')):
    with open('account_data.pkl', 'rb') as readMe:
        myChecking = pickle.load(readMe)
        Savings = pickle.load(readMe)   

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
        print("t o   w h a t   a c c o u n t   s h a l l   y o u   d e p o s i t  ( s a v i n g s / c h e c k i n g ) ? ")
        accountName = input("-->>").strip().lower()
        if (accountName == "savings"):
            fail = True
            while(fail):
                try:
                    print("\t a m o u n t ?")
                    sum = float(input("\t-->>"))
                    fail = False
                except:
                    print("e r r o r  :  e n t e r   n u m e r i c a l   v a l u e s   o n l y ")
            Savings.deposit(sum)
            print("s u c c e s s  :  $" + str(sum) + "   d e p o s i t e d   t o   s a v i n g s")
        elif(accountName == "checking"):
            showDashboard()
            print("\nt o   w h a t   c a t a g o r y  s h a l l   y o u   d e p o s i t  ? ")
            cataName = input("-->>").strip().lower()
            fail = True
            while(fail):
                try:
                    print("\t a m o u n t ?")
                    sum = float(input("\t-->>"))
                    fail = False
                except:
                    print("e r r o r  :  e n t e r   n u m e r i c a l   v a l u e s   o n l y ")
            retVal = myChecking.deposit(sum, cataName) 
            if(retVal == -1):
                print("e r r o r  :  n o   c a t a g o r i e s   a v a i l a b l e")
            elif(retVal == -2):
                print("e r r o r  :  c a t a g o r y   d. n. e. ")  
            elif(retVal == 0):
                print("s u c c e s s  :  $" + str(sum) + "   d e p o s i t e d   t o    " + Format.extend(cataName))
        else:
            print("e r r o r  :  m a y   o n l y   d e p o s i t   t o   s a v i n g s   o r   c h e c k i n g ")     
# user makes withdraw  
    elif(userChoice == "out"):
        print("f r o m   w h a t   c a t a g o r y   s h a l l   y o u   w i t h d r a w ? ")
        accountName = input("-->>").strip().lower()
        fail = True
        while(fail):
            try:
                print("\t a m o u n t ?")
                sum = float(input("\t-->>"))
                fail = False
            except:
                print("e r r o r  :  e n t e r   n u m e r i c a l   v a l u e s   o n l y ")
        retVal = myChecking.withdraw(sum, accountName) 
        if(retVal == -1):
            print("e r r o r  :  n o   c a t a g o r i e s   a v a i l a b l e")
        elif(retVal == -2):
            print("e r r o r  :  C H E C K I N G   O V E R D R A F T ") 
        elif(retVal == -3):
            print("e r r o r  :  C A T A G O R Y   O V E R D R A F T ") 
        elif(retVal == -4):
            print("e r r o r  :  c a t a g o r y   d. n. e. ") 
        elif(retVal == 0):
            print("s u c c e s s  :  $" + str(sum) + "   w i t h d r a w n   f r o m   " + Format.extend(cataName))
# user makes transfer..... 
    elif(userChoice=="trans"):
        transfer()
# user creates a catagory...
    elif(userChoice == "mkcat"):
        print("e n t e r   n a m e  o f   c a t a g o r y ")
        cataName = input("-->>").strip()
        retVal = myChecking.createCatagory(cataName)
        # myChecking.createCatagory(cataName)
        if(retVal == -1):
            print("e r r o r  :  c a t a g o r y   d u p l i c a t e ")
        elif(retVal == 0):
            print("s u c c e s s  :  c r e a t e d  "  + Format.extend(cataName) + "  a s   c a t a g o r y")

# user attempts to remove catagory 
# -1) if no catagories -2) if catagory is not in list -3) if it's not balance 0. and 0 exited normally and executed user objective. 
    elif(userChoice == "delcat"):
        print("\te n t e r   a   v a l i d   a n d   e m p t y   c a t a g o r y   n a m e   t o   r e m o v e ")
        cataName = input("\t-->>").strip().lower()
        retVal = myChecking.removeCatagory(cataName)
        if(retVal == -1):
            print("\te r r o r  :  n o   c a t a g o r i e s   a v a i l a b l e")
        elif(retVal == -2):
            print("\te r r o r  :  c a t a g o r y   d. n. e. ") 
        elif(retVal == -3):
            print("\te r r o r  :  c a t o r y   b a l a n c e   m u s t   b e   0   t o   r e m o v e ")
        elif(retVal == 0):
            print("\ts u c c e s s  :  r e m o v e d   " + Format.extend(cataName))  
# options print 
    elif(userChoice == "opt"):
        menu()       
# quit 
    elif(userChoice == "q"):
        # need stuff like "save changes?"
        # gets us asking do we want auto saves with version control. if yes, how?
        with open('C:/vault/pycode/budgetproject/account_data.pkl', 'wb') as output:
            pickle.dump(myChecking, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(Savings, output, pickle.HIGHEST_PROTOCOL)
            print("d a t a   s a v e d")
    else: 
        print(userChoice + "  i s   n o t   a   r e c o g n i z e d   c o m m a n d ")