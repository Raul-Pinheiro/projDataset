import pandas as pd
from matplotlib import pyplot
from settings import BASE_DIR
import os


def campos_por_metodologia(sample: int, filepath: str):
    output = os.path.join(
        BASE_DIR, filepath
    )

    planilha = pd.read_excel(output, None, skiprows=4, nrows=sample)

    metodologia = 'Corrente/Metodologia de Cálculo'

    campo = 'Nome do Campo'

    pl = planilha['PRP - 01-2023'].sort_values(by=metodologia, ascending=True)

    pyplot.barh(

        pl[metodologia].unique(),
        pl.groupby(metodologia)[campo].count(),

    )

    pyplot.xlabel('Total de Campos')

    pyplot.ylabel('Metodologia')

    pyplot.show()
