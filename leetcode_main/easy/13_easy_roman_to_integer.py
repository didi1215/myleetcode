class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ls = s #ls = list(s) 也可以转成列表，但是字符串也可以直接索引
        for index in range(len(ls)):
            if index < len(ls)-1 and dict[ls[index]] < dict[ls[index+1]]: # 注意这里的逻辑
                num = num - dict[ls[index]] 
            else:
                num = num + dict[ls[index]]
        return num
