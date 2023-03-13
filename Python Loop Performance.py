## Import the time module
import time

## Create a function that calculates the sum of all numbers from 1 to n using For Loop
def for_loop_function(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

## Create a function that calculates the sum of all numbers from 1 to n using While Loop
def while_loop_function(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

## Call the functions using different values of n (10, 100, 1,000, 10,000, 100,000)
call_values = [10, 100, 1000, 10000, 100000]

for n in call_values:
    time_start = time.time()
    for_loop_total = for_loop_function(n)
    time_end = time.time()
    print(f"\nFor Loop: {for_loop_total}")
    print(f"    Execution Time: {time_end - time_start:.10f}s")

    time_start = time.time()
    while_loop_total = while_loop_function(n)
    time_end = time.time()
    print(f"While Loop: {while_loop_total}")
    print(f"    Execution Time: {time_end - time_start:.10f}s")
