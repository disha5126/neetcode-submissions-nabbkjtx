class Solution:
    def myPow(self, x: float, n: int) -> float:
        f=1
        if n>0:
            while(n!=0):
                f=f*x
                n=n-1
        elif n<0:
            m=1
            while(n!=0):
                m=(m*x)
                n=n+1
            f=1/m
        else:
            pass
        
        return f

        