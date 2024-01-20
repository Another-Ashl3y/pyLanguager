from language.TokenLib import *

TK_INT = TokenKey("INTEGER")
TK_FLOAT = TokenKey("FLOAT")
TK_IDENTIFIER = TokenKey("IDENTIFIER")

TK_ADD = TokenKey("PLUS","+")
TK_SUB = TokenKey("MINUS","-")
TK_MUL = TokenKey("MUL","*")
TK_DIV = TokenKey("DIV","/")
TK_SET = TokenKey("SET","=")

TK_L_PARENTH = TokenKey("L_PARENTH","(")
TK_R_PARENTH = TokenKey("R_PARENTH",")")


OPERATOR_TOKENS = (TK_ADD.type, TK_SUB.type, TK_MUL.type, TK_DIV.type, TK_SET.type)

VALID_VAR_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
NUMBERS = "0123456789."
OPERATORS = "+-/*"
