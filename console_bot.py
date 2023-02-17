import re

# ================================= Decorator ================================#


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"<{args[0]}> does not appear in list"
        except ValueError:
            return "Give me a name and phone, please"

    return wrapper


# ================================== handlers ================================#


def hello(*args):
    return "How can I help you?"


def good_bye(*args):
    return False


def undefined(*args):
    return "What do you mean?"


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
        return f"I add contact for <{args[0]}> with phone <{args[1]}>"
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
    return COMMANDS.get(command, undefined)


# ================================ main function =============================#


def main():

    pattern = re.compile(
        r"^[a-zA-Z\s,!?]*(hello|add|change|phone|show all|good bye|close|exit)\s*(\w*)\s*(\d*)",
        re.IGNORECASE,
    )

    while True:

        # waiting for nonempty input
        while True:
            inp = input(">>> ").strip()
            if inp == "":
                continue
            break

        text = pattern.search(inp)

        params = (
            tuple(
                map(
                    # Made a commands to be a uppercase
                    lambda x: x.lower() if text.groups().index(x) == 0 else x,
                    text.groups(),
                )
            )
            if text
            else (None, 0, 0)
        )
        handler = get_handler(params[0])
        response = handler(params[1], params[2])
        if response is False:
            print("Good bye!")
            break
        print(response)


contacts = {}  # Global variable for storing contacts


# ================================ main programm =============================#

if __name__ == "__main__":

    main()
