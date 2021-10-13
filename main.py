import time

def fibonacci(n): return _fib(n)[0]

def _fib(n):
	if n == 0: return (0,1)
	else:
		a, b = _fib(n//2)
		c = a*(b*2-a)
		d = a*a+b*b
		if n%2 == 0: return (c,d)
		else: return (d,c+d)

amount,start_time = int(input("Amount of cycles: ")), time.time()

open("fib.txt", "w").write(str(fibonacci(amount)))
print(f"{time.time() - start_time} seconds")