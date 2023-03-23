with open('assets/make-a-game.txt') as new_file:
    new_context = new_file.read()

print(new_context)


def welcome():
    print("""
    Welcome to Make a Make A Video Game
    
    When you start the game you will be asked to enter in word 'like' adjectives or nouns
    enter after you enter in all the words them game will be created!
    
    enter start to get started!
          """
          )


def prompts():
    if new_context == "Adjective":
        input("Enter a Adjective: ")
    elif new_context == "Noun":
        input("Enter a Noun: ")

    else:
        input("working on it: ")


def strip_brackets():
    names = []
    stripped_template = ""

    i = 0
    while i < len(new_context):
        if new_context[i] == "{":
            j = i + 1
            while j < len(new_context) and new_context[j] != "}":
                j += 1

                if j < len(new_context) and new_context[j] == "}":

                    new_names = new_context[i + 1:j]
                    names.append(new_context[i + 1:j])
                    stripped_template += input(f"Enter {new_names}: ")
                    i = j + 1
                    continue

        stripped_template += new_context[i]
        i += 1

    print(stripped_template)
    with open('assets/make-a-game-copy.txt', 'w') as copy_file:
        copy_file.write(stripped_template)
    return stripped_template


def read_template(file_name):
    with open(file_name) as file:
        context = file.read()
        return context


def parse_template(template):
    placeholder_names = []
    stripped_template = ""

    i = 0
    while i < len(template):
        if template[i] == "{":
            j = i + 1
            while j < len(template) and template[j] != "}":
                j += 1

            if j < len(template) and template[j] == "}":
                placeholder_names.append(template[i+1:j])
                stripped_template += "{}"
                i = j + 1
                continue

        stripped_template += template[i]
        i += 1

    return stripped_template, tuple(placeholder_names)


def merge(template, word):
    add_words = template.format(word[0], word[1], word[2])
    return add_words


welcome()
strip_brackets()
