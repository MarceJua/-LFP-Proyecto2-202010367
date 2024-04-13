class Token:
    def __init__(self, Token, Lexema, fila , columna) -> None:
        self.Token = Token
        self.Lexema = Lexema
        self.fila= fila
        self.columna = columna
        self.siguiente = None
