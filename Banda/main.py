from musico import Musico
from banda import Banda
from album import Album

# Função para exibir opções do menu
def exibir_menu():
    print("\nOpções:")
    print("1. Adicionar músico")
    print("2. Remover músico")
    print("3. Adicionar álbum")
    print("4. Remover álbum")
    print("0. Sair")

# Criando a nova banda
nome_banda = input("Digite o nome da banda: ")
banda = Banda(nome_banda)

# Menu de Opções
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_musico = input("Digite o nome do músico: ")
        instrumento = input("Digite o instrumento do músico: ")
        musico = Musico(nome_musico, instrumento)
        banda.adicionar_musico(musico)
        print(f"Músico {nome_musico} adicionado com sucesso!")

    elif opcao == "2":
        for musico in banda.musicos:
            print()
        nome_musico = input("Digite o nome do músico a ser removido: ")
        
        for musico in banda.musicos:
            if musico.nome == nome_musico:
                banda.remover_musico(musico)
                print(f"Músico {nome_musico} removido com sucesso!")
                break
        else:
            print(f"Músico {nome_musico} não encontrado na banda.")

    elif opcao == "3":
        titulo_album = input("Digite o título do álbum: ")
        ano_lancamento = input("Digite o ano de lançamento do álbum: ")
        album = Album(titulo_album)
        banda.adicionar_album(album)
        print(f"Álbum {titulo_album} adicionado com sucesso!")

    elif opcao == "4":
        titulo_album = input("Digite o título do álbum a ser removido: ")
        for album in banda.albums:
            if album.titulo == titulo_album:
                banda.remover_album(album)
                print(f"Álbum {titulo_album} removido com sucesso!")
                break
        else:
            print(f"Álbum {titulo_album} não encontrado na banda.")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
