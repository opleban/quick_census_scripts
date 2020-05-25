import pandas as pd 
import os

# load field metadata values as dataframe
field_metadata_df = pd.read_csv('./metadata/cbg_field_descriptions.csv')
# field_metadata_df.astype('string').dtypes
print(field_metadata_df.dtypes)


# load cbg_geographic values as dataframe
cbg_geographic_df = pd.read_csv('./metadata/cbg_geographic_data.csv')



directory = './data'
for filename in os.listdir(directory):
    frames = []
    if filename.endswith(".csv"):
        current_file = os.path.join(directory, filename)
        print(current_file)
        df = pd.read_csv(current_file)
        # join geographic info
        merged_geo_df = df_joined_to_geo = pd.merge(df, cbg_geographic_df[['census_block_group', 'latitude', 'longitude']], how='left', on='census_block_group', suffixes=('', '_metadata'))
        # melt our column
        melted_df = pd.melt(merged_geo_df, id_vars =['census_block_group', 'latitude', 'longitude'], var_name="measure_code", value_name="measure_value")
        # melted_df['measure_code'] = melted_df['measure_code'].astype('string')
        # print(melted_df.dtypes)
        merged_df = pd.merge(melted_df, field_metadata_df, how='left', left_on='measure_code', right_on='table_id', suffixes=('', '_metadata'))
        frames.append(merged_df)

full_df = pd.concat(frames)

# output to csv
full_df.to_csv('census_output.csv')
print(full_df.dtypes)