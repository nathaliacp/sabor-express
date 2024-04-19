import os

restaurantes = [{
  "nome": "Praça",
  "categoria": "Japonesa",
  "ativo": False
  }, {
    "nome": "Pizza Suprema",
    "categoria": "Pizza",
    "ativo": True
  }, {
    "nome": "Cantina",
    "categoria": "Italiano",
    "ativo": False
  }]


def exibir_nome_do_programa():
    """Essa função é responsável por exibir o nome estilizado no
    início do programa"""
    print("""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

        ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)


def exibir_opcoes():
    """Essa função é responsável por exibir as opções disponíveis
    no menu
    """
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alterar estado do restaurante")
    print("4. Sair\n")


def finalizar_app():
    """Essa função é responsável por exibir uma mensagem
    de finalização da aplicação"""
    exibir_subtitulo("Finalizando o app")


def voltar_ao_menu_principal():
    """Essa função é responsável por solicitar uma tecla
    para retornar ao menu principal

    Outputs:
    - Retorna ao menu principal
    """
    input("\nDigite uma tecla para voltar ao menu: ")
    main()


def opcao_invalida():
    """Essa função é responsável por exibir uma mensagem de opção
    inválida e retorna ao menu principal

    Outputs:
    - Retorna ao menu principal
    """
    print("Opção Inválida!\n")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    """Essa função é responsável por exibir um subtítulo estilizado
    na tela

    Inputs:
    - texto: str - texto do subtítulo
    """
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(f"{linha}\n")


def cadastrar_novo_restaurante():
    """Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante na lista de restaurantes
    """
    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite o nome da categoria do {nome_do_restaurante}: ")

    dados_do_restaurante = {
      "nome": nome_do_restaurante,
      "categoria": categoria,
      "ativo": False
    }
    restaurantes.append(dados_do_restaurante)

    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()


def listar_restaurantes():
    """Essa função mostra uma lista de todos os restaurantes
    formatada de acordo com as propriedades do dicionário restaurante

    Outputs:
    - Exibe a lista de restaurantes na tela
    """
    exibir_subtitulo("Listando os restaurantes")

    print(f"{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(18)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(18)} | {categoria.ljust(18)} | {ativo}")

    voltar_ao_menu_principal()


def alterar_estado_restaurante():
    """Essa funçao altera o estado do restaurante caso ele seja 
    encontrado na lista

    Inputs:
    - Nome do restaurante

    Output:
    - Mensagem que indica se o restaurante foi ativado/desativado
    - Mensagem que indica que o restaurante não foi encontrado
    """
    exibir_subtitulo("Alterando estado do restaurante")

    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado!")

    voltar_ao_menu_principal()


def escolher_opcoes():
    """Essa função é responsável por solicitar e executar
    a opção escolhida pelo usuário

    Outputs:
    - Executa a opção escolhida pelo usuário
    """
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()

    except:
        opcao_invalida()


def main():
    """Essa função é responsável por iniciar o programa"""
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()
