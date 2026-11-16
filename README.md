# Sistema de comunicação digital
Recebe uma mensagem, converte em dados binários e simula a transmissão dos dados por um canal. Recebe de volta novamente e reconstroi a mensagem.

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
