from collections import deque
class MyStack:
    q=deque()
    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        self.q.reverse()
        x=self.q.popleft()
        self.q.reverse()
        return x
        

    def top(self) -> int:
        self.q.reverse()
        x = self.q[0]
        self.q.reverse()
        return x  

    def empty(self) -> bool:
        if len(self.q)==0:
            return True
        else :
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()