def add_func(student):#添加功能
    s_id = input("请输入要添加的学生学号:")
    if s_id not in student:  # 判断输入的学号是否已存在于系统中
        s_name = input("请输入该学生的姓名:")
        try:
            s_age = int(input("请输入该学生的年龄:"))
        except ValueError:  # 尝试捕获ValueError异常
            print("输入的年龄有问题(非整型),请重新输入")
            return False
        if s_age > 0:  # 判断年龄是否大于0
            try:
                s_grade = int(input("请输入该学生的成绩:"))
            except ValueError:  # 尝试捕获ValueError异常
                print("输入的学生成绩有问题(非整型),请重新输入")
                return False
            if 0 <= s_grade <= 100:  # 判断成绩是否属于0-100
                s_major = input("请输入该学生的专业:")
                # 往空字典student里添加学生信息
                student[s_id] = {"ID": s_id, "name": s_name, "age": s_age, "grade": s_grade, "major": s_major}
                print("该学生已成功添加")
                return True
            else:
                print("输入的成绩不符合规范(0-100),请重新输入")
                return False
        else:
            print("输入的年龄应大于0")
            return False
    else:
        print("该学生已存在,请重新输入")
        return False
def del_func(student):#删除功能
    if not student: #判断student里是否有信息
        print("暂无学生,请添加")
        return False
    s_id = input("请输入要删除的学生学号:")
    if s_id in student: #判断输入的学生学号是否存在于student里
        del student[s_id]
        print("该学生已删除")
        return True
    else:
        print("没有找到该学生,请重新输入")
        return False
def update_func(student):#修改功能
    if not student:#判断student里是否有信息
        print("暂无学生信息,请添加")
        return False
    s_id = input("请输入要修改的学生id:")
    if s_id in student:#判断输入的学生id是否存在
        s_name = input("请输入修改后该学生的姓名:")
        try:
            s_age = int(input("请输入修改后该学生的年龄:"))
        except ValueError:  # 尝试捕获ValueError异常
            print("输入的年龄有问题(非整型),请重新输入")
            return False
        if s_age > 0:  # 判断年龄是否大于0
            try:
                s_grade = int(input("请输入修改后该学生的成绩:"))
            except ValueError:  # 尝试捕获ValueError异常
                print("输入的学生成绩有问题(非整型),请重新输入")
                return False
            if 0 <= s_grade <= 100:  # 判断成绩是否属于0-100
                s_major = input("请输入修改后该学生的专业:")
                # 往空字典student里添加学生信息
                student[s_id] = {"ID": s_id, "name": s_name, "age": s_age, "grade": s_grade, "major": s_major}
                print("该学生已成功修改")
                return True
            else:
                print("输入的成绩不符合规范(0-100),请重新输入")
                return False
        else:
            print("输入的年龄应大于0")
            return False
    else:
        print("暂未找到该学生,请重新输入")
        return False
def find_func(student):#查询功能
    if not student:#判断是否存在学生信息
        print("暂无学生信息,请添加")
        return False
    b = input("请输入要查询的方式:1.按学生姓名查询 2.按成绩范围查询: ")
    match b:
        case "1":  # 按学生姓名查询
            find_by_name(student)
        case "2":  # 按成绩范围查询
            find_by_grade(student)
        case _:
            print("请按规范输入")
            return False
def find_by_name(student):
    result = [] #创建空列表
    i_name = input("请输入要查询的学生姓名:")
    for i in student.values(): #对student里的值进行遍历
        if i["name"] == i_name:
            result.append(i) #添加进result列表里
    if not result: #判断是否存在条件符合的学生
        print("没有找到此学生")
    else:
        for i in result:
            print(i)
    return False

def find_by_grade(student):
    result = [] #创建空列表
    try:
        upper_grade = int(input("请输入成绩上限:"))
        lower_grade = int(input("请输入成绩下限:"))
    except ValueError: #尝试捕获ValueError异常
        print("输入的成绩有问题,请重新输入")
        return False
    if 0 <= upper_grade <= 100 and 0 <= lower_grade <= 100:
        if upper_grade >= lower_grade: #成绩上限应大于等于成绩下限
            for i in student.values(): #对字典student的值进行遍历
                if upper_grade >= i["grade"] >= lower_grade:
                    result.append(i) #将符合条件的值添加进result列表中
            if not result: #判断是否存在符合条件的值
                print("没有学生的成绩符合条件")
            else:
                for i in result:
                    print(i)
            return False
        else:
            print("成绩上限应大于等于成绩下限")
            return False
    else:
        print("成绩范围应为(0-100)")
        return False
def analyse_func(student):#分析功能
    if not student: #判断student字典中是否为空
        print("暂无学生信息,请添加")
        return False
    grades = []#创建空列表
    num = 0 #对num进行赋值
    for i in student.values(): #对字典的值进行遍历
        if i["grade"] >= 60: #合格
            num += 1
        grades.append(i["grade"]) #将合格成绩添加进grades列表中
    highest = max(grades) #最高分
    lowest = min(grades) #最低分
    avg = round(sum(grades) / len(grades),1)  #平均分,保留1位小数
    pass_rate = round(num / len(grades)*100,1) #,及格率保留1位小数
    print(f"最高分为:{highest},最低分为:{lowest},平均分为:{avg},及格人数为{num},及格率为{pass_rate}%")
    return False
def statics_func(student):#统计功能
    if not student:#判断student字典中是否为空
        print("暂无学生信息,请添加")
        return False
    result = sorted(student.values(), key=lambda x: (-x["grade"], x["name"]), reverse=False)
    for i in result:
        print(i)


