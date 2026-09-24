def add(student):
    student_id = input("请输入学生的id:")
    if student_id in student:
        print("该学生已存在,请重新输入")
        return False
    student_name = input("请输入学生的姓名:")
    try:
        student_age = int(input("请输入学生的年龄:"))
    except ValueError:
        print("输入的数值(非整型)有问题")
        return False
    if student_age >= 0:
        try:
            student_grades = int(input("请输入学生的成绩:"))
        except ValueError:
            print("您输入的成绩有问题(非整型),请重新输入")
            return False
        if 0 <= student_grades <= 100:  # 对学生的成绩划分范围
            student_major = input("请输入学生的专业:")
        else:
            print("您输入的成绩不符合规范[0-100],请重新输入")
            return False
    else:
        print("您输入的年龄有问题(非正数),请重新输入")
        return False
    student[student_id] = {"id": student_id, "name": student_name, "age": student_age, "grades": student_grades,
                           "major": student_major}
    print("该学生已成功添加!")
    return True




def find(student):
    if not student:
        print("暂无学生,请添加")
        return False
    else:
        student_id = input("请输入您要查询的学生id:")
        if student_id not in student:
            print("该学生不存在,请重新输入")
            return False
        print(student[student_id])
        return False


def delete(student):
    if not student:
        print("暂无学生,请添加")
        return False
    else:
        student_id = input("请输入您要删除的学生id:")
        if student_id not in student:
            print("该学生不存在,请重新输入")
            return False
        del student[student_id]
        print("该学生已删除")
        return True




def update(student):
    if not student:
        print("暂无学生,请添加")
        return False
    else:
        student_id = input("请输入您要修改的学生id:")
        if student_id not in student:
            print("该学生不存在,请重新输入")
            return False
        student_name = input("请输入最终的姓名:")
        try:
            student_age = int(input("请输入最终的年龄:"))
        except ValueError:
            print("输入的年龄有问题(非整型),请重新输入")
            return False
        if student_age < 0:
            print("您输入的年龄有问题(非正数),请重新输入")
            return False
        try:
            student_grades = int(input("请输入最终的成绩:"))
        except ValueError:
            print("输入的成绩有问题(非整型),请重新输入")
            return False
        if not (0 <= student_grades <= 100):
            print("您输入的成绩不符合规范[0-100],请重新输入")
            return False
        student_major = input("请输入最终的专业:")
        student[student_id] = {"id": student_id, "name": student_name,
                               "age": student_age, "grades": student_grades,
                               "major": student_major}
        print("该学生已修改!")
        return True


def analyze(student):
    if not student:
        print("暂无学生,请添加")
        return False
    else:
        abc = []  # 定义一个空列表
        pass_grades = 0  # 初始及格人数
        for i in student.values():  # for循环,对字典student中的值进行遍历
            abc.append(i["grades"])  # 将grades中的值添加进abc空列表中
            if i["grades"] >= 60:  # if条件判断
                pass_grades += 1
        max_grades = max(abc)  # 求最大值
        min_grades = min(abc)  # 求最小值
        avg_grades = sum(abc) / len(abc)  # 求平均值
        print(f"分数最高为:{max_grades},分数最低为:{min_grades},平均分为:{avg_grades},及格人数为:{pass_grades}")
        return False



def statistics(student):
    if not student:
        print("暂无学生,请添加")
        return False
    else:
        for i in student.values():
            print(i)
        return False
