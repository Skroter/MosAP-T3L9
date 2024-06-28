from cgi import test
import random

N = 0
while N == 0:
    print('Введите число в диапазоне 1 - 100_000:')
    testN = int(input())
    if testN < 1:
        print('Введите число заново')
    elif testN > 100_000:
        print('Введите число заново')
    else:
        N = testN 
print(N)
# x = 2*10_000_000_000 
# arr = [random.randint(1, x) for i in range(N)] 
# many = set(arr) 
# print(len(many)) 