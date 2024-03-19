def calculate_hcf(x, y):
    """
    This function calculates the HCF of two numbers.
    """
    if x > y:
        smaller = y
    else:
        smaller = x
    hcf = 1
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The HCF of", num1, "and", num2, "is", calculate_hcf(num1, num2))