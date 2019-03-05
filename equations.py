#Equations for the accounting calculator


def test():
    selection = input("What do you want to test? ")
    print (selection)
    numOne = input("num1: ")
    numTwo = input("num2: ")
    numThree = input("num3: ")
    if selection == 1:
        print (accountingEquation(numOne, numTwo))

    elif selection == 2:
        print (netIncome(numOne, numTwo))

    elif selection == 3:
        print (breakEvenPoint(numOne, numTwo, numThree))

    elif selection == 4:
        print (cashRatio(numOne, numTwo))

    elif selection == 5:
        print (profitMargin(numOne, numTwo))

    elif selection == 6:
        print (debtEquityRatio(numOne, numTwo))

    elif selection == 7:
        print (costOfGoodsSold(numOne, numTwo, numThree))

    else:
        print("you are getting an error")


def accountingEquation (liability, equity):
    assets = liability + equity
    print (assets)
    return assets


def netIncome (revenues, expenses):
    income = revenues - expenses
    print ("2: ")
    return income


def breakEvenPoint(fixed, sales, variable):
    temp = fixed/sales
    breakeven = temp - variable
    print ("3: ")
    return breakeven


def cashRatio(cash, liabilities):
    ratio = cash/liabilities
    print ("4: ")
    return ratio


def profitMargin(income, sales):
    margin = income/sales
    print ("5: ")
    return sales


def debtEquityRatio(liabilities, equity):
    ratio = liabilities/equity
    print ("6: ")
    return ratio


def costOfGoodsSold(materials, inventory, outputs):
    temp = materials/inventory
    goodsSold = temp-outputs
    print ("7: ")
    return goodsSold


test() 