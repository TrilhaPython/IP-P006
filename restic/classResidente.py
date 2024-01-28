class Residente:
    residentes = []  # Lista para armazenar todos os residentes

    def __init__(self):
        # Coletando dados do usuário
        trilhas_validas = ['Python', 'Net', 'Jav']

        while True:
            self.turma = input('Digite a turma (Python, Net ou Jav): ').capitalize()

            if self.turma not in trilhas_validas:
                print('Trilha incorreta. Tente novamente.')
            else:
                break

        self.cpf = input('Digite os 11 dígitos do seu CPF: ')

        # Verificando ano de nascimento
        self.ano_nascimento = input('Digite os 4 dígitos do seu ano de nascimento: ')
        while not self.ano_nascimento.isdigit() or len(self.ano_nascimento) != 4:
            print('O ano de nascimento deve ser no formato aaaa. Digite novamente.')
            self.ano_nascimento = input('Digite os 4 dígitos do seu ano de nascimento: ')

        self.idade = int(input('Digite sua idade: '))

        # Verificando idade
        while self.idade != 2024 - int(self.ano_nascimento) and self.idade != 2023 - int(self.ano_nascimento):
            print('A idade não confere com o ano de nascimento. Tente novamente.')
            self.idade = int(input('Digite sua idade: '))

        self.formacao = int(input('Digite sua área de formação (0.Engenharia, 1.Computação ou 2.SemFormação): '))
        self.formacaoGeral = int(input('Digite sua formação geral (0.Engenharia, 1.Computação ou 2.SemFormação): '))

        # Coletando formação específica com base na formação geral
        if self.formacaoGeral == 0:  # Engenharia
            self.formacaoEspecifica = input('Digite sua formação específica (Engenharia): ')
        elif self.formacaoGeral == 1:  # Computação
            self.formacaoEspecifica = input('Digite sua formação específica (Computação): ')
        else:
            self.formacaoEspecifica = 'Sem formação.'

        # Coletando andamento da graduação ou tempo de formado (excludentes)
        self.andamentoGraduacao = None
        self.tempoFormacao = None
        opcao = input('Você está atualmente em andamento na graduação? (S/N): ').upper()
        if opcao == 'S':
            self.andamentoGraduacao = float(input('Digite o percentual da graduação concluído: '))
        else:
            self.tempoFormacao = int(input('Digite seu tempo de formado (em anos): '))

        self.experienciaPrevia = input('Você possui experiência prévia em programação? (S/N): ').upper() == 'S'

        # Incluindo descrição da experiência (se houver)
        self.descricaoExperiencia = None
        if self.experienciaPrevia:
            self.descricaoExperiencia = input('Descreva sua experiência em até 15 caracteres: ')[:15]

        # Adicionando o residente à lista de residentes
        Residente.residentes.append(self)

    def adicionar_residente(self):
        # Adicionar a lógica para adicionar o residente se necessário
        pass
