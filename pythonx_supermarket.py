def enterProducts():
    buyingData = {}
    add = "Y"
    enterDetails = True
    while True:
        details = input("Press A to add product and Q to quit: ").capitalize()
        if details == "A":
            product = input("Enter product: ").capitalize()
            quantity = int(input("Enter quantity: "))
            buyingData.update({product:quantity})
        elif details == "Q":
            break
            #enterDetails = False
        else:
            print("Please select a correct option")
        #add = input("Add again [Y/N]: ").capitalize()
    return buyingData

def getPrice(product, quantity):
    priceData = {
        "Biscuit": 300,
        "Chicken": 500,
        "Egg": 100,
        "Fish":300,
        "Coke": 200,
        "Bread": 200,
        "Apple": 300,
        "Onion": 300
    }
    subtotal = priceData[product] * quantity
    print(product + ":$" + str(priceData[product]) + "x" + str(quantity) + "=" + str(subtotal))
    return subtotal

def getDiscount(billAmount, membership):
    discount = 0
#    membership = input("Enter customer membership: ")
    if billAmount >= 25:
        if membership == "Gold":
            discount = 2
            discount_amount = billAmount * (discount/100)
            billAmount -= billAmount * (discount/100)
        elif membership == "Silver":
            discount = 1
            discount_amount = billAmount * (discount/100)
            billAmount -= billAmount * (discount/100)
        elif membership == "Bronze":
            discount = 0.5
            discount_amount = billAmount * (discount/100)
            billAmount -= billAmount * (discount/100)
        print(f"{discount} % off for {membership} membership on total amount: ${billAmount}")
    else:
        print("No discount on amount less than $25")
        return billAmount, discount_amount        

def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    print(f"The total amount is {billAmount}")
    #print(f"The discounted amount is $ {billAmount}")
    billAmount = getDiscount(billAmount, membership)
    #print(f"The discounted amount is $ {}")
                                                                    
def main():
    #while True:
        #details = input("Press A to add product and Q to quit: ").capitalize()
        #if details == "A":
    buyingData = enterProducts()
        #elif details == "Q":
            #break
    membership = input("Enter customer membership: ").capitalize()
    makeBill(buyingData, membership)
    print(buyingData)

main()