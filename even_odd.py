def even_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False

inital = int(input("Enter the intial range : "))
final =  int(input("Enter the final range : "))

for n in range (inital , final+1):
    print(n , even_odd(n))
    
