from restic.classResidente import Residente
from restic.classResidencia import Residencia
from restic.classTrilha import Trilha

def main():
    print('>>>SISTEMA DE CADASTRO DE RESIDENTES<<<')
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar novo residente")
        print("2. Mostrar todos os residentes cadastrados")
        print("3. Gerar DataFrame por trilha")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            residente = Residente()
            residente.adicionar_residente()
        elif opcao == "2":
            Residencia.exibir_historico_residentes()
        elif opcao == "3":
            trilha = input("Digite a trilha (Python, Net ou Jav): ").capitalize()
            Trilha.gerar_dataframe_por_trilha(trilha)
        elif opcao == "4":
            print("Sistema encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
