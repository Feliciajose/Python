# function to check if a number is an Armstrong number
def is_armstrong_number(num):
    # find the number of digits in the given number
    order = len(str(num))
    
    # initialize sum variable to 0
    sum = 0
    
    # find the sum of each digit raised to the power of number of digits
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    
    # return True if the sum is equal to the given number, else False
    return num == sum

# main program to find Armstrong numbers in a given range
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

print("Armstrong numbers in the given range are:")
for num in range(lower, upper+1):
    if is_armstrong_number(num):
        print(num)
