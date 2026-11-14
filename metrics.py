def ber(bits_tx, bits_rx):
    erros = bits_tx != bits_rx
    return erros.mean(), np.flatnonzero(erros)

EFICIENCIA = {"ASK": 1, "BPSK": 1, "QPSK": 2, "16QAM": 4}