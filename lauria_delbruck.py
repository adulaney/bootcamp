import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Specify parameters
n_gen = 16

# Chance of having beneficial mutation.
r = 1e-5

# Total number of cells
n_cells = 2**(n_gen - 1)

# Adaptive immunity: binomial distribution
ai_samples = np.random.binomial(n_cells, r, size=100000)

# Report mean and std
print('AI mean:', np.mean(ai_samples))
print('AI std:', np.std(ai_samples))
print('AI Fano:', np.var(ai_samples) / np.mean(ai_samples))


# Function to draw out of random mutation hypothesis
def draw_random_mutation(n_gen, r):
    """Draw sample under random mutation hypothesis."""
    # Initialize
    n_mut = 0
    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g - 2 * n_mut, r)

    return n_mut


def sample_random_mutation(n_gen, r, size=1):
    # Initialize
    samples = np.empty(size)

    # Draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen,r)

    return samples

rm_samples = sample_random_mutation(n_gen, r, 100000)

# Report mean and std
print('RM mean:', np.mean(rm_samples))
print('RM std:', np.mean(rm_samples))
print('RM Fano:', np.var(rm_samples) / np.mean(rm_samples))
