from commanders.jeanpipe.troops.baseTroop import BaseTroop 
class Tower(BaseTroop):
    # Clase Tower

    def __init__(self, pos):
        super().__init__()
        self.type = 'tower'
        self.pos = pos

    def moverse(self):
        pass

    def atacar(self):
        pass