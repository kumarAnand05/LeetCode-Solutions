class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        numbering=list(range(len(growTime)))
        numbering.sort(key=lambda plant: growTime[plant], reverse=True)
        pos=0
        tday=0
        for i in numbering:
            picked= plantTime[i]
            pos+=picked
            tday=max(tday,pos+growTime[i])
        return tday
