class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        if len(s) % 2 == 1:
            return False
        for b in s:
            bracketSet = set([")","}","]"])
            if b in bracketSet:
                openBracket = self.bracketChecker(b)
                if not valid:
                    return False
                elif valid[-1] != openBracket:
                    return False
                else:
                    valid.pop(-1)
                    
            else:
                valid.append(b)
        if valid:
            return False
        else:
            return True

    def bracketChecker(self,bracketType):
        opening = ""
        if bracketType == ")":
            opening = "("
        elif bracketType == "}":
            opening = "{"       
        elif bracketType == "]":
            opening = "["
        return opening
