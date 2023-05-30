import pandas as pd
from matplotlib import pyplot
from settings import BASE_DIR
import os


def preco_por_metodologia(sample: int, filepath: str):
    output = os.path.join(
        BASE_DIR, filepath
    )

    planilha = pd.read_excel(output, None, skiprows=4, nrows=sample)

    metodologia = 'Corrente/Metodologia de Cálculo'

    preco = 'Preço de Referência (R$/m³)'

    pl = planilha['PRP - 01-2023'].sort_values(
        by=[metodologia], ascending=True
    )

    pyplot.bar(
        pl[metodologia].unique(),
        pl.groupby(metodologia)[preco].mean()
    )

    pyplot.ylabel('Preço de Referência (R$/m³)')

    pyplot.xlabel('Nome do Campo')

    pyplot.show()
