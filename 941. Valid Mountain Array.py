class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak=max(arr)
        if arr.count(peak)>1: return False
        else:
            pos=arr.index(peak)
            if pos==0 or pos==(len(arr)-1): return False
            else:
                left= arr[:pos]
                right= arr[pos+1:]
                cl=sorted(left)
                cr=sorted(right,reverse=True)
                return (left==cl and right==cr and len(set(cl))==len(left) and len(set(cr))==len(right))
