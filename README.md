# Sistema de comunicação digital

Recebe uma mensagem, converte em dados binários e simula a transmissão dos dados por um canal. Recebe de volta novamente e reconstroi a mensagem.

Vídeo Sistema em Execução: https://youtu.be/S9PjqWY7q8g?si=kipOz636UEilOWhw

# Arquitetura

main.py - executa uma transmissão completa de uma mensagem de texto

binary_manipulation.py - converte ASCII para binário (e de volta) e faz o Hamming(7,4)

line_encoding.py - codificação e decodificação de linha: NRZ unipolar e Manchester

modulator.py - modulação e demodulação: ASK, BPSK e 16-QAM

channel.py - canais: AWGN e AWGN com rajadas. Controla o SNR (Eb/N0)

metrics.py - calcula a BER e mostra a posição dos bits errados

run_experiments.py - roda os experimentos e salva os resultados brutos em resultados.csv

plot_results.py - lê o resultados.csv e gera os gráficos e a tabela de compromisso

# Instruções de execução

Verifique se tem o numpy instalado através do terminal:
python -m pip show numpy
Caso contrário, instale
python -m pip install numpy

Se o código apresentar erros após instalar todas as dependências abra o terminal no main e execute 'python main.py'

Antes de executar o código altere as variáveis no início:

A - amplitude. Determina a amplitude dos sinais enviados;

APB - amostras por bit. Determina a quantidade de vezes que o mesmo sinal binário é repetido;

FP - frequência da portadora. Determina a frequência em Hz;

SNR - relação sinal-ruído. Quanto maior significa que menos ruídos ocorrerão. À medida que é diminuído aumenta a incidência de ruídos;

SEED - semente geradora de ruídos. Para evitar padrões aleatórios.

# Divisão de responsabilidades

Leonardo: binary_manipulation.py, line_encoding.py, modulator.py e main.py

Gabriel: channel.py, metrics.py, run_experiments.py, plot_results.py e o vídeo de demonstração

Vídeo Sistema em Execução: https://youtu.be/S9PjqWY7q8g?si=kipOz636UEilOWhw
