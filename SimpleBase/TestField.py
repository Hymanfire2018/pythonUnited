class Test:

    def __init__(self, foo):
        self.__foo = foo  # 左侧的__foo是类中的属性，foo只是参数罢了

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')  # 自动调用__init__方法，使‘Test’赋值给self，‘hello’赋值给foo

    # (私有方法)AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()

    # (私有属性)AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)


if __name__ == "__main__":
    main()
