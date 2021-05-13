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


def mid_finder(string: str, desired_length: int) -> str:
    half_offset = desired_length // 2
    return string[half_offset : (len(string) - (half_offset + 1))]


def is_empty(account) -> bool:
    return account


def l_row_function(
    previous_id: int,
    current_id: int,
    computer_group: str,
    previous_cloud_account_extrapolated,
    cloud_account,
):
    if is_empty(cloud_account):
        return cloud_account
    else:
        if current_id == previous_id:
            return previous_cloud_account_extrapolated
        else:
            if len(computer_group) > 30:
                return computer_group[11:13]
            else:
                return ""


def k_row_function(l2, k1):
    if l2 == "":
        return k1
    else:
        return l2


def extrapolate_column(data_frame: pd.DataFrame, column: str):
    return data_frame[column][11:13]


df = pd.read_csv("Original 2021-04_securitymoduleusage.csv")
# print(df)

no_fly_list = [
    # "Computers",
    "Computers > Linux \(group 2\) > DPC",
    "Computers > Windows \(group 1\) > DPC",
    "Computers > Windows \(group 1\) > CC",
    "Computers > Linux \(group 2\) > CC",
]

print(df)
df["test"] = df["Computer Group"][11:13]

print(df["test"])
