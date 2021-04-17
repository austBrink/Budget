from decimal import Decimal as d


#Illustrates how a valid
myRealNumber = d(1.10)+d(2.20)
myNumber = 1.1 + 2.2

print(myRealNumber)
print(myNumber)
print("formatted")
print("{:.2f}".format(myRealNumber))
print("{:.2f}".format(myNumber))