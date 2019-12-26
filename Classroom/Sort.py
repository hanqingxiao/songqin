'''
请定,义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。
1.定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数
def mySort(alist):alist [int,int .....]
2. 创建一个新的列表newList
3. 先找出所有元素中最小的，append在newList里面
if 2<9 取2
4. 再找出剩余的所有元素中最小的，append在newList里面
5. 依次类推，直到所有的元素都放到newList里面
'''
aList=[6,9,8,2,7]
newList=[]

# [6,2] [8] [9,7]
# [6, 2]  -  [9, 7]

# [2, 6]
middleValue = 6;
# [2, 6]

# [9, 7]
# [7] [9]
#快速排序
def mySort(list):
    if (len(list) <= 1):
        return list;

    list1 = [];
    list2 = [];
    middle = int(len(list) / 2);
    middleValue = list[middle];
    list.remove(middleValue);
    for i in range (0, len(list)):
        if (list[i] <= middleValue):
            list1.append(list[i])
        else:
            list2.append(list[i])

    return mySort(list1) + [middleValue] + mySort(list2)
# def mySort(list):
#     while len(list)>0:
#         min =list[0]
#         for i in range(0,len(list)):
#             if(list[i]<=min):
#                 min =list[i]
#         newList.append(min)
#         list.remove(min)
#     return newList
print(mySort(aList))



#     for i in range(0,len(list)-1):
#         if list[j]<list[j+1]:
#             min
#         list.remove(min)
#         newList[-1].append(min)
#     return newList
#



