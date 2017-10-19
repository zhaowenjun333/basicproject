"""定义一个函数， 功能：
findstr(targetstr, substr)
在targetstr里面查找 substr出现的次数
"""




def findsubstr(targetstr, substr):
    count =0
    i = len(substr)
    while True:
        ind=targetstr.find(substr)     #xiabiao
        if ind ==-1 :
            break
        count+=1
        # print(ind)
        targetstr=targetstr[ind+i:]
        # print(targetstr)
    return  count
str1="aaabbaaaa"
str2="bba"
num = findsubstr(str1,str2)
print(num)