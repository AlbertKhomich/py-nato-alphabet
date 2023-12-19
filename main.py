import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_df_voc = {row[1].letter: row[1].code for row in nato_df.iterrows()}


def nato_remake():

    name = input("Enter text: ")

    try:
        code_list = [nato_df_voc[letter.upper()] for letter in name if letter != ' ']
    except KeyError as error:
        print(f"{error} is not in English Alphabet!")
        nato_remake()
    else:
        print(code_list)


nato_remake()
