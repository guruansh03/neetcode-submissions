class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c= {}
        for i in nums:
            c[i] =  c.get(i,0) + 1
        print(c)
        m = 0
        e = 0
        for i in c:
            if c[i] > m:
                m = c[i]
                e = i
        return e