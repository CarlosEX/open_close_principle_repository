class PostgresDB:

    def __init__(self) -> None:
        self.__conexao = 'Postgres'

    def conectar(self) -> str:
        print('Conectando ao banco de Postgress...')

    def desconectar(self) -> str:
        print('Desconectando ao banco de Postgress...')