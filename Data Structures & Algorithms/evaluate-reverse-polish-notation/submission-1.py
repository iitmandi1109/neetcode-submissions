class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i in ('+','-','*','/'):
                b=int(s[-1])
                s.pop()
                a=int(s[-1])
                s.pop()
                if i=='+':
                    c=a+b
                if i=="-":
                    c=a-b
                if i=='*':
                    c=a*b
                if i=="/":
                    c=a/b
                s.append(c)
            else:
                s.append(i)

        return int(s[-1])