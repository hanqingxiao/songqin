'''
1.程序开始的时候提示用户输入学生年龄信息 格式如下：
Jack Green ,   21  ;  Mike Mos, 9;
我们假设 用户输入 上面的信息，必定会遵守下面的规则：
  学生信息之间用分号隔开（分号前后可能有不定数量的空格），(需要去空格)
  每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格）（(需要去空格)）
2. 程序随后将输入的学生信息分行显x示，格式如下
Jack Green :   21;
Mike Mos   :   09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
'''
str=input("请输入学生年龄信息：")
stuinfo = str.split(';')
for comma in stuinfo:
    if ','in comma:
        name=comma.split(',')[0]
        age=comma.split(',')[1]
        name=name.strip()
        age= age.strip()
        if age.isdigit():
            age=int(age)
            print(f'{name:<20}:{age:0>2};')
        else:
            continue