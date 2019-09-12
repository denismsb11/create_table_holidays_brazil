import pandas as pd
from unidecode import unidecode
from datetime import datetime
import os
import sys

mobile_holidays = ["carnaval", "paixao de cristo", "corpus christi"]

def execute():
    df = pd.read_excel("feriados_nacionais.xls", na_rep=None)
    df["Feriado"] = df["Feriado"].str.lower()
    df["Feriado"] = df["Feriado"].astype(str)
    df["Feriado"] = df["Feriado"].apply(unidecode)
    df = df.drop(columns="Dia da Semana")
    table_holidays = []
    # dia, mes, ano, estado, eh_feriado_nacional, eh_feriado_estadual,
    # eh_feriado_municipal, eh_movel, eh_fixo, nome_feriado
    for i in range(df.shape[0]):
        if i in mobile_holidays:
            table_holidays.append([df.iloc[i]["Data"].day, df.iloc[i]["Data"].month, df.iloc[i]["Data"].year, 1, 0, 0, None, 1, 0, df.iloc[i]["Feriado"]])
        else:
            table_holidays.append([df.iloc[i]["Data"].day, df.iloc[i]["Data"].month, df.iloc[i]["Data"].year, 1, 0, 0, None, 0, 1, df.iloc[i]["Feriado"]])

            
    df2 = pd.read_excel("feriados.xlsx", na_rep=None)
    print(df2.head(10))
    print(df2.iloc[0]["Município"])
    print(type(df2.iloc[0]["Município"]))
    df2 = df2["Município"].isnull()
    print(df2.head(20))
    sys.exit()

    df.to_csv("{}/holidays_brazil.csv".format(os.getcwd()),index=False)
    #df["Data"] = pd.to_datetime(df['Data'])
    print(df.head(20))



if __name__ == '__main__':
    execute()

import pandas as pd
from unidecode import unidecode
from datetime import datetime
import os
import sys

mobile_holidays = ["carnaval", "paixao de cristo", "corpus christi"]

def execute():
    df = pd.read_excel("feriados_nacionais.xls", na_rep=None)
    df["Feriado"] = df["Feriado"].str.lower()
    df["Feriado"] = df["Feriado"].astype(str)
    df["Feriado"] = df["Feriado"].apply(unidecode)
    df = df.drop(columns="Dia da Semana")
    table_holidays = []
    holidays = list(df["Feriado"])

    for i in range(df.shape[0]):
        print(df.iloc[i]["Data"].date())
        print(df.iloc[i]["Feriado"])
        table_holidays.append([df.iloc[i]["Data"].day, df.iloc[i]["Data"].month, df.iloc[i]["Data"].year, 1, 0, 0, ])
    
    df2 = pd.read_excel("feriados.xlsx", na_rep=None)
    print(df2.head(10))
    print(df2.iloc[0]["Município"])
    print(type(df2.iloc[0]["Município"]))
    df2 = df2["Município"].isnull()
    print(df2.head(20))
    sys.exit()

    df.to_csv("{}/holidays_brazil.csv".format(os.getcwd()),index=False)
    #df["Data"] = pd.to_datetime(df['Data'])
    print(df.head(20))



if __name__ == '__main__':
    execute()