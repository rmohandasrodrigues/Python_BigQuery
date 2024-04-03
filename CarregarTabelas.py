import pandas as pd
import os

from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv

#Carregar variaveis de ambiente do arquivo .env
load_dotenv()

# Carregando os dados da tabela csv
produtos = pd.read_csv("repositorio/tabelas/produtos.csv", sep=';')
print(produtos)

# Realizando a conexão com o BigQuery
key_path = os.getenv("KEY_PATH")
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])

# Especificando o esquema da tabela
schema = [
    bigquery.SchemaField("id", "INTEGER"),
    bigquery.SchemaField("descricao", "STRING"),
    bigquery.SchemaField("qdt", "INTEGER"),
    bigquery.SchemaField("valor", "FLOAT"),
]

# Criando uma tabela no BigQuery com o esquema especificado
client = bigquery.Client(credentials=credentials, project=os.getenv("PROJECT_ID"))
table_id = os.getenv("TABLE_PRODUTOS")
table = bigquery.Table(table_id, schema=schema)
client.create_table(table, exists_ok=True)  # Se a tabela já existir, ela será substituída

# Carregando os dados na tabela
job_config = bigquery.LoadJobConfig(
    schema=schema,
    write_disposition="WRITE_TRUNCATE"  # Substituir os dados existentes na tabela
)
job = client.load_table_from_dataframe(produtos, table_id, job_config=job_config)
job.result()  # Aguarda a conclusão do job

print("Dados carregados com sucesso no BigQuery!")