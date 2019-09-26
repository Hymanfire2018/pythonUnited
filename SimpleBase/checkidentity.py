# 用户身份验证

username = input('Input Username: ')
password = input('Input Password: ')
# 如果希望输入Password时 终端中没有回显 可以使用getpass模块的getpass函数
# import getpass
# password = getpass.getpass('Input Password: ')
if username == 'admin' and password == '123456':
    print('Success!')
else:
    print('Fault!')
