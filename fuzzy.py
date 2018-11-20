from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import numpy as np
mapping_df = pd.read_csv("new2013.csv",header=0)
# print(mapping_df.head())
# print(list(mapping_df))

data_df = pd.read_csv("ALL DATA Final.csv",header=0)

# print(mapping_df.head())
# print(list(mapping_df))
seat2013 = mapping_df['new'].unique()
# print(seat2013)
print(str(len(seat2013)))

# print(list(data_df))
# print(data_df.head())
seat2018 = data_df['Seat Name'].unique()

print(str(len(seat2018)))
sorted(seat2013)
i = 25110
with open("matching903.txt","w") as file:
    for p in seat2018[25110:]:
        file.write(str(i) + ". " + p + "\n")
        i = i+1
        for l in seat2013:


            if (fuzz.ratio(p,str(l)) > 90 ):
                if (fuzz.ratio(p, str(l)) == 100):
                    print("Found!! 100 " + str(i) + " " + str(p) + " " + str(l))
                    file.write(p + "\t\t" + str(l) + "\t" + str(fuzz.ratio(p, str(l))) + "\n")
                    index = np.argwhere(seat2013==p)
                    print(seat2013[index])
                    seat2013 = np.delete(seat2013,index)
                    print(str(len(seat2013)))
                    break
                print("Found!! " + str(i) + " " + str(p) + " " + str(l) )
                file.write(p +"\t\t"+  str(l) + "\t"+ str(fuzz.ratio(p,str(l)))+ "\n" )


        file.write("\n")


# print(str(len(pancayet)))
# print(str(len(local_body)))
# print(str(fuzz.ratio(pancayet, local_body)))