import pandas as pd
import os
import pickle
import sys
import requests
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, apriori, association_rules

#if response.status_code == 200:

dataset_url = os.environ.get('DATASET_URL', 'https://homepages.dcc.ufmg.br/~cunha/hosted/cloudcomp-2023s2-datasets/2023_spotify_ds1.csv')

response = requests.get(dataset_url, verify=False)

if response.status_code == 200:
    with open('/data/2023_spotify_ds1.csv', 'wb') as file:
        file.write(response.content)
else:    
    sys.exit(f"No file exists! {response.status_code}")

df = pd.read_csv('/data/2023_spotify_ds1.csv')

dataset = []
len(df['pid'].unique())
for i in df['pid'].unique():
    temp = []
    for j in df[df['pid'] == i].index:
        temp.append(df['track_name'][j])
    dataset.append(temp)
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df_t = pd.DataFrame(te_ary, columns=te.columns_)

freqItemSet = apriori(df_t, min_support=0.06,use_colnames=True)
rules = association_rules(freqItemSet, metric="confidence", min_threshold=0.05)

path = "/data/rules.pickle"
# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(path), exist_ok=True)
# Save the rules as pickle
with open(path, "wb") as file:
    pickle.dump(rules, file)