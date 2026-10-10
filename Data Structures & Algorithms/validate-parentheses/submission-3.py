class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        valid=True
        res=[]
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
              if not stack:
                valid=False
                break
              if stack[-1]!=pairs[ch]:
                valid=False
                break
        
              stack.pop()
        if stack :
            valid=False
        return valid

