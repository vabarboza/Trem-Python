class Log:
    def write_log(self, texto):
        arquivo = open('log.txt', 'a')
        arquivo.write(texto + '\n')
        arquivo.close()
        