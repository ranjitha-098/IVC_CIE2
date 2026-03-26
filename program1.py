n = int(input("Enter number: ")) 
temp = n 
s = 0 
digits = len(str(n)) 
while temp > 0:
    d = temp % 10
    s += d ** digits
    temp //= 10 

if s == n:
    print("Armstrong")  
else: 
    print("Not Armstrong")
