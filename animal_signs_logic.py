import nltk
import csv

FILE_NAME = "zoo.csv"


# read csv file
def read_csv(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        return list(reader)


def get_header():
    return read_csv(FILE_NAME)[0]


def get_animals(feature):
    animals = read_csv(FILE_NAME)
    found_animals = []
    feature_number = get_header().index(feature)
    for animal in animals:
        if animal[feature_number] == "1":
            found_animals.append(animal[0])
    return found_animals



# find word synonyms
def find_synonyms(word):
    synonyms = []
    for syn in nltk.corpus.wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)

