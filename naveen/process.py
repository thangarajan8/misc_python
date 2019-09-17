
def parseData(filePath):
    columns = 'route,drug_name,ingredients,etime,man_name,ing_count'.split(',')
    data = []
    man_names = []
    print('Processing {}'.format(filePath))
    try:
        with open(filePath,'r') as f:
            i = 0
            content = f.read()
            json_data = json.loads(content)
            results = json_data['results']
            for result in results:
#                print(i)
                if 'route' in result['openfda'].keys():
                    route = result['openfda']['route'].split(',')
                else:
                    route = ['NA']
                if 'substance_name' in result['openfda'].keys():
                    drug_name = result['openfda']['substance_name']
                else:
                    drug_name = ['NA']
                if 'spl_product_data_elements' in result.keys():
                    ingr = result['spl_product_data_elements']
                else:
                    ingr = ['NA']
                if 'manufacturer_name' in result['openfda'].keys():
                        man_name = result['openfda']['manufacturer_name'][0].strip()
                else:
                    man_name = 'NA'
                    
                e_time = result['effective_time']
                i += 1
                data.append([','.join(route),','.join(drug_name),','.join(ingr),e_time[:4],man_name,len(''.join(ingr).split(','))])
        return pd.DataFrame(data,columns=columns),man_names
    except Exception:
        raise
        print(filePath,i)

def pandas_explode(df, column_to_explode):
    """
    Similar to Hive's EXPLODE function, take a column with iterable elements, and flatten the iterable to one element 
    per observation in the output table

    :param df: A dataframe to explod
    :type df: pandas.DataFrame
    :param column_to_explode: 
    :type column_to_explode: str
    :return: An exploded data frame
    :rtype: pandas.DataFrame
    """

    # Create a list of new observations
    new_observations = list()

    # Iterate through existing observations
    for row in df.to_dict(orient='records'):

        # Take out the exploding iterable
        explode_values = row[column_to_explode]
        del row[column_to_explode]

        # Create a new observation for every entry in the exploding iterable & add all of the other columns
        for explode_value in explode_values:

            # Deep copy existing observation
            new_observation = copy.deepcopy(row)

            # Add one (newly flattened) value from exploding iterable
            new_observation[column_to_explode] = explode_value

            # Add to the list of new observations
            new_observations.append(new_observation)

    # Create a DataFrame
    return_df = pd.DataFrame(new_observations)

    # Return
    return return_df
import copy
import json

import pandas as pd
import glob
import os
from collections import Counter
path = 'E:\\learnings\\python\\naveen\\data'
extension = 'json'
os.chdir(path)
filePaths = glob.glob('*.{}'.format(extension))
data = []
ms = []
for filePath in filePaths:
    d,m= parseData(os.path.join(path,filePath))
    data.append(d)
    ms += m
drug_df = pd.concat(data)
man_name_counter = dict(Counter(ms))
sample = drug_df.head(10)
aster_df = drug_df.loc[drug_df['man_name']=='AstraZeneca Pharmaceuticals LP']
#'AstraZeneca Pharmaceuticals LP'

aster_df_a = aster_df.groupby(['etime','drug_name'],as_index=False)['ing_count'].mean()

drug_df['route_list'] = drug_df.apply(lambda x : x['route'].split(','),axis=1)
X = pandas_explode(drug_df,'route_list')

aster_df_b = X.groupby(['etime','route_list'],as_index=False)['ing_count'].mean()

aster_df_b['ing_count'] = aster_df_b['ing_count'].astype(int)

aster_df_a['ing_count'] = aster_df_a['ing_count'].astype(int)

aster_df_a.to_csv("aster_partA.csv",index=False)
aster_df_b.to_csv("aster_partB.csv",index=False)






a = [1,2,3,4,5,6,7,8,9]
for i in a:
    {a:i}
    print(a)
    
