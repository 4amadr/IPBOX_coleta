import psycopg2
from config_banco import config_data


#função para se conectar ao banco de dados
def conn_db():
    try:
        print("Iniciando ligação com o banco de dados...")
        conec = psycopg2.connect(**config_data)
        print('Conectado ao banco. Infos do banco:', conec)
        return conec
    except Exception as e:
        print(f"Ops, ocorreu um erro ao tentar se conectar ao banco de dados: ",e)
        return None
    finally:
        print("Tentativa de conexão finalizada!")

conn_db()
