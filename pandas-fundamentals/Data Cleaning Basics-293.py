## 1. Reading CSV Files with Encodings ##

import pandas as pd
laptops = pd.read_csv("laptops.csv",encoding = "Latin-1")
laptops.info()

## 2. Cleaning Column Names ##

def clean_col(col):
    col = col.strip()
    col = col.replace("Operating System","os")
    col = col.replace(" ","_")
    col = col.replace("(","")
    col = col.replace(")","")
    col = col.lower()
    return col

change_col = []
for ele in laptops.columns:
    clean_c = clean_col(ele)
    change_col.append(clean_c)
    
laptops.columns = change_col   
    

## 3. Converting String Columns to Numeric ##

laptops["screen_size"] = laptops["screen_size"].str.replace('"','').astype(float)
laptops.rename({"screen_size": "screen_size_inches"}, axis=1, inplace=True)
laptops["ram"] = laptops["ram"].str.replace("GB","").astype(int)
laptops.rename({"ram":"ram_gb"},axis=1,inplace=True)
dtypes = laptops.dtypes


## 4. Practicing Converting String Columns to Numeric ##

laptops["weight"] = (laptops["weight"]
                     .str.replace("kgs","")
                     .str.replace("kg","")
                     .astype(float)
                    )
laptops.rename({"weight":"weight_kg"},axis=1,inplace=True)

laptops["price_euros"] = (laptops["price_euros"]
                          .str.replace(",",".")
                          .astype(float)
                         )

weight_describe = laptops["weight_kg"].describe()
price_describe = laptops["price_euros"].describe()



## 5. Extracting Values from the Start of Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                    .str.split(n=1,expand=True)
                                    .iloc[:,0]
                               )

laptops["cpu_manufacturer"] = (laptops["cpu"]
                               .str.split(n=1,expand = True)
                               .iloc[:,0]
                              )

## 6. Extracting Values from the End of Strings ##

screen_res = laptops["screen"].str.rsplit(n=1, expand=True)
screen_res.columns = ["A", "B"]
screen_res.loc[screen_res["B"].isnull(), "B"] = screen_res["A"]
laptops["screen_resolution"] = screen_res["B"]

clean_cpu = laptops["cpu"].str.replace("GHz","")
cpu_res = clean_cpu.str.rsplit(n=1,expand=True)
cpu_res.columns = ["A","B"]
laptops["cpu_speed_ghz"] = cpu_res["B"].astype(float)


## 7. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}
laptops["os"] = laptops["os"].map(mapping_dict)

## 8. Dropping Missing Values ##

laptops_no_null_rows = laptops.dropna(axis=0)
laptops_no_null_cols = laptops.dropna(axis=1)

## 9. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"
laptops.loc[laptops["os"]=="No OS","os_version"] = "Version Unknown"
value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()

## 10. Challenge: Extracting Storage Information ##

laptops["storage"] = (laptops["storage"]
                      .str.replace("+","")
                      .str.replace("Flash Storage","FlashStorage")
                      .str.replace("TB","000")
                      .str.replace("GB","")
                      .str.strip()
                     )

sp_storage = laptops["storage"].str.split(n=3,expand=True)
sp_storage.columns = ["storage_1_capacity_gb","storage_1_type","storage_2_capacity_gb","storage_2_type"]
sp_storage.loc[sp_storage["storage_1_type"]=="FlashStorage","storage_1_type"] = "Flash Storage"
sp_storage.loc[sp_storage["storage_2_type"]=="FlashStorage","storage_2_type"] = "Flash Storage"
sp_storage["storage_1_capacity_gb"] = sp_storage["storage_1_capacity_gb"].astype(float)
sp_storage["storage_2_capacity_gb"] = sp_storage["storage_2_capacity_gb"].astype(float)

# unq_storage1 = sp_storage["storage_1_capacity_gb"].unique()
# unq_storage2 = sp_storage["storage_2_capacity_gb"].unique()
# print(unq_storage1)
# print(unq_storage2)
# unq_storage1 = sp_storage["storage_1_capacity_gb"].unique()
# unq_storage2 = sp_storage["storage_2_capacity_gb"].unique()
# print(unq_storage1)
# print(unq_storage2)


laptops = laptops.drop("storage",axis = 1)
laptops[["storage_1_capacity_gb","storage_1_type","storage_2_capacity_gb","storage_2_type"]] = sp_storage


## 11. Reordering Columns and Exporting Cleaned Data ##

laptops_dtypes = laptops.dtypes
cols = ['manufacturer', 'model_name', 'category', 'screen_size_inches',
        'screen', 'cpu', 'cpu_manufacturer', 'screen_resolution', 'cpu_speed_ghz', 'ram_gb',
        'storage_1_type', 'storage_1_capacity_gb', 'storage_2_type',
        'storage_2_capacity_gb', 'gpu', 'gpu_manufacturer', 'os',
        'os_version', 'weight_kg', 'price_euros']
laptops = laptops[cols]
laptops.to_csv("laptops_cleaned.csv",index = False)
laptops_cleaned = pd.read_csv("laptops_cleaned.csv")
laptops_cleaned_dtypes = laptops_cleaned.dtypes
