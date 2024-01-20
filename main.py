from language.lexer import Lexer
from language.parser import Parser
import os

if __name__=="__main__":
    while True:
        do = input("> ")
        
        if do == "exit":
            os.system("clear")
            break

        lexer = Lexer(do)
        tokens = lexer.tokenize()
        print(tokens)
        parser = Parser(tokens)
        tree = parser.branch()
        print("tree:",tree)
