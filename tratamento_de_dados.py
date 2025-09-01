import re
from ScrapIPBOX_API import dados_ipbox
'''Módulo que contém as funções para tratar os dados antes de serem inseridos dentro do banco de dados'''
def limpar_intervalo(dados_ipbox):
    """
    O arquivo JSON faz a contagem do tempo das pausas e a quantidade das pausas entre parênteses.
    Esta função trata esses dados removendo a parte entre parênteses.
    """
    campos_temporais = ['Banheiro', 'Descanso', 'Discando', 'Feedback', 'Lanche', 'Login', 'Pos Atendimento']
    try:
        for registro in dados_ipbox:
            # Acessa as pausas dentro de cada registro
            if 'pausas' in registro and registro['pausas']:
                pausas_dict = registro['pausas'][0]

                for campo in campos_temporais:
                    if campo in pausas_dict:
                        valor_original = str(pausas_dict[campo])
                        #Trocando o regex(usado anteriormente) por split
                        valor_limpo = valor_original.split("(")[0].strip()
                        pausas_dict[campo] = valor_limpo
                        print(f"Limpando {campo}: '{valor_original}' -> '{valor_limpo}'")

        return dados_ipbox
    except Exception as e:
        print(f"Erro na limpeza: {e}")
        return dados_ipbox

    finally:
        print("Operação finalizada")





def tratar_traco(dados_ipbox):
  campos_para_serem_tratados = ['tempo_logado', 'tempo_atendimento', 'abandonadas_no_ramal', 'toque_sem_atendimento', 'tma', 'tmd',
                  'tempo_pausa_total', 'tempo_nao_produtivo', 'tempo_disponivel', 'geradas', 'geradas_atendidas',
                  'tempo_geradas', 'tempo_medio_atendidas_geradas', 'tempo_medio_disponivel_geradas']

  lista_de_pausas = ['Banheiro', 'Descanso', 'Discando', 'Feedback', 'Lanche', 'Login', 'Pos Atendimento']
  try:
    for registro in dados_ipbox:
      # Tratar campos principais
      for campo in campos_para_serem_tratados:
        if registro.get(campo) == "-":
          registro[campo] = '00:00:00'

      # Tratar pausas (está dentro de uma lista)
      if 'pausas' in registro and len(registro['pausas']) > 0:
        pausas_dict = registro['pausas'][0]  # Primeiro item da lista
        for pausa in lista_de_pausas:
          if pausas_dict.get(pausa) == "-":
            pausas_dict[pausa] = '00:00:00'

    print("Dados tratados com sucesso")
    return dados_ipbox
  except Exception as e:
    print(f"Erro no tratamento de dados!", e)
  finally:
    print("Operação de tratamento finalizada")

limpar_intervalo(dados_ipbox)
