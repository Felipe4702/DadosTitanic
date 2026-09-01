import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/titanic.csv', sep=',')

def idade_genero_classe(df):
    #agrupa as estatisticas por sexo e clase, dentro disso pega e idade e faz as operacoes matematicas
    estatisticas = df.groupby (['Sex', 'Pclass'])['Age'].agg(['mean', 'median', 'std']).round(2)
    print("e\Estatisticas Idade por Genero e Classe:")
    print(estatisticas)


    #faz um grafico de caixas com o eixo x sendo as 3 classes e o y a idade, com sexos sendo diferenciados por cores
    plt.figure(figsize = (10,6))
    sns.boxplot(data=df, x = 'Pclass', y = 'Age', hue = 'Sex', palette = 'Set2')
    plt.title('Estatisticas Idade por Genero e Classe')
    plt.xlabel('Classe Social')
    plt.ylabel('Idade')
    plt.legend(title = 'Genero')

    #as caixas marcam onde comeca o 2 quartil e onde comeca o 4, com a linha horizontal sendo a mediana
    #a altura das linhas verticais sao calculadas como sendo 1.5 vezes o tamanho da caixa
    plt.show()

    return estatisticas

estatisticas = idade_genero_classe(df)