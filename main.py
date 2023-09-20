# A empresa Medieval Softwares deseja aumentar o salário
# dos colaboradores que ganham até R$ 6.000,00 em 10%

# O Arquivo csv contém os dados de todos os colaboradores

# Objetivo: calcular o salário final dos colaboradores que
# se enquadram nos requisitos do aumento

import extract, transform, load

e = extract.Extract("dados.csv")
df = e.extract_data()
t = transform.Transform(df)
df = t.transform_data()
l = load.Load('root','Carlos#38','localhost','colaboradores',df)
l.loading()
print(df)

