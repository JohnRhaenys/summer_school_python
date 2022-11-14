"""
Você foi contratado para fazer um sistema que armazena informacoes de series de televisao.

O cliente quer que você armazene os seriados dentro de uma pasta local no computador com o
nome "Seriados".

Voce deve criar uma pasta no computador PARA CADA seriado. O nome da pasta sera o nome da propria serie,
e dentro dela sera guardada a imagem da serie e um arquivo .txt contendo as seguintes informacoes:

1) Nome da série
2) Ano de lançamento
3) Avaliação
4) Imagem do seriado
5) Descricao da serie
6) Link para os detalhes completos sobre a serie
7) Imagem QR Code contendo os detalhes resumidos da serie


Além disso, o cliente quer que você crie funcionalidades de ordenar as séries por nome (ordem alfabetica),
por ano de lançamento e por avaliação.

Ah, e como o cliente esta pagando bem, também quer que seja possível pesquisar séries
por nome (nomes parecidos), por ano (todas as séries lançadas em 2017, por exemplo), e por avaliação.

Por fim, o cliente também ofereceu pagamento de hora extra para realizar uma outra atividade.
Dessa vez, ele quer um sistema de reconhecimento de voz. Ao falar um comando especifico,
o sistema deve reconhecer o comando e executa-lo.

Os comandos sao os seguintes:

- "Trailer <nome da serie>". -> Esse comando deve abrir um video do youtube para visualizacao do trailer
da mesma

- "Detalhes <nome da serie>" -> Ao dizer esse comando, o sistema devera falar, em voz alta,
o conteudo presente no arquivo de detalhes da serie

OBS: O conteudo original esta em ingles. Portanto, deve ser traduzido antes de ser apresentado

O site é https://www.imdb.com/chart/toptv
"""
import os

from ETAPA_03.desafio_01.constants import ROOT_PATH
from ETAPA_03.desafio_01.src.utils.utils import get_lista_de_series, save_image_file, generate_qr_code


def main():
    lista_series = get_lista_de_series()

    for serie in lista_series:
        nome_serie = serie.nome.replace(' ', '_')
        caminho_pasta = f'{os.path.join(ROOT_PATH, "storage", nome_serie)}'
        # save_image_file(serie, caminho_pasta)
        # generate_qr_code(serie, caminho_pasta)


if __name__ == '__main__':
    main()
