import time
import matplotlib.pyplot as plt

def F_recursive(n):
    if n <= 2:
        return 1
    else:
        return F_recursive(n-1) + F_recursive(n-2)

def F_dynamic(n):
    fib = [0] * (n+1)
    fib[1] = 1
    fib[2] = 1
    for i in range(3, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

def measure_execution_time(function, n):
    start_time = time.time()
    k = function(n)
    end_time = time.time()
    return end_time - start_time, k

n_values = list(range(10, 101, 10))
recursive_times = []
dynamic_times = []

max_recursive_time = 10000.0  # Maximum execution time for recursive method (adjust as needed)

for n in n_values:
    dynamic_time, k_dynamic = measure_execution_time(F_dynamic, n)
    dynamic_times.append(dynamic_time)
    if n >= 50:
        recursive_time = max_recursive_time
    else:
        recursive_time, k_rec = measure_execution_time(F_recursive, n)
        
    recursive_times.append(recursive_time)
    if recursive_time == max_recursive_time:
        print('max time')
    else:
        print('recursive time:', recursive_time)
    print('dynamic time:', dynamic_time)
    print('Fib value:', k_dynamic)

plt.plot(n_values, recursive_times, label='Recursive')
plt.plot(n_values, dynamic_times, label='Dynamic Programming')
plt.xlabel('Value of n')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of F(n) for Different Methods')
plt.legend()
plt.show()
