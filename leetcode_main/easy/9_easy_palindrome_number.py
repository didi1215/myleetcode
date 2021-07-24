class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = list(str(x))
        b = a[::-1]
        return a==b 
 # 巨大的坑就是python只能识别True和False是bool变量，如果if a==b: return true就会把true当作变量而报错
