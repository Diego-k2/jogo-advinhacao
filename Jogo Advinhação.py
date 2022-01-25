palavra = input("Digite a palavra secreta: ").lower()
digitado = []
chances = len(palavra) + 3


print(F"A palavra secreta tem {len(palavra)} letras.")

while chances >= 0:
    letra = input("Digite uma letra: ").lower()
    if len(letra) > 1:
        print("Isso nao vale, digite apenas uma letra")
        continue
    digitado.append(letra)
    print(digitado)

    if letra in palavra:
        print(F"A letra '{letra}' existe na palavra secreta.")
    else:
        print(F"A letra '{letra}' não existe na palavra secreta.")
        digitado.pop()

    secreto_temporario = ""
    for letra_secreta in palavra:
        if letra_secreta in digitado:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"
    print(secreto_temporario)

    if secreto_temporario == palavra:
        print("Voce acertou !!!!")
        break

    chances -= 1
    print(F"Você ainda tem {chances} chances")


