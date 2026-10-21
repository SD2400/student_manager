from utils.menu import menu_func
from utils.my_fun import *
from utils.storage import save_data,load_data
print("欢迎使用学生管理系统")
#定义菜单
student = load_data()
while True:
    menu_func() #输出菜单
    a = input("请输入您要使用的功能(1-7):")
    match a:  #使用match...case
        case "1":#添加
            if add_func(student):
                save_data(student)
        case "2":#删除
            if del_func(student):
                save_data(student)
        case "3":#修改
            if update_func(student):
                save_data(student)
        case "4":#查询
            find_func(student)
        case "5":#分析,最高分,最低分,平均分,及格率,及格人数
            analyse_func(student)
        case "6":#统计,按照成绩降序,姓名升序输出学生信息
            statics_func(student)
        case "7":#退出
            print("bye~")
            break
        case _:
            print("请按规范(1~7)输入~")





