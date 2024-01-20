from typing import Any
from language.keywords import *
class Node:
    def __init__(self, op, left = None, right = None) -> None:
        self.op = op
        self.left = left
        self.right = right
        self.simplify()
    
    def __repr__(self) -> str:
        # print(f"L: {self.left}, C: {self.op}, R: {self.right}")
        if self.left and self.right:
            return f"({self.left} {self.op} {self.right})"
        elif self.left:
            return f"({self.left} {self.op})"
        elif self.right:
            return f"({self.op} {self.right})"
        else:
            return f"{self.op}"

    def swap_right(self):
        self.simplify()
        right_copy = CopyNode(self.right.left, self.right.op, self.right.right)
        new_left = CopyNode(self.left, self.op, self.right.left)
        self.left = new_left
        self.op = right_copy.op
        self.right = right_copy.right
    
    def simplify(self):
        if type(self.left) == Token and type(self.op) == Token:
            # print("Simplifying")
            if self.left.type in (TK_ADD.type, TK_SUB.type):
                if self.left.type == self.op.type:
                    self.op = Token(TK_ADD.type)
                if self.left.type != self.op.type:
                    self.op = Token(TK_SUB.type)
                self.left = None


        if type(self.left) == type(self):
            self.left.simplify()
        if type(self.right) == type(self):
            self.right.simplify()
        return self


class CopyNode(Node):
    def __init__(self, l, t, r) -> None:
        self.left = l
        self.op = t
        self.right = r
        self.simplify()

