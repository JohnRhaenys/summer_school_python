class Serie:
    def __init__(self, nome, ano_lancamento, avaliacao, thumbnail_url, caminho_imagem=None, descricao=None, caminho_qr_code=None):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.avaliacao = avaliacao
        self.thumbnail_url = thumbnail_url
        self.caminho_imagem = caminho_imagem
        self.descricao = descricao
        self.caminho_qr_code = caminho_qr_code

    def __str__(self):
        return f'Nome: {self.nome}\n' \
               f'Ano lancamento: {self.ano_lancamento}\n' \
               f'Avaliacao: {self.avaliacao}\n'













