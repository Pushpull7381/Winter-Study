def greet():
    print(1)
    print(2)
greet()

def greet2(name):
    print("반가워요!", name, "님!")
greet2("미네")

def adder1(num1, num2):
    print(num1,"+",num2,"=", num1+num2)
adder1(1,2)

def adder2(num1, num2):
    sum=num1+num2
    return sum
result=adder2(4,5)
print(result)
print(adder2(11,8))

def main():
    print("----------------")
    greet()
    greet2("미네")
    adder1(1,2)
    print(adder2(11,8))
main()