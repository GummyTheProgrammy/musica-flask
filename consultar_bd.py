import pandas as pd
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt
import psycopg2.errors

# Puxa as informações do arquivo config.py
import config

# --- 1. CONFIGURAÇÕES DO BANCO DE DADOS ---
DB_NAME = config.DB_NAME
DB_USER = config.DB_USER
DB_PASS = config.DB_PASS
DB_HOST = config.DB_HOST

# --- 2. QUERY SQL PARA PEGAR OS DADOS AGREGADOS ---
sql_query = """
SELECT
    categoria,
    SUM(vendas_unidade) AS vendas_totais
FROM
    vendas_sinteticas
GROUP BY
    categoria
ORDER BY
    vendas_totais DESC;
"""

# Inicializamos a variável 'conn' com 'None'
conn = None

# --- 3. CONEXÃO E OBTENÇÃO DOS DADOS COM PYTHON ---
try:
    # Conecta ao banco de dados PostgreSQL
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    print("Conexão com o PostgreSQL estabelecida com sucesso!")
    
    # Executa a query SQL e carrega o resultado em um DataFrame do pandas
    df_analise = pd.read_sql_query(sql_query, conn)
    
    print("\nDados obtidos com sucesso. Criando o gráfico...")

except (Exception, psycopg2.Error) as error:
    print("Erro ao conectar ou executar a query:", error)
finally:
    # Apenas tenta fechar a conexão se ela foi estabelecida
    if conn:
        conn.close()
        print("Conexão com o PostgreSQL fechada.")

# --- 4. GERAÇÃO DO GRÁFICO DE BARRAS ---
plt.figure(figsize=(10, 6))
sns.barplot(x='categoria', y='vendas_totais', data=df_analise, palette='viridis')

plt.title('Vendas Totais por Categoria', fontsize=16)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Vendas Totais', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

