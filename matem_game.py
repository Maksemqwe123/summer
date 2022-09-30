"""Матем-игра"""
import random
import time

start_time = time.time()

a = random.randint(1, 963)
b = random.randint(1, 752)
c = a + b
print(f'{a} + {b} = ?')

summa = int(input('Введите пожалуйста ответ:\n'))

if summa == c:
    print("правильно!!!")
else:
    print('Неправильно(')

print(f'Прошло {(time.time() - start_time) // 1} секунды')
