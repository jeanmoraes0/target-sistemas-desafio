#! python

def inverter_string(string):
    if len(string) == 0:
        return string
    else:
        return inverter_string(string[1:]) + string[0]


string = input("Entre com a string: ")

print(f"String original: {string}")
print(f"String invertida: {inverter_string(string)}:")

""""
Metodo pythonico para inverter string

print(f"String original: {string}")
print(f"String invertida: {string[::-1]}:")

"""
