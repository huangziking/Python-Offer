'''
请实现一个函数，将一个字符串的空格替换成“%20”
例如，当字符串为We Are Happy 替换后的字符串将变为
We%20Are%20Happy
'''
'''
replaceSpace()字符串拼接
replaceSpace2()python方法
'''
class Solution:
    def replaceSpace(self,strreplac):
        if  not isinstance(strreplac,str) or strreplac==None:
            return False
        tmpstr = ''
        for s in strreplac:
            if s ==" ":
                tmpstr += '%20'
            else:
                tmpstr += s
        return tmpstr
    def replaceSpace2(self,strreplac):
        if not isinstance(strreplac,str) or strreplac==None:
            return False
        return strreplac.replace(' ','%20')
s = 'We Are Happy'
s1 = 2
test = Solution()

print(test.replaceSpace(s))
print(test.replaceSpace2(s))
print(test.replaceSpace(s1))
print(test.replaceSpace2(s1))