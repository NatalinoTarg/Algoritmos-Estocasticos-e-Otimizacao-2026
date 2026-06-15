"""
https://www.statology.org/how-to-perform-monte-carlo-simulations-in-python-with-example/

As simulações de Monte Carlo são um método para compreender a incerteza e prever resultados. 
Em Python, pode-se utilizar ferramentas como o NumPy e o Matplotlib para executar estas simulações e analisar os resultados. 

As simulações de Monte Carlo estimam probabilidades através de uma amostragem aleatória. 
Ajudam a modelar a incerteza e a prever resultados. 
O processo envolve:
-Definir o problema e o modelo.
-Gerar entradas aleatórias para variáveis incertas.
-Executar a simulação várias vezes com entradas aleatórias.
-Analisar a distribuição dos resultados.
-As simulações de Monte Carlo são aplicadas em áreas como finanças, engenharia, física e investigação operacional. 
São particularmente úteis quando é difícil encontrar soluções exatas devido à incerteza ou complexidade.

"""
import numpy as np

# Parameters for the model
mean_sales = 10000
std_dev_sales = 2000
price_min = 10
price_max = 20
fixed_costs = 80000
num_simulations = 10000  # Number of Monte Carlo simulations

# Generate random sales and price per unit
def generate_random_inputs():
    sales = np.random.normal(loc=mean_sales, scale=std_dev_sales)  # Sales follow normal distribution
    price_per_unit = np.random.uniform(low=price_min, high=price_max)  # Price follows uniform distribution
    return sales, price_per_unit

# Função para calcular profit
def calculate_profit(sales, price_per_unit):
    return (sales * price_per_unit) - fixed_costs

# Correr a simulaçáo e guardar resultados
def monte_carlo_simulation(num_simulations):
    profits = []
    for _ in range(num_simulations):
        sales, price_per_unit = generate_random_inputs()
        profit = calculate_profit(sales, price_per_unit)
        profits.append(profit)
    return profits

# Correr o  Monte Carlo
profits = monte_carlo_simulation(num_simulations)

# Output:
print(f"Estimated Profit Distribution (First 5 samples): {profits[:5]}")

import matplotlib.pyplot as plt

# Calcular as medidas estatisticas
mean_profit = np.mean(profits)
std_dev_profit = np.std(profits)
percentiles = np.percentile(profits, [5, 50, 95])

# Print dos resultados:
print(f"Mean Profit: ${mean_profit:.2f}")
print(f"Standard Deviation of Profit: ${std_dev_profit:.2f}")
print(f"5th Percentile Profit: ${percentiles[0]:.2f}")
print(f"50th Percentile Profit (Median): ${percentiles[1]:.2f}")
print(f"95th Percentile Profit: ${percentiles[2]:.2f}")

# Gráfico: 
plt.hist(profits, bins=50, color='skyblue', edgecolor='black')
plt.title('Monte Carlo Simulation: Profit Distribution')
plt.xlabel('Profit ($)')
plt.ylabel('Frequency')
plt.show()
