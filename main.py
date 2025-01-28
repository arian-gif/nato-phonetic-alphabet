import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {}
for (index, row) in data.iterrows():
    nato[row.letter.lower()]= row.code

isLetters = False
code_words=""
while not isLetters:
    try:
        word = input("Enter word:\n")
        code_words = [nato[letter] for letter in word]
        isLetters=True
    except KeyError:
        print("Please Enter letters only")
    else:
        print(code_words)