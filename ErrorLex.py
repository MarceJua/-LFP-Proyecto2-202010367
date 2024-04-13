class Error:
    def __init__(self, tipo, linea, columna, token, descripcion):
        self.tipo= tipo
        self.linea = linea
        self.columna = columna
        self.token = token
        self.descripcion = descripcion