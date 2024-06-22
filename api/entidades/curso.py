class Curso():
    def __init__(self, nome, descricao, dataPubli):
        self.__nome = nome
        self.__descricao = descricao
        self.__dataPubli = dataPubli
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
        
    @property
    def dataPubli(self):
        return self.__dataPubli
    
    @dataPubli.setter
    def dataPubli(self, dataPubli):
        self.__dataPubli = dataPubli