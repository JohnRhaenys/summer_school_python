import os
import urllib.request
import qrcode
from youtube_search import YoutubeSearch
import webbrowser
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


from ETAPA_03.desafio_01.constants import ROOT_PATH
from ETAPA_03.desafio_01.src.models.serie import Serie


def get_lista_de_series():

    lista_de_series = []
    caminho_arquivo = f'{os.path.join(ROOT_PATH, "series.html")}'

    with open(caminho_arquivo, 'r') as arquivo:
        for line in arquivo:

            if line.strip() == '<td class="posterColumn">':
                skip_lines(arquivo, 6)

                line = arquivo.readline()
                id = line[line.find('IMDb_files') + len('IMDb_files') + 1:line.rfind('.jpg"') + 4]
                thumbnail_url = f'https://m.media-amazon.com/images/M/{id}"'

            if line.strip() == '<td class="titleColumn">':
                arquivo.readline()
                line = arquivo.readline()
                posicao_final = line.rfind('<')
                tmp = line[:-2]
                posicao_inicial = tmp.rfind('>')

                # Nome
                nome_serie = tmp[posicao_inicial + 1:posicao_final]

                line = arquivo.readline()

                # Ano lancamento
                ano_lancamento = line[line.find('(') + 1:line.rfind(')')]

                arquivo.readline()
                arquivo.readline()

                line = arquivo.readline()

                posicao_final = line.rfind('<')
                tmp = line[:-2]
                posicao_inicial = tmp.rfind('>')

                # Avaliacao
                avaliacao = tmp[posicao_inicial + 1:posicao_final]

                objeto_serie = Serie(nome_serie, ano_lancamento, avaliacao, thumbnail_url)

                lista_de_series.append(objeto_serie)

    return lista_de_series


def skip_lines(file, lines_to_skip):
    for i in range(lines_to_skip):
        file.readline()


def save_image_file(serie, caminho_destino):
    caminho_thumbnail = os.path.join(caminho_destino, 'logo.jpg')
    urllib.request.urlretrieve(serie.thumbnail_url, caminho_thumbnail)


def generate_qr_code(serie, caminho_destino):

    detalhes = {
        'nome': serie.nome,
        'lancamento': serie.ano_lancamento,
        'avaliacao': serie.avaliacao
    }

    img = qrcode.make(detalhes)
    img.save(os.path.join(caminho_destino, 'qr_code.jpg'))


# Abrir microfone
import speech_recognition


def talk(string):
    tts = gTTS(string, lang='pt')
    tts.save('temp.mp3')
    sound = AudioSegment.from_file('temp.mp3')
    play(sound)


def ouvir_microfone():
    # Habilitar o microfone
    microfone = speech_recognition.Recognizer()

    # Utilizar o microfone
    with speech_recognition.Microphone() as source:

        # Reduzir ruido
        microfone.adjust_for_ambient_noise(source)

        print('AQUI 1')
        talk('Pode falar')

        # Ouvir
        audio = microfone.listen(source, timeout=5)

        try:

            frase = microfone.recognize_google(audio, language='pt-BR')

            resultados = YoutubeSearch(frase, max_results=1).to_dict()

            BASE_URL = 'https://www.youtube.com'
            id_video = resultados[0].get('url_suffix')
            url_video = f'{BASE_URL}{id_video}'

            talk(f'Ok. Buscando o video {frase}')

            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open(url_video)

        except speech_recognition.UnknownValueError:
            print('Nao entendi')
            return None

# Abrir a URL

ouvir_microfone()

