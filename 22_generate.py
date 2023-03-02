class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 1: return ["()"]

        lists = ["(",")"]
        lists = lists * n

        def gen(s:str):
            r = []
            if s.count("(") > s.count(")"):
                if s.count("(") <n:
                    r.append(s+"(")
                if s.count(")") <n:
                    r.append(s+")")
            elif s.count("(") < n:
                    r.append(s+"(")
            return r        
        
        s = "("
        lists.remove("(")
        r = gen(s)
        for j in range(2*(n-1)):
            m = []
            for i in range(len(r)):
                b = gen(r[i])
                m = m+b
            r = m
        return r