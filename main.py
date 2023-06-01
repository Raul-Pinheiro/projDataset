import pandas as pd
from matplotlib import pyplot
import matplotlib
import os
import squarify
import plotly.express as px

arquivo = "./Car_Models.csv"


def grafico_sunburst(amostragem: int = 100):
    """['Company', 'Model', 'Horsepower', 'Torque', 'Transmission Type', 'Drivetrain', 'Fuel Economy', 'Number of Doors', 'Price', 'Model Year Range', 'Body Type', 'Engine Type', 'Number of Cylinders']"""

    output = os.path.join(arquivo)

    planilha = pd.read_csv(output, nrows=amostragem)

    for x in planilha['Model Year Range']:

        print("ITEM", x)

    fig = px.sunburst(
        planilha, path=['Company', 'Model',  'Price'])
    fig.show()


def grafico_de_linha(amostragem: int = 100):
    output = os.path.join(arquivo)

    planilha = pd.read_csv(output, nrows=amostragem)

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


def grafico_de_setores(amostragem: int = 100):
    output = os.path.join(arquivo)

    planilha = pd.read_csv(output, nrows=amostragem)

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

    grafico_sunburst()

    grafico_de_linha()

    grafico_de_setores()


if __name__ == '__main__':

    main()
