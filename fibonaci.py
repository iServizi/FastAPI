n = int(input("Liczba ciagu fib - "))
n_0=0
n_1=1
for i in range(n):
     output = n_0 + n_1
     n_0=n_1
     n_1=output
     #print(output)
print(output)
        
        
