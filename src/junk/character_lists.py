
import src.data.character as ch

character_list = []

def add(someone):
    if someone.get_name() not in names():
        character_list.append(someone)

def get(name):
    marked: ch.character
    for character in character_list:
        if character.get_name() == name:
            marked = character
    return marked

def remove(name):
    marked: ch.character
    for character in character_list:
        if character.get_name() == name:
            marked = character
    character_list.remove(marked)

def names():
    names = []
    for character in character_list:
        names.append(character.get_name())
    return names

def test():
    add(ch.character("harley"))
    add(ch.character("harley"))
    add(ch.character("fred"))
    add(ch.character("remove me"))
    remove("remove me")
    print(get("harley"))
    for character in character_list:
        print(character)

test()