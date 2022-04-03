# -*- codeing = utf-8 -*-
# @Time : 2022/4/3 14:49
# @Author : 张思惠
# @File : multiplication.py
# @Software : PyCharm

# i=1
#
# for i in range(1,10):
#     j = 1
#     for j in range(j,i+1):
#         print("%d*%d=%d\t"%(i,j,i*j),end="")
#     print("\n")
i=1
while i<10:
    j=1
    while j<i+1:
        print("%d*%d=%d\t" % (i, j, i * j), end="")
        j+=1
    print("\n")
    i+=1