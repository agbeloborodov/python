

def thesaurus(*names):
    """ The function generates a list of employees from the passed parameters. The key is the first letter of the employee's name. """
    new_refbook = {}
    for item in names:
        first_symbol = item[0].upper()
        new_refbook[first_symbol] = new_refbook.setdefault(first_symbol, []) + [item.capitalize()]
    return new_refbook

print(thesaurus("Яков", "Иван", "Лилит", "Михаил", "Мария", "Петр", "Илья", "Ольга"))


