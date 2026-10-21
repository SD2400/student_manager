import json
def save_data(student):#保存数据,将python字典转化为json文件
    with open ("student.json","w",encoding="utf-8")as f:
        json.dump(student,f,ensure_ascii=False,indent=4)

def load_data():#读取数据,将json文件转为python字典
    try:
        with open("student.json","r",encoding="utf-8")as f:
            return json.load(f)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        return {}
