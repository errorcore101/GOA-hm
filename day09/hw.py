age = int(input("input age:"))

if age < 18:
    input("not old enough to get this car")
elif age > 18:
    input("get car at checkout")



temp = int(input("input temp (celcius):"))

if temp < 15:
    input("cold")
elif temp > 28:
    input("hot")



item = int(input("input item amount:"))

if item < 4:
    input("not enough")
elif item == 5:
    input("perfect amount, bought")
elif item > 6:
    input("too much")



itemprice = 20
yourmoney = int(input("input your money (you must pay 20$):"))

if yourmoney < itemprice:
    input("not enough money")
elif yourmoney > itemprice:
    input("thank you for the purchase")



num = int(input("enter number:"))

if num % 2:
    input("even")
else:
    input("odd")