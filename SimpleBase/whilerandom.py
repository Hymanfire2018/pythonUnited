"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点Larger/小一点Smaller/猜对了
"""

import random
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('Input a guess number: '))
    if number < answer:
        print('Larger')
    elif number > answer:
        print('Smaller')
    else:
        print('Guess Right!')
        break
print('You guessed %d times.' % counter)
