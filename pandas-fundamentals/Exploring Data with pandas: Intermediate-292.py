## 4. Using iloc to select by integer position continued ##

import pandas as pd
import numpy as np

f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

fifth_row=f500.iloc[4]
first_three_rows=f500[0:3]
first_seventh_row_slice=f500.iloc[[0,6],0:5]

## 5. Using pandas methods to create boolean masks ##

previously_ranked=f500[f500['previous_rank'].notnull()]
rank_change=previously_ranked['rank']-previously_ranked['previous_rank']

## 8. Using Boolean Operators ##

big_rev_neg_profit=f500.loc[(f500['revenues']>100000)&(f500['profits']<0)]
filter_tech_outside_usa=(f500['sector']=='Technology') & ~(f500['country']=='USA')
tech_outside_usa=f500[filter_tech_outside_usa].head()

## 11. Using Loops with pandas ##


top_employer_by_country={}
countries=f500['country'].unique()
for c in countries:
    selected_rows=f500.loc[f500['country']==c]
    sorted_rows=selected_rows.sort_values(by='employees',ascending=False)
    top_employer=sorted_rows.iloc[0]
    employer_name=top_employer['company']
    top_employer_by_country[c]=employer_name

## 12. Challenge: Calculating Return on Assets by Country ##

f500['roa']=f500['profits']/f500['assets']
f500.sort_values('sector',ascending=False)
top_roa_by_sector={}
for s in f500['sector'].unique():
    is_sector=f500['sector']==s
    sector_companies=f500.loc[is_sector]
    top_company=sector_companies.sort_values('roa',ascending=False).iloc[0]
    company_name=top_company['company']
    top_roa_by_sector[s]=company_name