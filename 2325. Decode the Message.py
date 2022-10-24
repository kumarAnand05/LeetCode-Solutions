class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        unique_key= []
        alpha= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for x in key:
            if x not in unique_key and x!=' ': unique_key.append(x)
        out=''
        for n in message:
            if n!=' ':out+= alpha[unique_key.index(n)]
            else: out+=' '
        return out
