class Solution:
    def countOrders(self, n: int) -> int:
        return (eval('*'.join(map(str, list(range(1,(2*n)+1))))))//(2**n)%(1000000000+7)
