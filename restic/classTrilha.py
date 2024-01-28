from restic.classResidente import Residente
import pandas as pd

class Trilha:
    @staticmethod
    def mostrar_residentes_por_trilha(trilha):
        trilha_residentes = [residente for residente in Residente.residentes if trilha.lower() in residente.turma.lower()]
        
        if not trilha_residentes:
            print(f'Nenhum residente encontrado na trilha {trilha}.')
            return

        data = []
        for residente in trilha_residentes:
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
