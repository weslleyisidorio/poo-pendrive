class Pendrive:
    
    def __init__(self, id, capacidade):
        self.__id = id
        self.__capacidadeMax = capacidade
        self.__capacidade = capacidade
        self.__arquivos = []
        
    
    @property
    def id(self):
        return self.__id
    
    @property
    def capacidadeMaxima(self):
        return self.__capacidadeMax
    
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, valor):
        if 0 < valor <= self.__capacidadeMax:
            self.__capacidade = valor
        else:
            print('Operação inválida!')

    @property
    def arquivos(self):
        return self.__arquivos
    @arquivos.setter
    def arquivos(self, novoArquivo):
        self.__arquivos.append(novoArquivo)
    
    def formatar(self):
        self.__arquivos = []
        self.capacidade = self.capacidadeMaxima
        print('pendrive formatado com sucesso!')
        print(f'Espaço livre: {self.capacidade} MB')
    
    def mesmoNome(self, nome):
        for file in self.__arquivos:
            if file.nome == nome:
                return True
        return False
    
    def adicionar(self, arquivo):
        if self.__capacidade >= arquivo.tamanho and not (self.mesmoNome(arquivo.nome)): 
            self.__arquivos.append(arquivo)
            self.__capacidade -= arquivo.tamanho
            return True
        return False


    def adicionar_arquivo(self, arquivo):
        if self.adicionar(arquivo):
            print('Arquivo adicionado com sucesso!')
            print(f'Espaço disponivel no pendrive: {self.__capacidade} MB')
        else:
            print('Espaço insuficiente!')

    def apagar(self, nomeArquivo):
        for arquivo in self.__arquivos:
            if arquivo.nome == nomeArquivo:
                self.__capacidade += arquivo.tamanho
                self.__arquivos.remove(arquivo)
                return True
            return False

    def apagar_arquivo(self, arquivo):
        if self.apagar(arquivo):
            print('Arquivo excluido com sucesso!')
            print(f'Espaço disponivel no pendrive: {self.__capacidade} MB')
        else:
            print('Arquivo inexistente!')
    
    def copiar(self, nomeArquivo, penDestino):
        for file in self.__arquivos:
            if file.nome == nomeArquivo:
                return penDestino.adicionar(file)
            else:
                print('Arquivo não encontrado.')
                return False

    def copiar_arquivo(self, nomeArquivo, penDestino):
        if self.copiar(nomeArquivo, penDestino):
            print('Arquivo copiado com sucesso!')
            print(f'Espaço disponível no pendrive destino: {penDestino.__capacidade} MB')
        else:
            print('Arquivo inexistente!')

    def mover_arquivo(self, arquivo, penDestino):
        if self.copiar(arquivo, penDestino) and self.apagar(arquivo):
            print('Arquivo copiado com sucesso!')
            print(f'Espaço disponível no pendrive destino: {penDestino.__capacida} MB')
        else:
            print('Erro! Já existe um arquivo com este nome!')
    
    def imprimeArquivos(self):
        lista = ''
        for file in self.__arquivos:
            lista += file.__str__()
            lista += '\n'
        return lista
        
    def __str__(self):
        cabecalho = '------Pendrive {self.id}------\n'
        espacoTotal = f'Espaço total: {self.capacidadeMaxima} MB\n'
        espacoLivre = f'Espaço livre: {self.capacidade} MB\n'
        espacoUsado = f'Espaço usado: {self.capacidadeMaxima - self.capacidade} MB\n'
        arquivos = '------Arquivos------\n'
        return f'{cabecalho}{espacoTotal}{espacoLivre}{espacoUsado}{arquivos}{self.imprimeArquivos()}'

class Arquivo:
    def __init__(self, nome, tipo, tamanho):
        self.__nome = nome
        self.__tipo = tipo
        self.__tamanho = tamanho

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, novoTipo):
        self.__tipo = novoTipo

    @property
    def tamanho(self):
        return self.__tamanho
    
    def __str__(self):
        return f"{self.nome}.....................{self.tamanho} MB"
    
def main():

    pendrive1 = Pendrive(1,1024)
    pendrive2 = Pendrive(2,512)
    pendrive1.adicionar_arquivo(Arquivo("teste1.txt","txt",10))
    # Arquivo adicionado com sucesso!
    #Espaço disponivel no pendrive: 1014 MB
    titanic = Arquivo("titanic.mp4","video",1048)
    pendrive1.adicionar_arquivo(titanic)
    # Espaço insuficiente!
    forro_das_antigas = Arquivo("forro.mp3","mp3",300)
    pendrive2.adicionar_arquivo(forro_das_antigas)
    # Arquivo adicionado com sucesso!
    #espaço disponivel no pendrive: 212 MB
    pendrive2.copiar_arquivo("forro.mp3",pendrive1)
    # Arquivo copiado com sucesso!
    # Espaço disponível no pendrive destino: 714 MB

    pendrive1.apagar_arquivo("teste1.docx")
    # Arquivo inexistente!

    pendrive1.apagar_arquivo("teste1.txt")
    # Arquivo excluido com sucesso!
    # Espaço disponivel no pendrive: 724 MB

    pendrive2.mover_arquivo("forro.mp3",pendrive1)
    # Erro! Já existe um arquivo com este nome!

    pendrive1.formatar()
    # pendrive formatado com sucesso!
    # Espaço livre: 1024 MB

    print(pendrive2)
    
        
if __name__ == '__main__':
    main()    