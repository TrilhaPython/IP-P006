from restic.classResidente import Residente
from restic.classResidencia import Residencia
from restic.classTrilha import Trilha

import pandas as pd

def main():
    print('>>>SISTEMA DE CADASTRO DE RESIDENTES<<<')
    residencia = Residencia()  # Crie um objeto da classe Residencia

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar novo residente")
        print("2. Mostrar todos os residentes cadastrados")
        print("3. Gerar DataFrame por trilha")
        print("4. Salvar dados em CSV")
        print("5. Carregar dados de CSV")
        print("6. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            residente = Residente()
            residente.adicionar_residente()
        elif opcao == "2":
            Residencia.exibir_historico_residentes(residente)  # Passe o objeto 'residente' como argumento
        elif opcao == "3":
            trilha = input("Digite a trilha (Python, Net ou Jav): ").capitalize()
            Trilha.gerar_dataframe_por_trilha(trilha)
        elif opcao == "4":
            nome_arquivo = input("Digite o nome do arquivo CSV para salvar os dados: ")
            residente.salvar_dados_csv(nome_arquivo)  # Chame o método no objeto residente
        elif opcao == "5":
            nome_arquivo = input("Digite o nome do arquivo CSV para carregar os dados: ")
            residencia.carregar_dados_csv(nome_arquivo)  # Chame o método no objeto residencia
        elif opcao == "6":
            print("Sistema encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
