class Trem:
    def __init__(self, passageiros, max_pas):
        self._passageiros = passageiros
        self._max_pas = max_pas

    def pick(self, passageiro):
        if self._max_pas > len(self._passageiros):
            self._passageiros.append(passageiro)
    
    def picks(self, passageiros):
        if self._max_pas > len(self._passageiros) + len(passageiros):
            self._passageiros.extend(passageiros)

    def drop(self, passageiro):
        self._passageiros.remove(passageiro)
    
    def drops(self, passageiros):
        for passag in passageiros:
            self._passageiros.remove(passag)

    def get_qtde_passageiros(self):
        return len(self._passageiros)

    def get_max_pas(self):
        return self._max_pas
    
    def to_string(self):
        print("## Trem ## Nº de Passageiros: " + str(len(self._passageiros)))
        print("Nº max: " + str(self._max_pas))
        print("Lista de passageiros")
        for passag in self._passageiros:
            passag.to_string()
