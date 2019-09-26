# Step1、导入tkinter模块中我们需要的东西
import tkinter
import tkinter.messagebox

def main():
	flag = True

	# 定义按钮触发的事件：修改标签上的文字？？？？？?？？？？？？？
	def change_label_text():
		nonlocal flag
		flag = not flag
		color, msg = ('red', 'Hello, world!')\
			if flag else ('blue', 'Goodbye, world!')
		label.config(text=msg, fg=color)

	# 定义按钮触发的事件：确认退出？？？？？?？？？？？？？
	def confirm_to_quit():
		if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗？'):
			top.quit()	# 退出顶级会话窗口

	# Step2、创建一个顶层窗口对象并用它来承载整个GUI应用
	top = tkinter.Tk()
	# 2.1 设置顶层窗口的大小
	top.geometry('240x160') # 小写字母x
	# 2.2 设置窗口标题
	top.title('小游戏')
	# Step3、在顶层窗口对象上添加GUI组件
	# 3.1 创建标签对象并添加到顶层窗口
	label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
	label.pack(expand=1)
	# 3.2 创建按钮对象
	# 3.2.1 创建一个装按钮的容器
	panel = tkinter.Frame(top)
	# 3.2.2 创建按钮对象：指定添加到哪个容器中，通过command参数绑定事件回调函数
	button1 = tkinter.Button(panel, text='修改', command=change_label_text)
	button1.pack(side='left') # pack方法用来设置组件放置的位置
	button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
	button2.pack(side='right')
	panel.pack(side='bottom')
	# Step4、开启主事件循环
	tkinter.mainloop()


if __name__ == '__main__':
	main()
