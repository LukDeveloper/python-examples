"""A Biblioteca Psycopg2
Esse pacote, faz a comunicação do Python com banco de dados PostgreSQL. Dessa forma é possível realizar operações no banco de dados via scripts Python. Estas funcionalidades facilitam e muito a manipulação de dados na linguagem Python e os bancos de dados PostgreSQL. A biblioteca pode ser instalada utilizando o comando abaixo:
                                        pip install psycopg2
"""
#Importando bibliotecas
import requests
import json
import pandas as pd
import psycopg2

# Requisição dos dados dos Deputados
url        = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
parametros = {}
resposta   = requests.request("GET", url, params=parametros)
objetos    = json.loads(resposta.text)
dados      = objetos['dados']

df = pd.DataFrame(dados)

for col in df.columns:
  df[col] = df[col].apply(str)

# Função para criar conexão no banco
def conecta_db():
  con = psycopg2.connect(host='localhost', 
                         database='db_deputados',
                         user='postgres', 
                         password='postgres')
  return con

# Função para criar tabela no banco
def criar_db(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()

# Dropando a tabela caso ela já exista
sql = 'DROP TABLE IF EXISTS public.deputados'
criar_db(sql)
# Criando a tabela dos deputados
sql = '''CREATE TABLE public.deputados 
      ( id            character varying(10), 
        uri           character varying(100), 
        nome          character varying(500), 
        siglaPartido  character varying(50), 
        uriPartido    character varying(200), 
        siglaUf       character varying(10), 
        idLegislatura character varying(10), 
        urlFoto       character varying(100), 
        email         character varying(100) 
      )'''
criar_db(sql)

# Função para inserir dados no banco
def inserir_db(sql):
    con = conecta_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

# Inserindo cada registro do DataFrame
for i in df.index:
    sql = """
    INSERT into public.deputados (id,uri,nome,siglaPartido,uriPartido,siglaUf,idLegislatura,urlFoto,email) 
    values('%s','%s','%s','%s','%s','%s','%s','%s','%s');
    """ % (df['id'][i], df['uri'][i], df['nome'][i], df['siglaPartido'][i], df['uriPartido'][i], df['siglaUf'][i], df['idLegislatura'][i], df['urlFoto'][i], df['email'][i])
    inserir_db(sql)
 
"""
Error: syntax error at or near "Angelo"
LINE 3: ...s.camara.leg.br/api/v2/deputados/141439','Chico D'Angelo','P...
"""

# Função para consultas no banco
def consultar_db(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  recset = cur.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
  con.close()
  return registros

# Realizando a consulta no PostegreSQL
reg = consulta_db('select * from public.deputados')

# Tranformando os dados da consulta no PostegreSQL em DataFrame
df_bd = pd.DataFrame(reg, columns=['id','uri','nome','siglaPartido','uriPartido','siglaUf','idLegislatura','urlFoto','email'])
df_bd.head()