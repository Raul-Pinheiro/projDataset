from graficos import *


def main():
    preco_por_metodologia(sample=10, filepath='datasets/precos.xlsx')
    preco_por_campo(sample=10,  filepath='datasets/precos.xlsx')
    campos_por_metodologia(sample=10,  filepath='datasets/precos.xlsx')


if __name__ == '__main__':

    main()
