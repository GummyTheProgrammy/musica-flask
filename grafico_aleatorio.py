# Importa as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

# 1. Cria dados aleatórios
# np.random.rand(50) gera um array de 50 números aleatórios entre 0 e 1
x = np.random.rand(50)
y = np.random.rand(50)

# 2. Cria o gráfico
# plt.figure() cria uma nova figura onde o gráfico será desenhado
plt.figure(figsize=(8, 6))

# plt.scatter() cria um gráfico de dispersão (pontos)
# Os parâmetros são os dados do eixo X, Y, o tamanho dos pontos (s) e a cor (c)
plt.scatter(x, y, s=100, c='blue', alpha=0.7)

# 3. Adiciona títulos e rótulos ao gráfico para facilitar a leitura
plt.title('Gráfico de Dispersão de Dados Aleatórios')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adiciona uma grade ao fundo do gráfico
plt.grid(True)

# 4. Mostra o gráfico
# plt.show() exibe a janela com o gráfico.
# Esta linha é essencial para que a visualização apareça.
plt.show()