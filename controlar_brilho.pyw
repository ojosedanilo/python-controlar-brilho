import screen_brightness_control as sbc
from configparser import ConfigParser
from time import sleep
from os import path, chdir

# Pega o nome do arquivo do script e o converte em um caminho absoluto
abspath = path.abspath(__file__)
# Extrai o diretório desse caminho
dname = path.dirname(abspath)
# Muda o diretório de trabalho atual para o diretório do arquivo
chdir(dname)

# Cria um objeto ConfigParser para ler o arquivo de condigurações
config = ConfigParser()

# Valor inicial para o brilho máximo permitido
max_brightness = 70
# Intervalo inicial (em segundos) para checar o brilho
recheck_time_seconds = 60


while True:
    # Espera o tempo definido antes de verificar o brilho novamente
    sleep(recheck_time_seconds)

    # Se o brilho atual for maior que o máximo permitido, ajusta para o valor máximo
    if sbc.get_brightness(display=0)[0] > max_brightness:
        print(f"{sbc.get_brightness(display=0)[0]}% -> {max_brightness}%")
        sbc.set_brightness(max_brightness, display=0)

    try:
        # Lê as configurações do arquivo "controlar_brilho_settings.ini"
        config.read("controlar_brilho_settings.ini")
        max_brightness = config.getint("controlar_brilho_settings", "max_brightness")
        recheck_time_seconds = config.getint(
            "controlar_brilho_settings", "recheck_time_seconds"
        )
    except:
        pass
