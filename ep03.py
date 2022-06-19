import yfinance as yf
from pandas import DataFrame


def pegar_cotacao(ativo):
    ticker = yf.Ticker(ativo)
    hist = ticker.history(period="max")
    return hist


class DataFormat:
    def __init__(self, cotacoes: DataFrame):
        self.df = cotacoes

    def prepare_data(self):
        self.remove_index()
        self.rename_coluns()
        self.remove_columns()
        return self.df

    def rename_coluns(self):
        self.df = self.df.rename({'Open': 'Abertura', 'Close': 'Fechamento'}, axis=1)
        return

    def remove_index(self):
        self.df['dia'] = self.df.index
        self.df = self.df.reset_index(drop=True)
        return

    def remove_columns(self):
        self.df = self.df.drop(['High', 'Low', 'Dividends', 'Stock Splits', 'Volume'], 1)
        return


meus_ativos = ['BBAS3.SA', 'VALE3.SA', 'PETR4.SA', 'COGN3.SA']


for ativo in meus_ativos:
    dados = pegar_cotacao(ativo)
    limpar_dados = DataFormat(dados).prepare_data()
    print(limpar_dados)
