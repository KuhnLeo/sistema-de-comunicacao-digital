import csv
import numpy as np

import modulator as mod
from channel import awgn

# parâmetros
N_BITS = 100_000                   
EBN0_DB = [0, 2, 4, 6, 8, 10, 12, 14]   
SEMENTES = [0, 1, 2, 3, 4]         
A, APB, FP = 1.0, 16, 2        

t = np.arange(N_BITS * APB) / APB  

with open("resultados.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["tecnica", "ebn0_db", "semente", "n_bits", "erros", "ber"])

    for ebn0 in EBN0_DB:
        for semente in SEMENTES:
            rng = np.random.default_rng(semente)

            bits = rng.integers(0, 2, N_BITS)                 #gera bits aleatórios
            tx = mod.bpsk(bits, A, APB, FP, t)                #modula
            rx = awgn(tx, ebn0, N_BITS, rng)                  #passa pelo canal
            bits_rx = mod.demo_bpsk(rx, A, APB, FP, t)        #demodula

            erros = int(np.sum(bits != bits_rx))              #conta erros
            w.writerow(["BPSK", ebn0, semente, N_BITS, erros, erros / N_BITS])
            print(f"BPSK Eb/N0={ebn0} dB semente={semente} BER={erros / N_BITS:.5f}")