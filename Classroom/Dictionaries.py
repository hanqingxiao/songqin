'''
1-定义路径名及文件路径
   fileName ='./0005_1.txt'
2-编写一个函数，其中参数fileName 为 数据库记录文件路径
 def putInfoToDict(fileName):
3文件每行的数据；每一行分为三个部分-签到时间、课程id、学生id
    fo=open(fileName)
    folines=fo.read().splitlines()
 4-输出结果是将数据库记录文件中的学生签到信息保存在一个字典对象中，并作为返回值返回。
 {
    131: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:09'},
        {'lessonid': 273,'checkintime':'2017-03-14 10:52:19'},
    ],
    126: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:19'},
    ],
}

setdefault(),如果键不存在于字典中，将会添加键并将值设为默认值。
dict.setdefault(key, default=None) ==retDict[userid] = [] ;retDict[userid].append(toAdd)


print()和pprint()都是python的打印模块，功能基本一样，唯一的区别就是pprint()模块
打印出来的数据结构更加完整，每行为一个数据结构，更加方便阅读打印输出结果。
'''
import pprint
fileDir ='./0005_1.txt'
dict={}
def putInfoToDict(fileName):
    fo=open(fileName)
    fileInfo=fo.read().splitlines()
    for one in fileInfo:
        #替换（、）、’
        list=one.replace('(', '').replace(')', '').replace("'",'').strip()
        checkintime=list.split(",")[0]
        lessonID = list.split(",")[1].strip()
        studentID=list.split(",")[2].strip()
        toAdd = {'lessonid': lessonID, 'checkintime': checkintime}
        dict.setdefault(studentID, []).append(toAdd)
    return dict
pprint.pprint(putInfoToDict(fileDir))