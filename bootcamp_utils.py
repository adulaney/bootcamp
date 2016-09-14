"""
bootcamp_utils: A collection of statistical functions
# proved useful 55 students
"""

import numpy as np

def ecdf(data):
    """
    Compute x, y values for an empirical distribution function.
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)
    return x, y


def draw_bs_reps(data, func, size=1, interval=[2.5, 97.5], CI='False'):
    """
    Generates bootstrap replicas of data and CI for desired statistic.
    """
    n = len(data)
    bs_replicates = np.empty(size)
    # Generate bootstrap replicas
    for i in range(size):
        bs_sample = np.random.choice(data, replace=True, size=n)
        bs_replicates[i] = func(bs_sample)
    conf_int = np.percentile(bs_replicates, interval)
    if CI == True:
        return bs_replicates, conf_int
    else:
        return bs_replicates
