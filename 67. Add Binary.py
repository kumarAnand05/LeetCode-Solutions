class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        out = ''
        if len(a)>len(b): b= '0'*(len(a)-len(b))+b
        elif len(a)<len(b): a= '0'*(len(b)-len(a))+a
        a= a[::-1]
        b= b[::-1]

        for n in range(len(a)):
            res= (int(a[n])+int(b[n])+carry)
            out+= str(res%2)
            carry=res//2
        if carry == 1:
            out+=str(carry)

        return out[::-1]
