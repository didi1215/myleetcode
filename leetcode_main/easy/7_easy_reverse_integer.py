class Solution:
    def reverse(self, x: int) -> int:
            s = list(str(x)) # 先转化为str再以列表形式存储
            if s[0] == '-':
                s1 = s[:0:-1] # -1：倒序，0：不要"-"
                r = "-"+"".join(s1) # .join()字符串后加字符串
            else:
                r = "".join(s[::-1])
            if -2**31 < int(r) < 2**31-1: # 注意输出是int
                return r
            else:
                return 0
