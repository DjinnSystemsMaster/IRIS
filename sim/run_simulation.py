import numpy as np
from model.recursive_agent import RecursiveAgent
from metrics.coherence import compute_coherence
from metrics.entropy import compute_entropy

def simulate():
    agent = RecursiveAgent(freeze_threshold=1.5)
    timesteps = 100
    noise_schedule = {i: 1.5 for i in range(0, timesteps, 20)}

    coherence_log = []
    entropy_log = []

    for t in range(timesteps):
        input_signal = np.random.rand()
        entropy = noise_schedule.get(t, 0.1)
        output = agent.update(input_signal, entropy)
        coherence_log.append(compute_coherence(agent.history))
        entropy_log.append(entropy)

    return coherence_log, entropy_log

if __name__ == "__main__":
    c_log, e_log = simulate()
    print("Simulation complete. Final coherence:", c_log[-1])
