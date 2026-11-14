import numpy as np
from math import erfc, sqrt
from channel import awgn
from metrics import ber

rng = np.random.default_rng(0)
n_bits, apb, fp = 100_000, 16, 2          # fp = ciclos da portadora por bit
t = np.arange(n_bits * apb) / apb          # tempo em unidades de bit

bits = rng.integers(0, 2, n_bits)
fase = np.repeat(np.where(bits == 1, 0, np.pi), apb)
tx = np.sin(2 * np.pi * fp * t + fase)     # BPSK

portadora = np.sin(2 * np.pi * fp * t)
for ebn0_db in range(0, 9, 2):
    rx = awgn(tx, ebn0_db, n_bits, rng)
    corr = (rx * portadora).reshape(n_bits, apb).sum(axis=1)   # demodulação por correlação
    bits_rx = (corr > 0).astype(int)
    b, _ = ber(bits, bits_rx)
    teorico = 0.5 * erfc(sqrt(10 ** (ebn0_db / 10)))           # Q(sqrt(2 Eb/N0))
    print(f"Eb/N0={ebn0_db} dB  simulado={b:.4f}  teórico={teorico:.4f}")