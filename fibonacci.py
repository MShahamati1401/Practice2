x = int(input("Please Inter Number of Fibonacci"))
fibo = [1, 1]
for i in range(2, x):
    fibo.append(fibo[-1]+fibo[-2])
print(fibo)