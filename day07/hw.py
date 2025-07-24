num1 = int(input("input number: "))
num2 = int(input("input number: "))

print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. **")
print("6. //")
print("7. %")

act = (input("input action: "))

if act == "+":
    input(num1 + num2)
elif act == "-":
    input(num1 - num2)
elif act == "*":
    input(num1 * num2)
elif act == "/":
    input(num1 / num2)
elif act == "**":
    input(num1 ** num2)
elif act == "//":
    input(num1 // num2)
elif act == "%":
    input(num1 % num2)
else:
    input("ERROR: invalid action")



num = 10

if num % 2:
    input("ლუწი")
else:
    input("კენტი")



if 90 < 95 < 100:
    input("საოცარი!!!")
elif 80 < 84.5 < 89:
    input("მაგარია!!")
elif 70 < 74.5 < 79:
    input("არაუშავს")
elif 60 < 64.5 < 69:
    input("ცუდი")
elif 0 < 29.5 < 59:
    input("ძალიან ცუდი")



if 18 < 20:
    input("ზილი")
elif 21 < 100:
    input("იკარუს")



if 25 < 100:
    input("ჩაიცვი მოკლე ტანცაცმელი")
elif 0 < 10:
    input("ჩაიცვი გრაძელი ტანსაცმელი")