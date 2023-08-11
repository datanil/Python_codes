# Write a function, primeNumberDetector, that tests if a number, n is a prime number.

# Function Name: primeNumberDetector
# Input: integer n
# Output: boolean: true if n is a prime number else false.
# Example: primeNumberDetector(13) => True
#------------------------------------------------------------------------------------------------#

#Creating a function name 'primeNumberDetector(n)'
def primeNumberDetector(n):

    if n <= 1:
        return False 
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i <= n**(1/2):
        if n % i == 0:
            return False
        i += 2
    return True

#Creating a list of numbers from user's defined range
l = []

initial = int(input("Enter your desired initial range : "))
final = int(input("Enter your desired final range : "))
for element in range(initial, final+1):
    l.append(element)


#iterating to list to detect prime numbers 
for n in l:
    print(n, primeNumberDetector(n))

