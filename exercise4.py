import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils as bcut

df_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
df_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

df_1973 = df_1973.rename(columns={'yearband':'year'})
df_1973.loc[:, 'year'] = 1973

# Add Years to remaining DataFrames
df_1975.insert(2, 'year', value=1975)
df_1987.insert(2, 'year', value=1987)
df_1991.insert(2, 'year', value=1991)
df_2012.insert(2, 'year', value=2012)

# Rename column titles
df_1973 = df_1973.rename(columns={'beak length': 'beak length (mm)',
                                  'beak depth': 'beak depth (mm)'})
df_1975 = df_1975.rename(columns={'Beak length, mm': 'beak length (mm)',
                                  'Beak depth, mm': 'beak depth (mm)'})
df_1987 = df_1987.rename(columns={'Beak length, mm': 'beak length (mm)',
                                  'Beak depth, mm': 'beak depth (mm)'})
df_1991 = df_1991.rename(columns={'blength': 'beak length (mm)',
                                  'bdepth': 'beak depth (mm)'})
df_2012 = df_2012.rename(columns={'blength': 'beak length (mm)',
                                  'bdepth': 'beak depth (mm)'})

# Remove duplicates from the same year
pd.DataFrame.drop_duplicates(df_1973, subset='band', keep='first')
pd.DataFrame.drop_duplicates(df_1975, subset='band', keep='first')
pd.DataFrame.drop_duplicates(df_1987, subset='band', keep='first')
pd.DataFrame.drop_duplicates(df_1991, subset='band', keep='first')
pd.DataFrame.drop_duplicates(df_2012, subset='band', keep='first')

# Concatenate DataFrames
df_combined = pd.concat((df_1973, df_1975, df_1987, df_1991, df_2012),
                         ignore_index=True, axis=0)

# Plot ECDF of beak depths
df_complete = pd.read_csv('data/grant_complete.csv', comment='#')

df_fd_1987 = df_complete.loc[(df_complete['year']==1987) & (df_complete['species']=='fortis'), 'beak depth (mm)']
df_fl_1987 = df_complete.loc[(df_complete['year']==1987) & (df_complete['species']=='fortis'), 'beak length (mm)']
df_sd_1987 = df_complete.loc[(df_complete['year']==1987) & (df_complete['species']=='scandens'), 'beak depth (mm)']
df_sl_1987 = df_complete.loc[(df_complete['year']==1987) & (df_complete['species']=='scandens'), 'beak length (mm)']

df_fd_1973 = df_complete.loc[(df_complete['year']==1973) & (df_complete['species']=='fortis'), 'beak depth (mm)']
df_fl_1973 = df_complete.loc[(df_complete['year']==1973) & (df_complete['species']=='fortis'), 'beak length (mm)']
df_sd_1973 = df_complete.loc[(df_complete['year']==1973) & (df_complete['species']=='scandens'), 'beak depth (mm)']
df_sl_1973 = df_complete.loc[(df_complete['year']==1973) & (df_complete['species']=='scandens'), 'beak length (mm)']

df_fd_1975 = df_complete.loc[(df_complete['year']==1975) & (df_complete['species']=='fortis'), 'beak depth (mm)']
df_fl_1975 = df_complete.loc[(df_complete['year']==1975) & (df_complete['species']=='fortis'), 'beak length (mm)']
df_sd_1975 = df_complete.loc[(df_complete['year']==1975) & (df_complete['species']=='scandens'), 'beak depth (mm)']
df_sl_1975 = df_complete.loc[(df_complete['year']==1975) & (df_complete['species']=='scandens'), 'beak length (mm)']

df_fd_1991 = df_complete.loc[(df_complete['year']==1991) & (df_complete['species']=='fortis'), 'beak depth (mm)']
df_fl_1991 = df_complete.loc[(df_complete['year']==1991) & (df_complete['species']=='fortis'), 'beak length (mm)']
df_sd_1991 = df_complete.loc[(df_complete['year']==1991) & (df_complete['species']=='scandens'), 'beak depth (mm)']
df_sl_1991 = df_complete.loc[(df_complete['year']==1991) & (df_complete['species']=='scandens'), 'beak length (mm)']

df_fd_2012 = df_complete.loc[(df_complete['year']==2012) & (df_complete['species']=='fortis'), 'beak depth (mm)']
df_fl_2012 = df_complete.loc[(df_complete['year']==2012) & (df_complete['species']=='fortis'), 'beak length (mm)']
df_sd_2012 = df_complete.loc[(df_complete['year']==2012) & (df_complete['species']=='scandens'), 'beak depth (mm)']
df_sl_2012 = df_complete.loc[(df_complete['year']==2012) & (df_complete['species']=='scandens'), 'beak length (mm)']

x_ecdf_fd_1987, y_ecdf_fd_1987 = bcut.ecdf(df_fd_1987)
x_ecdf_sd_1987, y_ecdf_sd_1987 = bcut.ecdf(df_sd_1987)


plt.plot(x_ecdf_fd_1987, y_ecdf_fd_1987, marker='.', alpha=0.5)
plt.plot(x_ecdf_sd_1987, y_ecdf_sd_1987, marker='.', alpha=0.5)
plt.show()
plt.close()

plt.plot(df_fd_1987, df_fl_1987, color='blue', marker='.',
                                 linestyle='none', alpha=1)
plt.plot(df_sd_1987, df_sl_1987, color='red', marker='.',
                                  linestyle='none', alpha=1)
plt.plot(df_fd_1973, df_fl_1973, marker='.', linestyle='none', alpha=1)
plt.plot(df_sd_1973, df_sl_1973, marker='.', linestyle='none', alpha=1)
plt.plot(df_fd_1975, df_fl_1975, marker='.', linestyle='none', alpha=1)
plt.plot(df_sd_1975, df_sl_1975, marker='.', linestyle='none', alpha=1)
plt.plot(df_fd_1991, df_fl_1991, marker='.', linestyle='none', alpha=1)
plt.plot(df_sd_1991, df_sl_1991, marker='.', linestyle='none', alpha=1)
plt.plot(df_fd_2012, df_fl_2012, marker='.', linestyle='none', alpha=1)
plt.plot(df_sd_2012, df_sl_2012, marker='.', linestyle='none', alpha=1)

plt.xlabel('Beak depth (mm)')
plt.ylabel('Beak length (mm)')
plt.legend(('1987', '1973', '1975', '1991', '2012'), loc='lower right')
plt.axis([6, 13, 8, 17])
plt.show()


# Seaborn badass plots
# sns.lmplot(x='beak length (mm)', y='beak depth (mm)', data=df_complete,
#            fit_reg=False, hue='year')
# sns.lmplot(x='beak length (mm)', y='beak depth (mm)', data=df_complete,
#            fit_reg=False, hue='species')
