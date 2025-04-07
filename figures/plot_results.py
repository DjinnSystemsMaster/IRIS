import matplotlib.pyplot as plt

def plot_logs(coherence_log, entropy_log):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.plot(coherence_log, 'g-', label='Coherence')
    ax2.plot(entropy_log, 'r--', label='Entropy')

    ax1.set_xlabel('Timestep')
    ax1.set_ylabel('Coherence', color='g')
    ax2.set_ylabel('Entropy', color='r')

    plt.title('Sullivan Channel: Entropy-Coherence Dynamics')
    plt.show()
