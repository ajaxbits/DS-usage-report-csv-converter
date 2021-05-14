import csv
import pandas as pd
import numpy as np

# For L2
# =IF(LEN(M2)>0,M2,(IF(A2=A1,L1,(IF(LEN(D2)>30,MID(D2,12,13),"")))))

# For K2
# IF(L2="",K1,L2)


def substring_row_eliminator(
    column, no_fly_list: list, data_frame: pd.DataFrame
) -> pd.DataFrame:
    for string in no_fly_list:
        data_frame = data_frame[~data_frame[column].str.contains(string)]
    return data_frame


def extrapolate_column(data_frame: pd.DataFrame, column: str):
    return data_frame[column].str[12:24]


def accounts_extrapolated(data_frame):
    mask = data_frame["Computer Group"].str.len() > 30
    data_frame.loc[mask, "Cloud Account Extrapolated"] = extrapolate_column(
        data_frame, "Computer Group"
    )
    return data_frame


def accounts_extrapolated_use_this_one(data_frame):
    data_frame["Cloud Account Extrapolated (Use This Column)"] = data_frame[
        "Cloud Account Extrapolated"
    ].fillna(method="ffill")
    return data_frame


def order_data_frame(data_frame):
    cols = [
        "id",
        "hostname",
        "Display Name",
        "Computer Group",
        "Instance Type",
        "Start Date",
        "Start Time",
        "Stop Date",
        "Stop Time",
        "Duration (Seconds)",
        "Cloud Account Extrapolated (Use This Column)",
        "Cloud Account Extrapolated",
        "Cloud Account",
        "AM",
        "WRS",
        "AC",
        "IM",
        "LI",
        "FW",
        "DPI",
    ]
    return data_frame[cols]


df = pd.read_csv("Original 2021-04_securitymoduleusage.csv")

no_fly_list = [
    "Computers > Linux \(group 2\) > DPC",
    "Computers > Windows \(group 1\) > DPC",
    "Computers > Windows \(group 1\) > CC",
    "Computers > Linux \(group 2\) > CC",
]

df = substring_row_eliminator("Computer Group", no_fly_list, df)
df = accounts_extrapolated(df)
df = accounts_extrapolated_use_this_one(df)
df = order_data_frame(df)
# TODO arrange by computer group and add the second workbook sheet

df.to_csv("modified.csv")
