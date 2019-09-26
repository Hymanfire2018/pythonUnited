class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar() 		# 使私有的__bar()方法变成“公有”
    print(test._Test__foo)  # 使私有的__foo属性变成“公有”


if __name__ == "__main__":
    main()
