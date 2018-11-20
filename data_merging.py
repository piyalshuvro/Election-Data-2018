import pandas as pd
import numpy as np
import os
import glob
import shutil

path = "C:\Monash RA Work\Election 2018\Final Data"
output_path = "C:\Monash RA Work\Election 2018\Cleaned Data"
for x in os.listdir(path):

    print(path+"\\"+x)

    for f in glob.glob(path+"\\"+x+"\*.csv"):

        df = pd.read_csv(f)
        df.columns = ['a', 'b','c','d','e','f','g']
        df['h'] =  df["a"].apply(lambda x: x if x.isdigit()==False else None)
        df['i'] = df["a"].apply(lambda x: x if x.isdigit() else None)
        df = df.fillna(method="ffill")
        df = df.dropna().reset_index(drop=True)
        df['j'] = df["a"].apply(lambda x: x if x.isdigit() else None)
        df = df.dropna().reset_index(drop=True)
        del df['i']
        del df['j']
        df = df[['h','a','b','c','d','e','f','g']]
        df.columns = ['Seat Name','Sl.No','Candidate Name', 'Father/Husband', 'Gender', 'Category', 'Party Affiliation', 'Votes in Favour']


        df.to_csv(output_path+"\\"+x+"\\"+os.path.basename(f),index=False)





