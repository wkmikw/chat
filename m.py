# -*- coding: utf-8 -*-

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x1=bin(x)
        x2=bin(y)
        L1=len(x1)
        L2=len(x2)
        if x>y:
        	p=L2
        else:
        	p=L1
        i=1
        cal=0
        while p>2:       	
        	if x1[L1-i]!=x2[L2-i]:
        		cal=cal+1
        	i=i+1
        	p=p-1
        return(cal)

a=Solution()
x=1;y=4
print(a.hammingDistance(x,y))


