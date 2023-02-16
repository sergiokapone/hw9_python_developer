import re

# ================================= Decorator ================================#


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return f"<{args[0]}> does not appear in list"
        except ValueError:
            return "Give me a name and phone please"

    return inner


# ================================== handlers ================================#


def hello(*args):
    return "How can I help you?"


def good_bye(*args):
    return False


def show_all(*args):
    for k, v in contacts.items():
        print(f"{k}: {v}")
    return f"List contain <{len(contacts)}> contacts"


@input_error
def get_phone(*args):
    return contacts[args[0]]


@input_error
def add_contact(*args):
    if args[0] and args[1]:
        contacts[args[0]] = args[1]
        return f"I add contact for <{args[0]}> with value <{args[1]}>"
    else:
        raise ValueError


@input_error
def change_contact(*args):
    if contacts.get(args[0]):
        contacts[args[0]] = args[1]
        return f"I change contact for <{args[0]}> to value <{args[1]}>"
    else:
        raise ValueError


# =============================== handler loader =============================#


def get_handler(command, *ars):
    COMMANDS = {
        "hello": hello,
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "show all": show_all,
        "good bye": good_bye,
        "close": good_bye,
        "exit": good_bye,
    }
    return COMMANDS[command]


# ================================ main function =============================#


def main():

    pattern = re.compile(
        r"^[a-zA-Z\s,!?]*(hello|add|change|phone|show all|good bye|close|exit)\s*(\w*)\s*(\d*)"
    )

    while True:
        try:
            text = pattern.search(input(">>> "))
            handler = get_handler(*text.groups())
            response = handler(text.group(2), text.group(3))
            if response is False:
                print("Good bye!")
                break
            print(response)
        except AttributeError:
            print("What do you mean?")


contacts = {}  # Global variable for storing contacts


# ================================ main programm =============================#

if __name__ == "__main__":

    main()
