from language.keywords import *


class Lexer:
    def __init__(self, code) -> None:
        self.code = code
        self.pos = -1
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos += 1
        if self.pos < len(self.code):
            self.current_char = self.code[self.pos]
            return
        self.current_char = None
        
    def tokenize(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in OPERATORS:
                word = self.build_word(OPERATORS)
                if TK_ADD.contains(word):
                    tokens.append(Token(TK_ADD.type))
                elif TK_SUB.contains(word):
                    tokens.append(Token(TK_SUB.type))
                elif TK_MUL.contains(word):
                    tokens.append(Token(TK_MUL.type))
                elif TK_DIV.contains(word):
                    tokens.append(Token(TK_DIV.type))
            elif TK_SET.contains(self.current_char):
                tokens.append(Token(TK_SET.type))
            
            elif TK_L_PARENTH.contains(self.current_char):
                tokens.append(Token(TK_L_PARENTH.type))
            elif TK_R_PARENTH.contains(self.current_char):
                tokens.append(Token(TK_R_PARENTH.type))
            
            elif self.current_char in NUMBERS:
                word = self.build_word(NUMBERS)
                # print(word)
                if "." in word:
                    tokens.append(Token(TK_FLOAT.type, float(word)))
                else:
                    tokens.append(Token(TK_INT.type, int(word)))
            elif self.current_char in VALID_VAR_CHARS and not(self.current_char in NUMBERS):
                word = self.build_word(VALID_VAR_CHARS)
                # print(word)
                if False: pass
                else: # Make sure it is not a keyword
                    tokens.append(Token(TK_IDENTIFIER.type, word))
        

            self.advance()
        return tokens
    
    def build_word(self, valid_symbols):
        if self.current_char in valid_symbols:
            word = ""
            while self.current_char != None and self.current_char in valid_symbols:
                word += self.current_char
                self.advance()
            self.pos -= 1
            return word
        



