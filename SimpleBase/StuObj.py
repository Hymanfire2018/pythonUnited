class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
	def __init__(self, name, age):		# self参数是类中的每个方法的参数都必须有的，用于指示本对象，相当于Java中的this
		self.name = name
		self.age = age

	def study(self, course_name):
		print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
	def watch_movie(self):
		if self.age < 18:
			print('%s只能看《熊出没》.' % self.name)
		else:
			print('%s正在看喜欢的电影.' % self.name)


def main():
	stu1 = Student('zjy', 18)	        # 自动调用__init__方法，使‘Student’赋值给self，‘zjy’赋值给name，'18'赋值给age
	stu1.study('Python程序设计')
	stu1.watch_movie()


if __name__ == '__main__':
	main()
