import random


def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        print("ERROR")
        return
    splitter_text = text.split(sep)
    new_array = []
    if not option:
        for element in splitter_text:
            yield element
        return
    elif option == "shuffle":
        new_array = random.sample(splitter_text, len(splitter_text))
    elif option == "unique":
        for x in splitter_text:
            if x not in new_array:
                new_array.append(x)
    elif option == "ordered":
        new_array = sorted(splitter_text)
    if not new_array:
        print("ERROR")
        return
    for element in new_array:
        yield element


text = "Le Lorem Ipsum est simplement du faux texte Le ."
for word in generator(text, sep=" "):
    print(word)
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
for word in generator(text, sep=" ", option="ordered"):
    print(word)
for word in generator(text, sep=" ", option="unique"):
    print(word)
