from restic.classResidente import Residente
import pandas as pd


class Residencia:
    @staticmethod
    def exibir_historico_residentes():
        data = []
        for residente in Residente.residentes:
            registro = {
                'Identificador': f'tic18{residente.turma}{residente.cpf[:3]}{residente.ano_nascimento[-2:]}',
                'Idade': residente.idade,
                'Formacao': residente.formacao,
                'Formacao Geral': residente.formacaoGeral,
                'Formacao Especifica': residente.formacaoEspecifica,
                'Andamento Graduacao': residente.andamentoGraduacao,
                'Tempo de Formado': residente.tempoFormacao,
                'Experiencia Previa': residente.experienciaPrevia,
                'Descricao Experiencia': residente.descricaoExperiencia
            }
            data.append(registro)

        # Nomeando as colunas
        columns = ['Identificador', 'Idade', 'Formacao', 'Formacao Geral', 'Formacao Especifica', 'Andamento Graduacao', 'Tempo de Formado', 'Experiencia Previa', 'Descricao Experiencia']

        # Criando o DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Exibindo o DataFrame
        print(df)

while True:
    residente = Residente()

    opcao = input('Deseja adicionar um novo residente (A) ou mostrar todos os residentes cadastrados (M)? (A/M): ').upper()
    if opcao == 'M':
        Residencia.exibir_historico_residentes()
        break
    elif opcao != 'A':
        break

@staticmethod
def salvar_dados_csv(nome_arquivo):
    data = []
    for residente in Residente.residentes:
        registro = {
            'Identificador': f'tic18{residente.turma}{residente.cpf[:3]}{residente.ano_nascimento[-2:]}',
            'Idade': residente.idade,
            'Formacao': residente.formacao,
            'Formacao Geral': residente.formacaoGeral,
            'Formacao Especifica': residente.formacaoEspecifica,
            'Andamento Graduacao': residente.andamentoGraduacao,
            'Tempo de Formado': residente.tempoFormacao,
            'Experiencia Previa': residente.experienciaPrevia,
            'Descricao Experiencia': residente.descricaoExperiencia
        }
        data.append(registro)

    columns = ['Identificador', 'Idade', 'Formacao', 'Formacao Geral', 'Formacao Especifica', 'Andamento Graduacao', 'Tempo de Formado', 'Experiencia Previa', 'Descricao Experiencia']
    df = pd.DataFrame(data, columns=columns)

    df.to_csv(nome_arquivo, index=False)
    print(f'Dados salvos no arquivo CSV: {nome_arquivo}')

@staticmethod
def carregar_dados_csv(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        Residente.residentes = []

        for _, row in df.iterrows():
            residente = Residente()
            residente.turma = row['Identificador'][4:7]
            residente.cpf = row['Identificador'][7:10]
            residente.ano_nascimento = row['Identificador'][10:]
            residente.idade = row['Idade']
            residente.formacao = row['Formacao']
            residente.formacaoGeral = row['Formacao Geral']
            residente.formacaoEspecifica = row['Formacao Especifica']
            residente.andamentoGraduacao = row['Andamento Graduacao']
            residente.tempoFormacao = row['Tempo de Formado']
            residente.experienciaPrevia = row['Experiencia Previa']
            residente.descricaoExperiencia = row['Descricao Experiencia']

        print(f'Dados carregados do arquivo CSV: {nome_arquivo}')
    except FileNotFoundError:
        print(f'Arquivo CSV não encontrado: {nome_arquivo}')

def salvar_dados_csv(nome_arquivo):
    data = []
    for residente in Residente.residentes:
        registro = {
            'Identificador': f'tic18{residente.turma}{residente.cpf[:3]}{residente.ano_nascimento[-2:]}',
            'Idade': residente.idade,
            'Formacao': residente.formacao,
            'Formacao Geral': residente.formacaoGeral,
            'Formacao Especifica': residente.formacaoEspecifica,
            'Andamento Graduacao': residente.andamentoGraduacao,
            'Tempo de Formado': residente.tempoFormacao,
            'Experiencia Previa': residente.experienciaPrevia,
            'Descricao Experiencia': residente.descricaoExperiencia
        }
        data.append(registro)

    columns = ['Identificador', 'Idade', 'Formacao', 'Formacao Geral', 'Formacao Especifica', 'Andamento Graduacao', 'Tempo de Formado', 'Experiencia Previa', 'Descricao Experiencia']
    df = pd.DataFrame(data, columns=columns)

    df.to_csv(nome_arquivo, index=False)
    print(f'Dados salvos no arquivo CSV: {nome_arquivo}')

# Adicione o método abaixo na classe 'classResidencia' em 'classResidencia.py'
@staticmethod
def carregar_dados_csv(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        Residente.residentes = []

        for _, row in df.iterrows():
            residente = Residente()
            residente.turma = row['Identificador'][4:7]
            residente.cpf = row['Identificador'][7:10]
            residente.ano_nascimento = row['Identificador'][10:]
            residente.idade = row['Idade']
            residente.formacao = row['Formacao']
            residente.formacaoGeral = row['Formacao Geral']
            residente.formacaoEspecifica = row['Formacao Especifica']
            residente.andamentoGraduacao = row['Andamento Graduacao']
            residente.tempoFormacao = row['Tempo de Formado']
            residente.experienciaPrevia = row['Experiencia Previa']
            residente.descricaoExperiencia = row['Descricao Experiencia']

        print(f'Dados carregados do arquivo CSV: {nome_arquivo}')
    except FileNotFoundError:
        print(f'Arquivo CSV não encontrado: {nome_arquivo}')