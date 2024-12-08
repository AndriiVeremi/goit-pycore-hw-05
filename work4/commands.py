from decorators import input_error

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Expected 2 arguments: name and phone.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Expected 2 arguments: name and new phone.")
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated."
    else:
        raise KeyError(f"{name} not found.")

@input_error
def show_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Expected 1 argument: name.")
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        raise KeyError(f"{name} not found.")

@input_error
def show_all_contact(contacts):
    if not contacts:
        return "No contacts saved."
    else:
        result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return result

@input_error
def delete_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Expected 2 arguments: name and phone.")
    name, phone = args
    if name in contacts and contacts[name] == phone:
        del contacts[name]
        return "Contact deleted."
    else:
        raise KeyError(f"{name} not found.")
