import numpy as np
from numpy.core.fromnumeric import size
import tkinter as tk
import tkinter.messagebox
import pandas as pd
import matplotlib.pyplot as plt

class stat_regression:
    a = np.array([0, 0], np.float)

    def __init__(self, data):
        self.data = pd.DataFrame(data)
        sum_of_x = np.sum(self.data.iloc[:, 0])
        sum_of_y = np.sum(self.data.iloc[:, 1])
        sum_of_sqrdx = np.sum(self.data.iloc[:, 0]**2)
        sum_of_xy = np.sum(self.data.iloc[:, 0]*self.data.iloc[:, 1])
        self.data_size = len(self.data)
        self.a[0] = (sum_of_y*sum_of_sqrdx - sum_of_x*sum_of_xy)/(self.data_size*(sum_of_sqrdx) - sum_of_x**2)
        self.a[1] = (self.data_size*(sum_of_xy) - sum_of_x*sum_of_y)/(self.data_size*(sum_of_sqrdx) - sum_of_x**2)

        #Coleta o eixo y da reta em todos os pontos (dados encontrados com os cálculos para a mesma).
        self.calculate_y = self.predict(self.data.iloc[:, 0])
        self.global_error = 0

        media_reta_y = np.sum(self.calculate_y)/(len(self.calculate_y))
        media_real_y = np.sum(self.data.iloc[:, 1])/(len(self.calculate_y))
        somatorio = 0
        variancia_real = 0
        variancia_reta = 0
        for i in range(0, len(self.calculate_y)):
            #Atribui a variável de erro global a soma de todos os erros (erro em um ponto = valor calculado - valor real) ao quadrado (método de erro global ao quadrado).
            self.global_error += (self.calculate_y[i] - self.data.iloc[i, 1])**2
            #Atribui a variável de grau de dependência a soma de valor calculado - valor real em todos os pontos elevados ao quadrado e divididos pelo valor calculado (qui quadrado).
            somatorio += (self.data.iloc[i, 1] - media_real_y)*(self.calculate_y[i] - media_reta_y)
            variancia_real += (self.data.iloc[i, 1] - media_real_y)**2
            variancia_reta += (self.calculate_y[i] - media_reta_y)**2

        #Faz a média geral dividindo o erro encontrado pela quantidade de valores.
        self.global_error = self.global_error/len(self.calculate_y)
        self.degree_dependencies = somatorio/np.sqrt(variancia_real*variancia_reta)

        if(self.degree_dependencies > 0.9):
            self.message_degree = "Very strong correlation"
        elif(self.degree_dependencies > 0.7):
            self.message_degree = "Strong correlation"
        elif(self.degree_dependencies > 0.5):
            self.message_degree = "Moderate correlation"
        elif(self.degree_dependencies > 0.3):
            self.message_degree = "Weak correlation"
        else:
            self.message_degree = "Negligible correlation"

    """
        Função responsável por aplicar o modelo encontrado
    """
    def predict(self, x):
        return self.a[0] + self.a[1]*x

    """
        Função responsável pela geração do gráfico (a mesma será chamada ao clica em seu devido botão).
    """
    def show_graphic(self):
        self.data.plot(x=0, y=1, kind='scatter')
        x = [min(self.data.iloc[:, 0]), max(self.data.iloc[:, 0])]
        y = [self.predict(x[0]), self.predict(x[1])]
        plt.plot(x, y, color="red")
        plt.show()

    """
        Função responsável pelo cálculo do erro (a mesma será chamada ao clica em seu devido botão e irá ser gerada uma subjanela).
    """
    def show_error(self):
        tkinter.messagebox.showinfo(title='The global error', message=f'Global error (squared solution) = {self.global_error}')

    """
        Função responsável pelo cálculo do grau de dependência entre os pontos (a mesma será chamada ao clica em seu devido botão).
    """
    def show_degree_dep(self):
        tkinter.messagebox.showinfo(title='The dependency degree', message=f'Dependency degree (Pearson correlation) = {self.degree_dependencies}\n{self.message_degree}')

    """
        Função responsável pelo cálculo do modelo matemático encontrado (a mesma será chamada ao clica em seu devido botão).
    """
    def show_mathematical_model(self):
        tkinter.messagebox.showinfo(title='The mathematical model', message=f'f(x) = {self.a[0]} + {self.a[1]}x')