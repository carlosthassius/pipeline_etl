from pandas import *

class Transform:
    def __init__(self, df):
        self.df = df

    def transform_data(self):
        # DF com colaboradores que receberão aumento
        df_t = self.df[self.df['Salário']<=6000].copy()

        # Iterador para criar uma lista com os salários ajustados
        self.new_value = []
        for value in df_t['Salário']:
            self.new_value.append(int(value*1.1))

        # Atribui os valores da lista à nova coluna
        df_t.loc[:, 'Salário ajustado'] = self.new_value
        return df_t