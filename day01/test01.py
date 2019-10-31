# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        res = 1
        n = int(input())
        while n != 0:
            if n%number != 0:
                tep = n%number
                res *= tep
                n = n - tep
                number = number - 1
            else:
                tmp = n/number
                res *= tmp
                n = n - tmp
                number = number - 1
        return res

s = Solution()
res = s.cutRope(2)
print(res)