import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.title("Central Limit Theorem Demo")

st.write(
    "Pick a sample size and run a bunch of simulations. "
    "As the sample size goes up, the sample mean starts to look more normal."
)

lam = st.slider("Lambda (rate)", 0.5, 3.0, 1.0)
n = st.slider("Sample size (n)", 1, 200, 30)
sims = st.slider("Simulations", 500, 10000, 5000)

rng = np.random.default_rng(42)

# generate sims experiments, each with n draws
samples = rng.exponential(scale=1/lam, size=(sims, n))

# take the mean of each experiment
means = samples.mean(axis=1)

fig, ax = plt.subplots()
ax.hist(means, bins=40, density=True)
ax.set_title("Distribution of Sample Means")
ax.set_xlabel("Sample mean")
ax.set_ylabel("Density")

st.pyplot(fig)
