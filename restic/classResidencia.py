from classResidencia import Residente
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