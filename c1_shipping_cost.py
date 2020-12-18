# this doesn't work


def shipping_cost(weight):
        if weight <=0:
             print("Your package was not weighed properly")
        elif weight <= 15:
                print("Shipping is Free")
        elif weight > 15 and weight <= 50:
                print("Shipping cost is: $10")
        else:
                print("Shipping cost is: $25")
        return

while True :
    weight = input("Enter package weight when done enter done: ")
    if weight == "done" :
        print("Thanks for using the Shipping calculator")
        break
    shipping_cost(float(weight))


