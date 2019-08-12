#Savannah Dessert, cssc0696
#Using COLED-V Organization Name File from the United States National Archives condition the file and convert to CSV file
#The script displays each major command by name and a quick overview of the units in its structure in an easy to read format. 

import pandas as pd

def view_layout(df):
    cmd = (df["Major Command Code"].unique())[7:]
    for i in cmd:
        df1 = df.loc[df["Major Command Code"] == i]
        print("Major Command Code:{}".format(i))
        cmd2 = df1["Major Command Code2"].unique()
        for j in cmd2:
            df2 = df1.loc[df1["Major Command Code"] == j]
            unit = df2["Major Unit Name"].unique()
            print("\t Major Command Code2:{}".format(j))
            for k in unit:
                print("\t\t Unit Name: {}".format(k))
                df3 = df2.loc[df2["Major Unit Name"] == k]
                sub = df3["Sub-Unit Name"].unique()
                for l in sub:
                    df4 = df3.loc[df3["Sub-Unit Name"] == l]
                    subno = df4["Sub-Unit No."].unique()
                    dep = df4["Unit Branch"].unique()
                    print("\t\t\t Sub-Unit Name: {}".format(l))
                    for m in subno:
                        print("\t\t\t\t Sub-Unit No.: {}".format(m))
                        for n in dep:
                            print("\t\t\t\t\t Branch Department: {}".format(n))
                            
def condition(df, col_names):
    col_names.remove("spaces") #remove empty spaces
    col_names.remove("space")
    df = df.drop(columns = "space")
    df = df.drop(columns = "spaces")
    df =  df.dropna()
    df = df.iloc[0:2392,:] #drop last row of all 9s
    if not df["Major Command Code"].equals(df["Major Command Code2"]):
        col_names.remove("Major Command Code2")
        df.drop(columns = "Major Command Code2")
    df = df.sort_values(by = col_names)
    view_layout(df)               
    
def read_file():
    try:
        col_widths = [2, 3, 2, 13, 3, 2, 3, 12, 2, 38]
        col_names = ["Major Command Code", "space", "Major Command Code2", "Major Unit Name", "Sub-Unit UIC", "Company Designation", "Sub-Unit No.", "Sub-Unit Name", "Unit Branch", "spaces"]
        df = pd.read_fwf("./RG338.COLEDV.ONAM", widths=col_widths, names=col_names )
        condition(df, col_names)
    except FileNotFoundError:
        print("File not found")
        return
   
read_file()
