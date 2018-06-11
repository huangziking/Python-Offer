'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
查找方式从最大值开始查找即右上角开始
如果输入整数大于当前元素，则向下移一位
如果输入整数小于当前元素，则向左移一位
'''

class Solution:
    def FindTarget(self,target,array):
        if array==[]:
            print("数组为空.")
            return False

        rawnum=len(array)
        colnum=len(array[0])

        i=colnum-1
        j=0
        count=0
        while i>=0 and j<rawnum:
            if array[j][i]>target:
                i-=1
            elif array[j][i]<target:
                j+=1
            else:
                return j,i
        return False
'''
测试数据
'''
array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]

array2 = []

array3 = [[62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],[63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],[64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],[66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],[67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]]

FindTarget = Solution()
print("target位置为:",FindTarget.FindTarget(10,array))
print("target位置为:",FindTarget.FindTarget(30,array2))
print("target位置为:",FindTarget.FindTarget(60,array3))