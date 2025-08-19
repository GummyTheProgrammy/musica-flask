import pandas as pd
import numpy as np
import psycopg2

# --- 1. CONFIGURAÇÕES DO BANCO DE DADOS ---
DB_NAME = config.DB_NAME
DB_USER = config.DB_USER
DB_PASS = config.DB_PASS
DB_HOST = config.DB_HOST

# --- 2. GERAÇÃO DE DADOS SINTÉTICOS ---
# Definimos o esquema (colunas)
dados = {
    'produto_id': np.arange(1, 21),
    'produto_nome': [f'Produto_{i}' for i in range(1, 21)],
    'categoria': np.random.choice(['Eletrônicos', 'Roupas', 'Alimentos'], 20),
    'vendas_unidade': np.random.randint(50, 500, 20)
}
# Criamos o DataFrame
df = pd.DataFrame(dados)

# --- 3. CONEXÃO E INSERÇÃO DE DADOS NO POSTGRESQL ---
try:
    # Conecta ao banco de dados
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cursor = conn.cursor()
    print("Conexão com o PostgreSQL estabelecida com sucesso!")

    # Cria uma tabela se ela não existir
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS vendas_sinteticas (
        produto_id INT PRIMARY KEY,
        produto_nome VARCHAR(255),
        categoria VARCHAR(100),
        vendas_unidade INT
    );
    """
    cursor.execute(sql_create_table)
    conn.commit()
    print("Tabela 'vendas_sinteticas' verificada/criada.")

    # Insere os dados do DataFrame na tabela
    for _, row in df.iterrows():
        sql_insert = """
        INSERT INTO vendas_sinteticas (produto_id, produto_nome, categoria, vendas_unidade)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (produto_id) DO UPDATE SET
            produto_nome = EXCLUDED.produto_nome,
            categoria = EXCLUDED.categoria,
            vendas_unidade = EXCLUDED.vendas_unidade;
        """
        cursor.execute(sql_insert, tuple(row))
    
    # Confirma todas as inserções
    conn.commit()
    print("Dados inseridos com sucesso na tabela 'vendas_sinteticas'.")

except (Exception, psycopg2.Error) as error:
    print("Erro ao trabalhar com o PostgreSQL:", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexão com o PostgreSQL fechada.")