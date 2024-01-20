class Token:
    def __init__(self, type_, value=None) -> None:
        self.type = type_
        self.value = value
    def __repr__(self) -> str:
        if self.value != None:
            return f"{self.value}"
        return f"{self.type}"

class TokenKey:
    def __init__(self, type_, words=None) -> None:
        self.type = type_
        self.words=words
    def contains(self, word):
        if self.words:
            if type(self.words) == list:
                if word in self.words:
                    return True
            elif type(self.words) == str:
                if word == self.words:
                    return True
        return False

