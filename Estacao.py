class Estacao:
    def __init__(self, nome, num, passageiros, trem):
        self._nome = nome
        self._num = num
        self._passageiros = passageiros
        self._trem = trem

    def get_num(self):
        return self._num
    
    def set_num(self, num):
        self._num = num
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome
    
    def get_trem(self):
        return self._trem
    
    def set_trem(self, trem):
        self._trem = trem

    def chegada(self, passageiro):
        self._passageiros.append(passageiro)

    def chegadas(self, passageiros):
        self._passageiros.extend(passageiros)

    def saida(self, passageiro):
        self._passageiros.remove(passageiro)

    def saidas(self, passageiros):
        for passag in passageiros:
            self._passageiros.remove(passag)
    
    def up_trem(self, passageiro, trem):
        if self._trem:
            trem.pick(passageiro)
            self._passageiros.remove(passageiro)
    
    def ups_trem(self, passageiros, trem):
        if self._trem:
            trem.picks(passageiros)
            for passag in self._passageiros:
                self._passageiros.remove(passag)

    def down_trem(self, passageiro, trem):
        if self._trem:
            self._passageiros.append(passageiro)
            trem.drop(passageiro)

    def downs_trem(self, passageiros, trem):
        self._passageiros.extend(passageiros)
        trem.drops(passageiros)
    
    def to_string(self):
        print('\n ## Estação: ' + str(self._num) + ' - ' + self._nome)
        print('Trem: ' + str(self._trem))
        print('Lista de passageiros')
        for passag in self._passageiros:
            passag.to_string()