'''
1-读取file.txt
    fo=open(filedir )
2-获取每一行的信息
    fo.readlines()-----list
    去掉换行符
    fo.read().spitlines()
3-去掉空格，前后中间都会有
space.replace(' ','')
4-计算税后工资*0.9和扣税金额

5-将姓名、税前工资、扣税金额、税后工资存入新的文件file2.TXT；且需要取整数
'''
fileDir='./file1.txt'
fo=open(fileDir)
EmpSal=[]
folines=fo.read().splitlines()
for space in folines:
    EmpSal.append(space.replace(' ',''))
for sem in EmpSal:
    name=sem.split(';')[0]
    salary=sem.split(';')[1]
    pre_tax=int(salary.split(':')[-1])
    income=int(pre_tax*0.9)
    tax=int(pre_tax-income)
    fd = open("file2.txt", 'a+')
    fd.write(f'{name:10};{salary:12};tax:{tax:5};income:{income:5}\n')
fd.close()
fo.close()
