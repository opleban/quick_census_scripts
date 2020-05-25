import pandas as pd 
import os

# load zcta to county crosswalk dataframe
zcta_county_rel_df = pd.read_csv('./metadata/zcta_county_rel_10.csv')
zcta_county_rel_df['ZCTA5'] = zcta_county_rel_df['ZCTA5'].astype(str).str.zfill(5)
zcta_county_rel_df['STATE'] = zcta_county_rel_df['STATE'].astype(str).str.zfill(2)
zcta_county_rel_df['COUNTY'] = zcta_county_rel_df['COUNTY'].astype(str).str.zfill(3)

# load field metadata values as dataframe
cbg_fips_codes_df = pd.read_csv('./metadata/cbg_fips_codes.csv')
cbg_fips_codes_df['state_fips'] = cbg_fips_codes_df['state_fips'].astype(str).str.zfill(2)
cbg_fips_codes_df['county_fips'] = cbg_fips_codes_df['county_fips'].astype(str).str.zfill(3)



# merge them

merged_df = pd.merge(zcta_county_rel_df[['ZCTA5', 'STATE', 'COUNTY']], cbg_fips_codes_df[['state_fips', 'state', 'county_fips', 'county', 'class_code']], how='left', left_on=['STATE','COUNTY'], right_on=['state_fips','county_fips'])

print("MERGED \n \n")
print(merged_df.dtypes)
# output to csv
merged_df.to_csv('zcta_with_county_info.csv')