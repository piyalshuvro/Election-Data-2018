import pandas as pd
import numpy as np
import os
import glob
import shutil
import re

path = "C:\Monash RA Work\Election 2018\Code\ALL DATA Final.csv"
output_path = "C:\Monash RA Work\Election 2018"
#
# for x in os.listdir(path):
#
#     print(path+"\\"+x)
# merge all data
# all_data = []
# for f in glob.glob(output_path + "\*.csv"):
#     all_data.append(pd.read_csv(f))
#
# df = pd.concat(all_data, ignore_index=True)
# df.to_csv(output_path + '\ALL DATA Final.csv', index=False)

# 2013 data
#
# df = pd.read_csv(path)
# seatno = []
# for string in df['seatidentifation1']:
#
#     if "/" in string:
#         new = "/" + string.split("/")[0] + "-" + str(int(string.split("/")[1]))
#         seatno.append(new)
#     elif "-" in string:
#         if "`" in string:
#             string = string.replace("`","")
#         new = "/" + string.split("-")[0] + "/-" + str(int(string.split("-")[1]))
#
#         seatno.append(new)
# df['new'] = df['GP'] + seatno
# df.to_csv("new.csv", index=False)


#2018 data
#
# df = pd.read_csv(path)
# seatno = []
# for string in df['Seat Name']:
#
#     if "/" in string:
#         print(string)
#         new = string.split("/")[0] + "/" + string.split("/")[1].split('-')[0] + "-" + str(int(string.split("/")[1].split('-')[1]))
#         seatno.append(new)
#     elif "-" in string:
#         if "`" in string:
#             string = string.replace("`","")
#         new = "/" + string.split("-")[0] + "/-" + str(int(string.split("-")[1]))
#
#         seatno.append(new)
# df['new'] = df['GP'] + seatno
# df.to_csv("new.csv", index=False)

mapping_df = pd.read_csv("new2013.csv",header=0)
# print(mapping_df.head())
# print(list(mapping_df))

data_df = pd.read_csv("ALL DATA Final.csv",header=0)
# print(list(data_df))
# print(data_df.head())

# gp_df = pd.read_csv("GP_Code_Details.csv")
# print(list(gp_df))

df = pd.merge(mapping_df , data_df, how = 'outer',left_on='new',right_on='Seat Name')
df.to_csv("outer2.csv",index=False)







