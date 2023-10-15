def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Not enough data. Please enter correctly again"
    else:
        if name in contacts.keys():
            contacts[name] = phone
            return "Such a contact with this name already exists. Contact updated"
        else:
            contacts[name] = phone
            return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Not enough data. Please enter correctly again"
    else:
        if name in contacts.keys():
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Error! Name not found."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts.keys():
        return contacts[name]
    else:
        return "Error! Name not found."

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")



if __name__ == "__main__":
    pass