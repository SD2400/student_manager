import json
def load_data():
    try:
        with open("student.json","r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # 建立一个空字典,student = {"id":{"id":"001", "name":"张三","age":20,"score":90 ,"major":"数学与应用数学"},{},...}
        return {}



def save_data(student):
    with open("student.json","w",encoding="utf-8") as f:
        json.dump(student,f,ensure_ascii=False,indent=4)