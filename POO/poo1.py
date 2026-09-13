class Candidato:
    def __init__(self, nome, tecnologia_principal, objetivo_empresa):
        self.nome = nome
        self.tecnologia_principal = tecnologia_principal
        self.objetivo_empresa = objetivo_empresa

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, estudo {self.tecnologia_principal} e meu obejtivo é trabalhar na empresa {self.objetivo_empresa}!"

pessoa = Candidato("Lucas", "Python", "V360")

#mensagem = pessoa.apresentar()
#print(mensagem)

print(pessoa.apresentar())