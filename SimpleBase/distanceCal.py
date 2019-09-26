from math import sqrt

class Point(object):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y


	def show(self):
		print('点在平面上的位置：x = %d, y = %d' % (self.x, self.y))


	def distance(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		return sqrt(dx ** 2 + dy ** 2)


	def move_to(self, x, y):
		"""移动到指定位置

		:param x: 新的横坐标
		"param y: 新的纵坐标
		"""
		self.x = x
		self.y = y


	def move_by(self, dx, dy):
		"""移动指定的增量

		:param dx: 横坐标的增量
		"param dy: 纵坐标的增量
		"""
		self.x += dx
		self.y += dy


def main():
	p1 = Point(3, 5)
	p2 = Point()

	p1.show()
	p2.show()

	p2.move_by(-1, 2)
	p2.show()

	print(p1.distance(p2))


if __name__ == '__main__':
	main()
