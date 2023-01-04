class Solution:
  def minimumRounds(self, tasks: List[int]) -> int:
    return -1 if 1 in collections.Counter(tasks).values() else sum((x + 2) // 3 for x in collections.Counter(tasks).values()) 
