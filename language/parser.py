from language.Nodes import *
from language.keywords import *

ORDER = [
    TK_SET.type,
    TK_ADD.type,
    TK_SUB.type,
    TK_MUL.type,
    TK_DIV.type,
    TK_L_PARENTH
]

class Parser:
    def __init__(self, tokens: list) -> None:
        self.tokens = tokens
        # self.tokens.reverse()
        self.pos = -1
        self.current_token = None

    def branch(self, left = None, indent=1):
        self.advance()
        token = self.current_token
        if token:
            right = self.branch(token)
            # print(f"NODES: L:{left}, C:{token}, R:{right}")
            if token.type in OPERATOR_TOKENS:
                token = Node(token, left, right)
            
                

            if type(right) == Node:
                if type(token) == Node:
                    # print(f"OPERATORS: (T:{token.op}|INDEX:{ORDER.index(token.op.type)}, R:{right.op}|INDEX:{ORDER.index(right.op.type)})")
                    if ORDER.index(token.op.type) > ORDER.index(right.op.type):
                        token.swap_right()
                    return token.simplify()
                return right.simplify()
        return token

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None
        return self.current_token


# x = 1 + 2
# (IDENT, x) (SET) (INT, 1) (ADD) (INT, 2)
# LOOK X (left)
# LOOK SET (IS OPERATOR)
# X
# SET(X, 1)
# SET(X, ADD(1, 2))
