from repository import Repositorio
from databases import PostgresDB, MysqlDB

db_conn_postgres = PostgresDB()
db_conn_mysql = MysqlDB()

repo = Repositorio()

repo.insert(db_conn_postgres)   
repo.insert(db_conn_mysql)

repo.select(db_conn_postgres)
repo.select(db_conn_mysql)