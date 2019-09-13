import pandas as pd
from unidecode import unidecode
from datetime import datetime
import os
import sys
import numpy as np


mobile_holidays = ["carnaval", "paixao de cristo", "corpus christi"]

def execute():
    df = pd.read_excel("feriados_nacionais.xls", na_rep=None)
    df["Feriado"] = df["Feriado"].str.lower()
    df["Feriado"] = df["Feriado"].astype(str)
    df["Feriado"] = df["Feriado"].apply(unidecode)
    df = df.drop(columns="Dia da Semana")
    table_holidays = []
    # dia, mes, ano, estado, municipio, eh_feriado_nacional, eh_feriado_estadual,
    # eh_feriado_municipal, eh_movel, eh_fixo, nome_feriado
    for i in range(df.shape[0]):
        if i in mobile_holidays:
            table_holidays.append(
            [df.iloc[i]["Data"].day,
            df.iloc[i]["Data"].month,
            df.iloc[i]["Data"].year,
            None,
            None,
            1, 0, 0,
            1, 0,
            df.iloc[i]["Feriado"]])
        else:
            table_holidays.append(
            [df.iloc[i]["Data"].day,
            df.iloc[i]["Data"].month,
            df.iloc[i]["Data"].year,
            None,
            None,
            1, 0, 0,
            0, 1,
            df.iloc[i]["Feriado"]])
            
    df2 = pd.read_excel("feriados.xlsx", na_rep=None)
    df2["sigla"] = df2["sigla"].str.lower()
    df2["municipio"] = df2["municipio"].str.lower()
    df2["municipio"] = df2["municipio"].astype(str)
    df2["municipio"] = df2["municipio"].apply(unidecode)
    df2["obs"] = df2["obs"].str.lower()
    df2["obs"] = df2["obs"].astype(str)
    df2["obs"] = df2["obs"].apply(unidecode)
    df2["obs"] = df2["obs"].replace(np.nan, None, regex=True)
    for i in range(df.shape[0]):
        print(df2.iloc[i]["municipio"])
        print(type(df2.iloc[i]["municipio"]))
        if df2.iloc[i]["municipio"] == 'nan':
            table_holidays.append([df2.iloc[i]["dia"], df2.iloc[i]["mês"],None,df2.iloc[i]["sigla"],df2.iloc[i]["municipio"],0, 1, 0, 0, 0, df2.iloc[i]["obs"]])
        else:
            table_holidays.append(
            [df2.iloc[i]["dia"],
            df2.iloc[i]["mês"],
            None,
            df2.iloc[i]["sigla"],
            df2.iloc[i]["municipio"],
            0, 0, 1,
            0, 0,
            df2.iloc[i]["obs"]])
    sys.exit()

    df.to_csv("{}/holidays_brazil.csv".format(os.getcwd()),index=False)

if __name__ == '__main__':
    execute()
