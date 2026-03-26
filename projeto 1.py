meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "BLZ":  "a pessoa afirma que esta ok",
            "MANO": "jeito informal de charmar alguem",
            "MEME": "alguma situacao(print,video ou momento)que e considerada muita engracada ",
            "KKK": "a pessoa esta rindo",
            }

word = input("Digite uma palavra moderna que você não entende (escreva toda a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    # O que devemos fazer se a palavra for encontrada?
else:
    # O que devemos fazer se a palavra não for encontrada?
    print("nao encontrei a palavra")
