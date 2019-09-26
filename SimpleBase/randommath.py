# 掷骰子决定做什么事情

from random import randint
face = randint(1, 6)        #使用random模块的randint函数生成指定范围的随机数来模拟掷骰子
if face == 1:
    result = 'Sing'
elif face == 2:
    result = 'Dance'
elif face == 3:
    result = 'Paint'
elif face == 4:
    result = 'Socccer'
elif face == 5:
    result = 'Tennis'
else:
    result = 'Cold Joke'
print(result)
