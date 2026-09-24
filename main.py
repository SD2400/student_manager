from utils.my_fun import add,find,delete,update,analyze,statistics
from utils.menu import menu
from utils.storage import load_data,save_data
print("欢迎进入学生管理系统")
student = load_data()
while True:      #while循环
    menu()  # 输出菜单
    try:
        a = int(input("请输入您要使用的功能:"))
    except ValueError:
        print("输入的数值有问题,请重新输入!!!")
        continue
    if a == 1:    #添加
        if add(student):
            save_data(student)
    elif a == 2:   #查询
        find(student)
    elif a == 3 :    #删除
        if delete(student):
            save_data(student)
    elif a == 4 :    #修改
        if update(student):
            save_data(student)
    elif a == 5:    #成绩分析
        analyze(student)
    elif a == 6:    #成绩统计
        statistics(student)
    elif a == 0:    #退出
        print("bye~")
        break           #退出循环
    else:
        print("您的操作不符合规范,请重新输入~")
