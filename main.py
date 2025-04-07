from sim.run_simulation import simulate
from figures.plot_results import plot_logs

if __name__ == "__main__":
    coherence_log, entropy_log = simulate()
    plot_logs(coherence_log, entropy_log)
