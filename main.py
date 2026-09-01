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

def sobrevivencia_faixa_etaria(df):

    grupos = [0,12,18,59,100]
    nomes = ['Criancas (0-12)', 'Jovens (13-18)', 'Adultos (19-59)', 'Idosos (60+)']

    #cria uma nova coluna no df, de acordo com o que decidimos nos grupos e nomes
    df['Faixa Etaria'] = pd.cut(df['Age'], bins = grupos, labels = nomes)
    #agrupamos por cada grupo do faixa etaria e calculamos a porcentagem de sobreviventes, observerd = true pra tirar o warning
    taxa = df.groupby('Faixa Etaria', observed = True)['Survived'].mean().round(2) * 100
    #faz com que os indices voltem a ser 0,1,2... e nao os nomes dados. isso ajuda na criacao do grafico
    taxa = taxa.reset_index()
    
    print("Taxa de sobrevivencia por grupo demografico:")
    print(taxa)


    plt.figure(figsize = (10,6))
    #hue = faixa etaria e legend = false para tirar warnig
    sns.barplot(data=taxa, x='Faixa Etaria', y='Survived', hue='Faixa Etaria', palette='Set2', legend=False)
    
    plt.title('Taxa de sobrevivencia por grupo demografico')
    plt.xlabel('Faixa etaria')
    plt.ylabel('Taxa de Sobrevivência')
    plt.ylim(0,100)

    plt.show()

    return taxa



#estatisticas = idade_genero_classe(df)
taxa = sobrevivencia_faixa_etaria(df)