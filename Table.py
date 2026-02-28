# Multiplication Table program 

# ! Multiplication Table function
def multiplication_table(number):

    # loop from 1 to 10:
    for i in range(1, 11):

        # print table line
        print(f"{number} x {i} = {number * i}")

        # Askuser for a number
number = int(input("Enter a number : "))
multiplication_table(number)