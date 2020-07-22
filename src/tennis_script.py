import matplotlib.pyplot as plt
import numpy as np

def one_dim_scatterplot(data, ax, jitter=0.2, **options):
    if jitter:
        jitter = np.random.uniform(-jitter, jitter, size=data.shape)
    else:
        jitter = np.repeat(0.0, len(data))
    ax.scatter(data, jitter, **options)
    ax.yaxis.set_ticklabels([])
    ax.set_ylim([-1, 1])
    
def get_sample_means(sampler, n_samples, size):
    means = []
    for _ in range(size):
        means.append(np.mean(sampler.rvs(n_samples)))
    return means