word =input("Digitare la parola:")
word1 = word[::-1] #comando che gira la stringa
if word == word1:
    print(word, "E un palindromo")
else:
    print(word, "Non e un palindromo")