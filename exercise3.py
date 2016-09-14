import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import scipy.stats
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize':18, 'axes.titlesize': 18}
sns.set(rc=rc)

wt_lac = np.loadtxt('data/wt_lac.csv', delimiter=',', comments='#', skiprows=3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', delimiter=',', comments='#', skiprows=3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', delimiter=',', comments='#', skiprows=3)


# Calculate fold change
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Calculate fold change given IPTG concentration.
    """
    numerator = RK * (1 + c / KdA)**2
    denom = (1 + c / KdA)**2 + Kswitch * (1 + c / KdI)**2
    fc = (1 + numerator / denom)**(-1)

    return fc

def fold_change_bohr(bohr_parameter):
    """
    Gives Fold change as a function of bohr parameter
    """
    fc_bohr = 1 / (1 + np.exp(-bohr_parameter))

    return fc_bohr


def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """
    Calculate Bohr parameter.
    """
    numerator = (1 + c / KdA)**2
    denom = (1 + c / KdA)**2 + Kswitch * (1 + c / KdI)**2
    bohr_param = -np.log(RK) - np.log(numerator / denom)

    return bohr_param


# Exercise 3.3d
min_iptg = np.min(np.concatenate((wt_lac[:,0], q18m_lac[:,0], q18a_lac[:,0])))
max_iptg = np.min(np.concatenate((wt_lac[:,0], q18m_lac[:,0], q18a_lac[:,0])))
iptg_theory = np.logspace(np.log10(min_iptg), np.log10(max_iptg), 100)
theoretical_fc_wt = fold_change(iptg_theory, 141.5)
theoretical_fc_q18a = fold_change(iptg_theory, 16.56)
theoretical_fc_q18m = fold_change(iptg_theory, 1328)
# Plot data
plt.semilogx(wt_lac[:,0],wt_lac[:,1], marker='.', markersize=20,
           alpha=0.5)
plt.semilogx(q18a_lac[:,0],q18a_lac[:,1], marker='.', markersize=20,
           alpha=0.5)
plt.semilogx(q18m_lac[:,0],q18m_lac[:,1], marker='.', markersize=20,
           alpha=0.5)
plt.semilogx(iptg_theory,theoretical_fc_wt, marker='.', markersize=20,
           alpha=0.5)
plt.semilogx(iptg_theory,theoretical_fc_q18a, marker='.', markersize=20,
           alpha=0.5)
plt.semilogx(iptg_theory,theoretical_fc_q18m, marker='.', markersize=20,
           alpha=0.5)
plt.legend(('wt lac', 'q18a lac', 'q18m lac', 'wt theoretical',
            'q18a theoretical', 'q18m theoretical'), loc='upper left')
plt.show()
plt.close()

# Exercise 3.3e
bohr = np.arange(-6,6)
bohr_wt = bohr_parameter(wt_lac[:,0], 141.5)
bohr_q18a = bohr_parameter(q18a_lac[:,0], 16.56)
bohr_q18m = bohr_parameter(q18m_lac[:,0], 1328)


plt.plot(bohr, fold_change_bohr(bohr), color='black')
plt.plot(bohr_wt, wt_lac[:,1], marker='.', markersize=20,
           alpha=0.5)
plt.plot(bohr_q18a, q18a_lac[:,1], marker='.', markersize=20,
           alpha=0.5)
plt.plot(bohr_q18m, q18m_lac[:,1], marker='.', markersize=20,
           alpha=0.5)
plt.legend(('Black line', 'wt theoretical',
            'q18a theoretical', 'q18m theoretical'), loc='upper left')
plt.xlabel('Bohr Parameter')
plt.ylabel('Theoretical Fold Change')
plt.show()
