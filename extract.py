from pandas import *

class Extract:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv

    def extract_data(self):
        # Lê o arquivo csv e carrega dados no DF
        return read_csv("dados.csv")