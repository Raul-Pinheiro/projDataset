import pandas as pd
from matplotlib import pyplot
from settings import BASE_DIR
import os


def preco_por_campo(sample: int, filepath: str):
    output = os.path.join(
        BASE_DIR, filepath
    )

    planilha = pd.read_excel(output, None, skiprows=4, nrows=sample)

    campo = 'Nome do Campo'

    preco = 'Preço de Referência (R$/m³)'

    pl = planilha['PRP - 01-2023'].sort_values(by=[campo], ascending=True)

    pyplot.plot(pl[campo], pl[preco],)

    pyplot.ylabel('Preço de Referência (R$/m³)')

    pyplot.xlabel('Nome do Campo')

    pyplot.show()
