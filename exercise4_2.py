import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils as bcut

df_weight = pd.read_csv('data/bee_weight.csv', comment='#')
df_sperm = pd.read_csv('data/bee_sperm.csv', comment='#')
df_sperm = pd.DataFrame.dropna(df_sperm)
# ECDF of drone weight
control = df_weight.loc[df_weight['Treatment']=='Control', 'Weight']
pest = df_weight.loc[df_weight['Treatment']=='Pesticide', 'Weight']

control_sperm = df_sperm.loc[df_sperm['Treatment']=='Control', 'Quality']
pest_sperm = df_sperm.loc[df_sperm['Treatment']=='Pesticide', 'Quality']

x_ecdf_c, y_ecdf_c = bcut.ecdf(control)
x_ecdf_p, y_ecdf_p = bcut.ecdf(pest)

x_ecdf_cs, y_ecdf_cs = bcut.ecdf(control_sperm)
x_ecdf_ps, y_ecdf_ps = bcut.ecdf(pest_sperm)

# Plot ECDFs
plt.plot(x_ecdf_c, y_ecdf_c, marker='.', linestyle='none')
plt.plot(x_ecdf_p, y_ecdf_p, marker='.', linestyle='none')
plt.plot(x_ecdf_cs, y_ecdf_cs, marker='.', linestyle='none')
plt.plot(x_ecdf_ps, y_ecdf_ps, marker='.', linestyle='none')
plt.xlabel('Weight')
plt.ylabel('ECDF')
plt.legend(('Weight-Control', 'Weight-Pesticide','Sperm-Control',
            'Sperm-Pesticide'), loc='upper left')
plt.show()

# Compute mean drone weight
c_mean, c_ci = bcut.draw_bs_reps(control, np.mean, size=10000, CI=True)
p_mean, p_ci = bcut.draw_bs_reps(pest, np.mean, size=10000, CI=True)
s_c_mean, s_c_ci = bcut.draw_bs_reps(control_sperm, np.mean, size=10000, CI=True)
s_p_mean, s_p_ci = bcut.draw_bs_reps(pest_sperm, np.mean, size=10000, CI=True)
s_c_median, s_med_c_ci = bcut.draw_bs_reps(control_sperm, np.median, size=10000, CI=True)
s_p_median, s_med_p_ci = bcut.draw_bs_reps(pest_sperm, np.median, size=10000, CI=True)
