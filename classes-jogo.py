class Heroi :
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    

    def atacar(self):
        if self.tipo == 'Mago':
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "fez um ataque misterioso" 

        print(f"O {self.tipo} atacou usando {ataque}.")
    
heroi1 = Heroi("Arthur", 30, input("Insira a classe do heroi: "))
#heroi2 = Heroi("Merlin", 150, input("Insira a classe do heroi: "))
#heroi3 = Heroi("Bruce", 25, input("Insira a classe do heroi: "))
#heroi4 = Heroi("Ryu", 20, input("Insira a classe do heroi: "))

heroi1.atacar()  
#heroi2.atacar() 
#heroi3.atacar()
#heroi4.atacar() 





