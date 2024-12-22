print("hello we will print the table of multipl")
def multiplication_table(number):
    for i in range(1, 11):
        print(str(number) + " x " + str(i) + " = " + str(number * i))
number = int(input("Enter a number x: "))
multiplication_table(number)
