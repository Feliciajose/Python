def sum_of_odds(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i
    return sum

n = int(input("Enter the value of n: "))
sum = sum_of_odds(n)
print("The sum of the first", n, "odd numbers is", sum)
