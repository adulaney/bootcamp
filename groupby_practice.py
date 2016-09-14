import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

impf_I = df.loc[df['ID']=='I','impact force (mN)']
impf_II = df.loc[df['ID']=='II','impact force (mN)']
impf_III = df.loc[df['ID']=='III','impact force (mN)']
impf_IV = df.loc[df['ID']=='IV','impact force (mN)']

total_I = 0
total_II = 0
total_III = 0
total_IV = 0

for i in range(len(impf_I)+len(impf_II)+len(impf_III)+len(impf_IV)):
    if i < 20:
        total_I = impf_I.loc[i]
    elif i >= 20 and i<40:
        total_II = impf_II.loc[i]
    elif i>=10 and i<60:
        total_III = impf_III.loc[i]
    elif i >= 60:
        total_IV = impf_IV.loc[i]
mean_I = total_I / len(impf_I)
mean_II = total_II / len(impf_II)
mean_III = total_III / len(impf_III)
mean_IV = total_IV / len(impf_IV)

df_impf = df.loc[:, ['ID', 'impact force (mN)']]

# Make Groupby object
grouped = df_impf.groupby('ID')

# Apply the np.mean function to the grouped object
df_mean_impf = grouped.apply(np.mean)
