class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices=[bank[x].count('1') for x in range(len(bank)) if bank[x].count('1')!=0]
        lasers=0
        for n in range(len(devices)-1):
            if n!=len(devices)-1:
                lasers+=(devices[n]*devices[n+1])
        return lasers
