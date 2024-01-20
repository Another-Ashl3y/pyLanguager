class Node:
    def __init__(self, op, left = None, right = None) -> None:
        self.op = op
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        if self.left and self.right:
            return f"({self.left} {self.op} {self.right})"
        elif self.left:
            return f"({self.left} {self.op})"
        elif self.right:
            return f"({self.op} {self.right})"
        else:
            return f"{self.op}"

    def swap_right(self):
        right_copy = CopyNode(self.right.left, self.right.op, self.right.right)
        new_left = CopyNode(self.left, self.op, self.right.left)
        self.left = new_left
        self.op = right_copy.op
        self.right = right_copy.right
        


class CopyNode:
    def __init__(self, l, t, r) -> None:
        self.left = l
        self.op = t
        self.right = r
    
    def __repr__(self) -> str:
        if self.left and self.right:
            return f"({self.left} {self.op} {self.right})"
        elif self.left:
            return f"({self.left} {self.op})"
        elif self.right:
            return f"({self.op} {self.right})"
        else:
            return f"{self.op}"