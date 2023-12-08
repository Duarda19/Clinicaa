class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura
    def set_base(self, base):
        if self.__base >= 0:
            self.__base = base
        else:
            raise ValueError("Valor inválido")
    def set_altura(self, altura):
        if self.__altura >= 0:
            self.__altura = altura
        else:
            raise ValueError("Valor inválido")
    
    def __str__(self):
        return f"Base = {self.__base}, altura = {self.__altura}"

    