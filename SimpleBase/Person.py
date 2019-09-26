class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 必须要先getter方法，然后再setter方法，否则会有编译错误

    @property  # 访问器：getter方法
    def age(self):
        return self._age

    @property  # 访问器：getter方法
    def name(self):
        return self._name

    @age.setter  # 修改器：setter方法
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋...' % self._name)
        else:
            print('%s正在玩斗地主...' % self._name)


def main():
    person = Person('zjy', 12)
    person.play()

    """
    为了重新为person._age赋值，系统根据此语句将自动调用相应的set方法，重新为_age赋值。
    这里使用的是_age，实际上，使用person.age也ok，
    但其他age的变形就不行了，也就是说，可以是_age或age，
    看下一知识点就可以知道如何进行名称使用的限制了
    """
    person._age = 22

    """
    你以为下面也是为变量重新赋值的语句，但其实：TypeError: 'int' object is not callable.
    所以，这是一种错误的重新为成员变量赋值的方法，与Java不太相同的地方。
    Java要写出调用的set方法为变量赋值，
    而这里的重新赋值应该写成上面那样，系统明白(@age.setter)你是想重新为变量赋值。
    """
    #	person.age(22)

    person.play()

    """
    下面的语句：AttributeError: can't set attribute. 
    因为没有提供name的set方法(@name.setter)，所以不能修改此属性。
    """
    #	person.name = 'zyy'

    """
    如何通过所谓的get方法调用属性值？这里有必要说一下：
    你以为：print('姓名：%c' % person.name())
    但实际：print('姓名：%c' % person.name)
    又与Java不同，这里不把他们当做方法来使用，而是直接当作成员变量！
    然后会自动调用相应的get方法~
    """
    print('姓名：%s' % person.name)


if __name__ == '__main__':
    main()
