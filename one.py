import tkinter as tk
import tkinter.messagebox  # 弹窗库
import pickle  # 用于python特有的类型和python的数据类型间进行转换
import random

# 窗口
window = tk.Tk()
window.title('湖人总冠军系统')
window.geometry('450x300')

# 标签 用户名密码
tk.Label(window, text='用户名:').place(x=100, y=150)  # place位置
tk.Label(window, text='密码:').place(x=100, y=190)
# 用户名输入框
var_usr_name = tk.StringVar()
# textvariable的需要StringVar类型的值
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
# 密码输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


# 登录函数
def usr_log_in():
    # 输入框获取用户名密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            # 必填参数file必须以二进制可读模式打开，即“rb”，其他都为可选参数
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:  # 捕获错误
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            # 必填参数file表示obj要写入的文件对象，file必须以二进制可写模式打开，即“wb”
            pickle.dump(usrs_info, usr_file)
    # 判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            # showinfo提示信息弹窗
            # tk.messagebox.showinfo(title='welcome',
            # message='登录成功，欢迎您：'+usr_name)
            # 新建注册界面
            # toplevel顶级窗口
            window_message = tk.Toplevel(window)
            window_message.geometry('350x200')
            window_message.title('登录成功')

            # 查看信息
            def see_message():
                try:
                    with open('usr_message.pickle', 'rb') as usr_file:
                        exist_usr_message = pickle.load(usr_file)
                        tk.messagebox.showinfo('姓名', exist_usr_message['用户姓名'])
                        tk.messagebox.showinfo('学号', exist_usr_message['学号'])
                        tk.messagebox.showinfo('年龄', exist_usr_message['年龄'])
                        tk.messagebox.showinfo('专业', exist_usr_message['专业'])
                except FileNotFoundError:
                    exist_usr_message = {}
                    is_write = tk.messagebox.askyesno('提示', '您还没有录入信息，是否现在录入')
                    if is_write:
                        write_message()

            # 录入信息
            def write_message():
                # 确定写入
                def true_change():
                    name1 = new_name.get()
                    id1 = new_id.get()
                    major1 = new_major.get()
                    age1 = new_age.get()

                    exist_usr_message[用户姓名] = name1
                    exist_usr_message[学号] = id1
                    exist_usr_message[专业] = major1
                    exist_usr_message[年龄] = age1
                    with open('usr_message.pickle', 'wb') as usr_file:
                        pickle.dump(exist_usr_message, usr_file)
                        window_mess.destroy()

                window_mess = tk.Toplevel(window_message)
                window_mess.geometry('350x200')
                window_mess.title('用户信息')

                new_name = tk.StringVar()
                tk.Label(window_mess, text='用户姓名：').place(x=10, y=10)
                tk.Entry(window_mess, textvariable=new_name).place(x=150, y=10)

                new_id = tk.StringVar()
                tk.Label(window_mess, text='学号：').place(x=10, y=50)
                tk.Entry(window_mess, textvariable=new_id).place(x=150, y=50)

                new_major = tk.StringVar()
                tk.Label(window_mess, text='专业：').place(x=10, y=90)
                tk.Entry(window_mess, textvariable=new_major).place(x=150, y=90)

                new_age = tk.StringVar()
                tk.Label(window_mess, text='年龄：').place(x=10, y=130)
                tk.Entry(window_mess, textvariable=new_age).place(x=150, y=130)
                # 确认录入按钮及位置
                # command点击按钮后执行的函数
                bt_confirm_mess = tk.Button(window_mess, text='确认录入', command=true_cdhange)

                bt_confirm_mess.place(x=150, y=170)

            # 修改信息
            def change_message():

                window_mess = tk.Toplevel(window_message)
                window_mess.geometry('350x200')
                window_mess.title('用户信息')

                new_name = tk.StringVar()
                tk.Label(window_mess, text='用户姓名：').place(x=10, y=10)
                tk.Entry(window_mess, textvariable=new_name).place(x=150, y=10)

                new_id = tk.StringVar()
                tk.Label(window_mess, text='学号：').place(x=10, y=50)
                tk.Entry(window_mess, textvariable=new_id).place(x=150, y=50)

                new_major = tk.StringVar()
                tk.Label(window_mess, text='专业：').place(x=10, y=90)
                tk.Entry(window_mess, textvariable=new_major).place(x=150, y=90)

                new_age = tk.StringVar()
                tk.Label(window_mess, text='年龄：').place(x=10, y=130)
                tk.Entry(window_mess, textvariable=new_age).place(x=150, y=130)

                # 确认修改按钮及位置
                # command点击按钮后执行的函数
                bt_confirm_mess = tk.Button(window_mess, text='确认修改')
                bt_confirm_mess.place(x=150, y=170)
                exist_usr_message['用户姓名'] = new_name
                exist_usr_message['学号'] = new_id
                exist_usr_message['专业'] = new_major
                exist_usr_message['年龄'] = new_age
                with open('usr_message.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_message, usr_file)
                    window_mess.destroy()

            bt_message1 = tk.Button(window_message, text='查看信息', command=see_message)
            bt_message1.place(x=80, y=130)
            bt_message2 = tk.Button(window_message, text='修改信息', command=change_message)
            bt_message2.place(x=160, y=130)

        else:
            # showerror错误信息弹窗
            tk.messagebox.showerror(message='密码错误')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名或密码为空')
    # 不在数据库中弹出是否注册的框
    else:
        # 对话框，是/否，返回值true/false
        is_signup = tk.messagebox.askyesno('提示', '您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()


# 注册函数
def usr_sign_up():
    # 确认注册时的相应函数
    def signtowcg1():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误', '用户名已存在')
        elif np == '' or nn == '':
            tk.messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            tk.messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('欢迎', '注册成功')
            # 注册成功关闭注册框
            window_sign_up.destroy()

    # 新建注册界面
    # toplevel顶级窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    # 用户名变量及标签、输入框
    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认注册按钮及位置
    # command点击按钮后执行的函数
    bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',
                                   command=signtowcg1)
    bt_confirm_sign_up.place(x=150, y=130)


# 修改密码
def usr_change():
    # 确认修改密码时的相应函数
    def signtowcg2():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

            # 检查用户名存在、密码为空、旧密码是否正确
        if nn not in exist_usr_info:
            tk.messagebox.showerror('错误', '用户名不存在')
        elif np == '' or nn == '':
            tk.messagebox.showerror('错误', '用户名或旧密码为空')
        elif exist_usr_info[nn] != np:
            tk.messagebox.showerror('错误', '旧密码不正确')
        # 信息没有问题则将新密码写入数据库
        else:
            exist_usr_info[nn] = npf
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('欢迎', '修改成功')
            # 修改成功关闭修改框
            window_change.destroy()

    # 修改密码界面
    # toplevel顶级窗口
    window_change = tk.Toplevel(window)
    window_change.geometry('350x200')
    window_change.title('修改密码')
    # 用户名变量及标签、输入框
    new_name = tk.StringVar()
    tk.Label(window_change, text='用户名：').place(x=10, y=10)
    tk.Entry(window_change, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = tk.StringVar()
    tk.Label(window_change, text='请输入旧密码：').place(x=10, y=50)
    tk.Entry(window_change, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_change, text='请输入新密码：').place(x=10, y=90)
    tk.Entry(window_change, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认修改按钮及位置
    # command点击按钮后执行的函数
    bt_confirm_change = tk.Button(window_change, text='确认修改',
                                  command=signtowcg2)
    bt_confirm_change.place(x=150, y=130)


# 退出的函数
def usr_sign_quit():
    window.destroy()


class RandomBall():
    '''
    定义运动的球的类
    '''

    def __init__(self, canvas, scrnwidth, scrnheight):
        '''
        canvas: 画布，所有的内容都应该在画布上呈现出来，此处通过此变量传入
        scrnwidth/scrnheigh:屏幕宽高
        '''
        self.canvas = canvas
        # 定义屏幕的大小
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight

        # 球出现的初始位置要随机，此处位置表示的球的圆心
        # xpos表示位置的x坐标
        self.xpos = random.randint(100, int(self.scrnwidth) - 100)
        self.ypos = random.randint(100, int(self.scrnheight) - 100)

        # 定义球运动的速度
        # 模拟运动：不断的擦掉原来画，然后在一个新的地方再从新绘制
        # 此处xvelocity模拟x轴方向运动
        self.xvelocity = random.randint(4, 20)
        self.yvelocity = random.randint(4, 20)

        # 球的大小随机
        # 此处球的大小用半径表示
        self.radius = random.randint(20, 100)

        # 定义颜色
        # RGB表示法：三个数字，每个数字的值是0-255之间，表示红绿蓝三个颜色的大小
        # 在某些系统中，之间用英文单词表示也可以，比如red, green
        # 此处用lambda表达式
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

    def create_ball(self):
        '''
        用构造函数定义的变量值，在canvas上画一个球
        '''
        # tkinter没有画圆形函数
        # 只有一个画椭圆函数，画椭圆需要定义两个坐标，
        # 在一个长方形内画椭圆，我们只需要定义长方形左上角和右下角就好
        # 求两个坐标的方法是，已知圆心的坐标，则圆心坐标减去半径能求出
        # 左上角坐标，加上半径能求出右下角坐标
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        # 再有两个对角坐标的前提下，可以进行画圆
        # fill表示填充颜色
        # outline是外围边框颜色
        self.item = self.canvas.create_oval(x1, y1, x2, y2, \
                                            fill=self.color, \
                                            outline=self.color)

    def move_ball(self):
        # 移动球的时候，需要控制球的方向
        # 每次移动后，球都有一个新的坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        # 以下判断是会否撞墙
        # 撞了南墙就要回头
        # 注意撞墙的算法判断
        if self.xpos + self.radius >= self.scrnwidth:
            # 装到了右边墙
            self.xvelocity = -self.xvelocity
            # 或者以下代码
            # self.xvelocity *= -1
        if self.ypos + self.radius >= self.scrnheight:
            # 装到了下边墙
            self.yvelocity = -self.yvelocity
        if self.xpos - self.radius <= 0:
            # 装到了左边墙
            self.xvelocity = -self.xvelocity
        if self.ypos - self.radius <= 0:
            # 装到了上边墙
            self.yvelocity = -self.yvelocity

        # 在画布上挪动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver():
    '''
    定义屏保的类
    可以被启动
    '''
    # 如何装随机产生的球？
    balls = list()

    def __init__(self):
        # 每次启动球的数量随机
        self.num_balls = random.randint(6, 20)

        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)

        # 任何鼠标移动都需要取消
        self.root.bind('<Motion>', self.myquit)
        # 同理，按动任何键盘都需要退出屏保
        self.root.bind('<Key>', self.myquit2)
        # 得到屏幕大小规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        # 创建画布，包括画布的归属，规格
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        # 在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, w, h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        # after是200毫秒后启动一个函数，需要启动的函数是第二个参数
        self.canvas.after(200, self.run_screen_saver)

    def myquit(self, e):
        # 此处只是利用了事件处理机制
        # 实际上并不关心事件的类型
        # B = tkinter.Button(self.root,text='确地退出',command=self.root.destory)
        # B.pack()
        self.root.destroy()

    def myquit2(self, e):
        self.root.destroy()


bt_login = tk.Button(window, text='登录', command=usr_log_in)
bt_login.place(x=100, y=230)
bt_logup = tk.Button(window, text='注册', command=usr_sign_up)
bt_logup.place(x=160, y=230)
bt_change = tk.Button(window, text='修改密码', command=usr_change)
bt_change.place(x=220, y=230)
bt_protect = tk.Button(window, text='启动屏保', command=ScreenSaver)
bt_protect.place(x=300, y=230)
bt_logquit = tk.Button(window, text='退出', command=usr_sign_quit)
bt_logquit.place(x=380, y=230)
# 主循环
# 进入消息循环
window.mainloop()
