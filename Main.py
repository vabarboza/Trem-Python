from typing import Text
from Passageiro import Passageiro
from Trem import Trem
from Estacao import Estacao
from Log import Log

def print_estado(trem, estacoes):
    trem.to_string()

    for estacao in estacoes:
        estacao.to_string()


if __name__ == '__main__':
    trem = Trem([], 10)

    log = Log()
    
    passageiro1 = Passageiro("Clara", 34)
    passageiro2 = Passageiro("Fabio", 130)
    passageiro3 = Passageiro("Yuri", 110)
    passageiro4 = Passageiro("Lucas", 130)
    passageiro5 = Passageiro("Vinicius", 110)

    estacao_a = Estacao('Oxford', 1, [], True )
    estacao_b = Estacao('Londres', 2, [], False)
    estacao_c = Estacao('Manchester', 3, [], False)

    estacao_a.chegadas([passageiro1,passageiro2,passageiro3])
    estacao_b.chegada(passageiro4)
    estacao_c.chegada([passageiro5])

    estacoes = []
    estacoes.extend([estacao_a, estacao_b, estacao_c])

    estacao_a.ups_trem([passageiro1, passageiro2, passageiro3], trem)
    estacao_a.set_trem(False)
    log.write_log("Passageiros subiram no trem")
    trem.to_string()

    print('')

    estacao_b.set_trem(True)
    estacao_b.downs_trem([passageiro3, passageiro1], trem)
    estacao_b.ups_trem([passageiro4], trem)
    estacao_b.set_trem(False)
    trem.to_string()

    print('')

    estacao_c.set_trem(True)
    estacao_c.down_trem(passageiro4, trem)
    estacao_c.ups_trem([passageiro5], trem)
    trem.to_string()
    
    print('')

    ##print_estado(trem, estacoes)