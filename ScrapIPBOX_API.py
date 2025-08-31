import requests


url = "https://contech1.ipboxcloud.com.br:8624/ipbox/api/getPA1"

payload='de=20250822000000&ate=20250822235959'
headers = {
  'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC92ZXJpeC5jb20uYnIiLCJhdWQiOiJodHRwOlwvXC9pcGJveC5jb20uYnIiLCJpYXQiOjE3MjU5OTE0NzMsIm5iZiI6MTcyNTk5MTQ3NSwiZGF0YSI6eyJ1c3VhcmlvX2lkIjoiMSIsInRva2VuX2lkIjoiSXp1ejhRdmxYYzh4eTlOQWdvWXoifX0.nAiowP1RQ6l2CG7pTpfWuF1cxyNYuZi6UY_aMOt6vSY',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload, )
dados = response.json()
if response.status_code == 200:
  try:
    dados_ipbox = response.json()["data"]
    print(dados_ipbox[:2])
    print("Dados coletados sem problemas")

  except Exception as e:
    print(f"Erro ao coletar dados, a requisição da sua API foi fuzilada", e)

  finally:
    print("Operação finalizada")
else:
    print(f"Error: Request failed with status code {response.status_code}")






