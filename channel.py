import numpy as np

def _sigma(sinal, ebn0_db, n_bits):
    ebn0 = 10 ** (ebn0_db / 10)
    ps = np.mean(sinal ** 2)
    amostras_bit = len(sinal) / n_bits
    return np.sqrt(ps * amostras_bit / (2 * ebn0))

def awgn(sinal, ebn0_db, n_bits, rng):
    sigma = _sigma(sinal, ebn0_db, n_bits)
    return sinal + sigma * rng.standard_normal(len(sinal))

def awgn_rajadas(sinal, ebn0_db, n_bits, rng, bloco, p_gb=0.01, p_bg=0.2, fator_ruim=5.0):
    sigma = _sigma(sinal, ebn0_db, n_bits)
    n_blocos = int(np.ceil(len(sinal) / bloco))
    u = rng.random(n_blocos)
    ruim = np.zeros(n_blocos, dtype=bool)
    for i in range(1, n_blocos):
        ruim[i] = (u[i] >= p_bg) if ruim[i - 1] else (u[i] < p_gb)
    sigma_amostra = np.where(np.repeat(ruim, bloco)[:len(sinal)],
                             sigma * fator_ruim, sigma)
    return sinal + sigma_amostra * rng.standard_normal(len(sinal))

