import math
import time
NUMBER = 600851475143
start_time = time.time()

def Check(num):
    for i in range(2, num, 1):
        if num % i == 0:
            return False
    return True


def Decide_prost(Number):
    prost_number = []
    number = math.sqrt(NUMBER).__int__()
    for i in range(13, number, 1):
        if Number % i != 0:
            continue
        if Check(i):
            prost_number.append(i)
    print(prost_number[-1])




Decide_prost(NUMBER)
print(time.time() - start_time)