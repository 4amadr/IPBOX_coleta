# Projeto de Automação de Coleta de Dados - IPBOX 📊

## 📌 Sobre o Projeto
Este projeto tem como objetivo **automatizar a coleta de dados do discador IPBOX**, utilizando sua **API**, para extrair informações de telefonia e melhorar a análise de dados posterior.  

Ele foi desenvolvido como parte de um projeto maior da **GSolutions**, e futuramente será integrado ao **Projeto JamesIA**, que busca reduzir tarefas manuais extensas e suscetíveis a erros através de automações robustas e funcionais.

---

## 🚀 Funcionalidades
- Coleta de dados de telefonia via API do IPBOX.  
- Tratamento de inconsistências em registros temporais e de contagem.  
- Integração com banco de dados PostgreSQL.  
- Estruturação e armazenamento de dados para análises futuras.  

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3  
- **Bibliotecas:**  
  - `requests` → para requisições à API  
  - `regex` → para tratamento de dados inconsistentes  
  - `psycopg2` → para integração com banco de dados PostgreSQL  

---

## 📚 Conhecimentos Aplicados
- Programação Orientada a Objetos (POO).  
- Estruturação de arquivos e organização do código.  
- Conexão e configuração de banco de dados.  
- Coleta, limpeza e tratamento de diferentes tipos de dados.  
- Lógica de programação para automações.  

---

## ⚠️ Desafios Enfrentados
Durante o desenvolvimento, foi identificado que os dados de pausa dos operadores vinham no formato:  


Onde `05` representava a quantidade de pausas de determinado operador.  
Esses dados apresentavam inconsistências e não podiam ser integrados diretamente ao banco de dados.  

🔧 **Solução:** Utilização da biblioteca **Regex** para tratar e remover as contagens, tornando os registros consistentes para inserção.  


## 🧑‍💻 Autor
Desenvolvido por **Victor Amador**  
📎 [LinkedIn](https://www.linkedin.com/in/victor--viegas)  

