class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule= ['type','color','name']
        return len([x for x in items if x[rule.index(ruleKey)]==ruleValue])
