## 1. Reading CSV Files with Encodings ##

df = pd.read_csv("laptops.csv", encoding='Latin-1')
df.info()

## 3. Cleaning Column Names Continued ##

def clean_col(col):
    col=col.strip()
    col=col.replace('Operating System','os')
    col=col.replace(' ','_')
    col=col.replace('(','')
    col=col.replace(')','')
    col=col.lower()
    return col

laptops.columns=[clean_col(c) for c in laptops.columns]



## 8. Extracting Values from Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                    .str.split(n=1,expand=True)
                                    .iloc[:,0]
                               )

laptops["cpu_manufacturer"] = (laptops["cpu"].str.split(n=1,expand=True).iloc[:,0]
                               )

## 9. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}
laptops['os']=laptops['os'].map(mapping_dict)

## 10. Dropping Missing Values ##

laptops_no_null_rows=laptops.dropna()
laptops_no_null_cols=laptops.dropna(axis=1)

## 11. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()

laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"
laptops.loc[laptops["os"] == "No OS", "os_version"] ='Version Unknown'
value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()