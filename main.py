import pandas as pd
from matplotlib import pyplot
import matplotlib
import os
import squarify

arquivo = "./Car_Models.csv"


def grafico_de_arvore(sample: int = 100):
    output = os.path.join(arquivo)

    planilha = pd.read_csv(output, nrows=sample)

    df = planilha['Fuel Economy'].value_counts()

    cmap = matplotlib.cm.Blues
    mini = min(df)
    maxi = max(df)
    norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
    colors = [cmap(norm(i)) for i in df]

    print(df)

    squarify.plot(sizes=df, label=df.index, color=colors)

    pyplot.title('Economia de combustível por veículo.')

    pyplot.show()


def grafico_de_linha(sample: int = 100):
    output = os.path.join(arquivo)

    planilha = pd.read_csv(output, nrows=sample)

    pyplot.plot(
        planilha['Company'].unique(),
        planilha.groupby('Company')['Number of Doors'].min(),


    )

    pyplot.ylabel('Número mínimo de portas')
    pyplot.xlabel('Empresa')
    pyplot.ylim((0, 6))
    pyplot.title(
        'Gráfico de Empresa de Carros e seus números mínimos de portas por veículo.'
    )

    pyplot.show()


def grafico_de_setores(sample: int = 100):
    output = os.path.join(arquivo)

    planilha = pd.read_csv(output, nrows=sample)

    pyplot.pie(
        planilha.groupby('Company')['Model'].count(),
        labels=planilha['Company'].unique(),
        autopct="%1.1f%%"
    )

    pyplot.title(
        'Percentual de Modelos de Veículos por Companhia.'
    )

    pyplot.show()


def main():

    grafico_de_arvore()

    grafico_de_linha()

    grafico_de_setores()


if __name__ == '__main__':

    main()
