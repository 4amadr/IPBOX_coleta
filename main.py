import inserir_banco

"""Executa a função que coleta ao banco de dados e coleta os dados do discador IPBOX"""
try:
    inserir_banco.inserir_banco()
    print("Banco de dados coletado com sucesso!")
except Exception as e:
    print("Erro ao executar a função", e)
finally:
    print("Execução total finalizada")