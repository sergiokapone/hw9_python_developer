import re


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return f"{args[0]} does not appear in list"
        except ValueError:
            return "Give me name and phone please"

    return inner


def hello(*args):
    return "How can I help you?"


def good_bye(*args):
    return False


def show_all(*args):
    for k, v in contacts.items():
        print(f"{k}: {v}")
    return f"List contain {len(contacts)} contacts"


@input_error
def get_phone(*args):
    return contacts[args[0]]


def undefined(*args):
    return "What do you mean?"


@input_error
def add_contact(*args):
    if args[1]:
        contacts[args[0]] = args[1]
        return f"I add contact for <{args[0]}> with value <{args[1]}>"
    else:
        raise ValueError


def parse_input(user_input):
    return list(filter(lambda item: item != "", user_input.split(" ")))


contacts = {}


def get_handler(command, *ars):
    COMMANDS = {
        "hello": hello,
        "add": add_contact,
        "change": add_contact,
        "phone": get_phone,
        "show all": show_all,
        "good bye": good_bye,
        "close": good_bye,
        "exit": good_bye,
        "": undefined,
    }
    return COMMANDS[command]


def get_pattern():
    pattern = re.compile(
        r"^[a-zA-Z\s,!?]*(hello|add|change|phone|show all|good bye|close|exit)\s*(\w*)\s*(\d*)"
    )
    text = pattern.search(input(">>> "))
    if text is None:
        return ("", "", "")
    return text.groups()


def main():

    while True:
        pattern = get_pattern()
        handler = get_handler(pattern[0])
        response = handler(pattern[1], pattern[2])
        if response is False:
            print("Good bye!")
            break
        print(response)


if __name__ == "__main__":

    main()
