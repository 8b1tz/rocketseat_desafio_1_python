def menu():
    print("===== Menu =====")
    print("1. Adicionar um contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar um contato")
    print("4. Marcar/desmarcar um contato como favorito")
    print("5. Ver lista de contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")


def adicionar_contato(agenda):
    nome = input('Qual o nome do seu contato? ')
    telefone = input(f'Qual o número de telefone de {nome}? ')
    email = input(f'Qual o e-mail de {nome}? ')

    agenda.append({
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    })
    return 'Contato adicionado com sucesso!'


def adicionar_favorito(agenda):
    numero = input('Qual o número do contato que você deseja favoritar? ')
    encontrado = False
    for contato in agenda:
        if contato.get("telefone") == numero:
            contato['favorito'] = True
            encontrado = True
            break
    if encontrado:
        return 'Contato favoritado com sucesso!'
    return 'Contato não encontrado!'


def listar_favoritos(agenda):
    return [contato for contato in agenda if contato.get("favorito")]


def listar_contatos(agenda):
    return agenda


def atualizar_contato(agenda):
    numero = input('Digite o número do contato que você deseja atualizar: ')
    for contato in agenda:
        if contato.get('telefone') == numero:
            print(f'O contato é: {contato}')
            campo = input('Qual campo deseja atualizar? ')
            novo_valor = input(f'Qual novo valor para {campo}? ')
            contato[campo] = novo_valor
            return 'Contato atualizado com sucesso!'
    return 'Contato não encontrado!'


def apagar_contato(agenda):
    numero = input('Qual o número do contato que você deseja apagar? ')
    for contato in agenda:
        if contato["telefone"] == numero:
            agenda.remove(contato)
            return 'Contato removido com sucesso!'
    return 'Contato não encontrado!'


def main():
    agenda = []
    escolha = ''

    while escolha != '7':
        menu()
        escolha = input('--> ')

        opcoes = {
            "1": adicionar_contato,
            "2": listar_contatos,
            "3": atualizar_contato,
            "4": adicionar_favorito,
            "5": listar_favoritos,
            "6": apagar_contato,
        }

        if escolha in opcoes:
            print(opcoes[escolha](agenda))
        elif escolha != '7':
            print("Escolha uma opção válida. ")


if __name__ == "__main__":
    main()
