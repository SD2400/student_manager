import json
print("欢迎进入学生管理系统")
menu = """
######学生管理系统#######
#       1.添加        #
#       2.查询        #
#       3.删除        #
#       4.修改        #
#       5.统计        #
#       0.退出        #
#######################
"""
print(menu)      #输出菜单
try:
    with open("student.json","r",encoding="utf-8") as f:
        student = json.load(f)
except:
    # 建立一个空字典,student = {"id":{"id":"001", "name":"张三","age":20,"score":90 ,"major":"数学与应用数学"},{},...}
    student = {}
def save_data():
    """

    :return:
    """
    with open("student.json","w",encoding="utf-8") as f:
        json.dump(student,f,ensure_ascii=False,indent=4)
while True:      #while循环
    a = int(input("请输入您要使用的功能:"))

    if a == 1:  #添加
        student_id = input("请输入学生的id:")
        if student_id in student:
            print("该学生已存在,请重新输入")
            continue #退出当前循环,开始下一次循环
        student_name = input("请输入学生的姓名:")
        student_age = int(input("请输入学生的年龄:"))
        student_grades = int(input("请输入学生的成绩:"))
        student_major = input("请输入学生的专业:")
        student[student_id] = {"id":student_id,"name":student_name,"age":student_age,"grades":student_grades,"major":student_major}
        save_data()
        print("该学生已成功添加!")
    elif a == 2:   #查询
        student_id = input("请输入您要查询的学生id:")
        if student_id not in student:
            print("该学生不存在,请重新输入")
            continue
        print(student[student_id])


    elif a == 3:    #删除
        student_id = input("请输入您要删除的学生id:")
        if student_id not in student:
            print("该学生不存在,请重新输入")
            continue
        del student[student_id]
        save_data()


    elif a == 4:    #修改
        student_id = input("请输入您要修改的学生id:")
        if student_id not in student:
            print("该学生不存在,请重新输入")
            continue
        student_name = input("请输入要最终的姓名:")
        student_age = input("请输入最终的年龄:")
        student_grades = input("请输入最终的成绩:")
        student_major = input("请输入最终的专业:")
        student[student_id]={"id":student_id,"name":student_name,"age":student_age,"grades":student_grades,"major":student_major}
        save_data()

    elif a == 5:    #统计
            abc=[]                  #定义一个空列表
            pass_grades = 0         # 初始及格人数
            for i in student.values():    #for循环,对字典student中的值进行遍历
                abc.append(i["grades"])  #将grades中的值添加进abc空列表中
                if i["grades"] >= 60:  #if条件判断
                    pass_grades += 1
            max_grades = max(abc)  #求最大值
            min_grades = min(abc)  #求最小值
            avg_grades = sum(abc)/len(abc)  #求平均值
            print(f"分数最高为:{max_grades},分数最低为:{min_grades},平均分为:{avg_grades},及格人数为:{pass_grades}")




    elif a == 0:    #退出
        print("bye~")
        break           #退出循环


    else:
     print("您的操作不符合规范,请重新输入~")

