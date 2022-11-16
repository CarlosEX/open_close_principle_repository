class MysqlDB:

    def __init__(self) -> None:
        self.__conexao = 'Mysql'

    def conectar(self) -> str:
        print('Conectando ao banco de Mysql...')

    def desconectar(self) -> str:
        print('Desconectando ao banco de Mysql...')