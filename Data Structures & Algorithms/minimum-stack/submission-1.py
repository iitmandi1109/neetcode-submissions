class MinStack:
    def __init__(self):
        self.s=[]
        self.a=float("INF")
    def push(self, val: int) -> None:
        self.a=min(self.a,val)
        self.s.append(val)
    def pop(self) -> None:
        val = self.s.pop()
        if val == self.a:
            self.a = min(self.s) if self.s else float("inf")
    def top(self) -> int:
        return self.s[-1]
    def getMin(self) -> int:
        return self.a
