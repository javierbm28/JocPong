class ObjetoEscenario:
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color

    def Pinta(self, superficie):
        pass  # Esto se sobrescribirá en las subclases