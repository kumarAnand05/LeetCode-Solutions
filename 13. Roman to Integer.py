class Solution:
    def romanToInt(self, s: str) -> int:
        cm= s.find('CM')
        cd= s.find('CD')
        xc= s.find('XC')
        xl= s.find('XL')
        ix= s.find('IX')
        iv= s.find('IV')
        m= s.find('M')
        d= s.find('D')
        c= s.find('C')
        l= s.find('L')
        x= s.find('X')
        v= s.find('V')
        
        score=0

        if cm!=-1:
            s = s.replace("CM", "900 ")
        if cd!=-1:
            s = s.replace("CD", "400 ")
        if xc!=-1:
            s = s.replace("XC", "90 ")
        if xl!=-1:
            s = s.replace("XL", "40 ")
        if ix!=-1:
            s = s.replace("IX", "9 ")
        if iv!=-1:
            s = s.replace('IV', "4 ")
        s=s.replace('M', '1000 ')
        s=s.replace('D', '500 ')
        s=s.replace('C', '100 ')
        s=s.replace('L', '50 ')
        s=s.replace('X', '10 ')
        s=s.replace('V', '5 ')
        t= s.split()
        for n in t:
            if 'I' not in n:
                score+= int(n)
            else:
                score+= len(n)
        return score
    
