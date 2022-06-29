#! python

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        b = a + b
        yield b
        a = a + b


sequencia_fibonacci = [0, 1]

f = fibonacci()

x = int(input("Digite o valor: "))

while True:
    if x in sequencia_fibonacci:
        print(f"Contém {x} na sequência ")
        print(sequencia_fibonacci)
        break
    elif sequencia_fibonacci[-1] > x:
        print(f"Não contém {x} na sequência")
        proximo = sequencia_fibonacci.pop()
        print(sequencia_fibonacci)
        print(f"Próximo número da sequência é: {proximo}")
        break
    else:
        sequencia_fibonacci.append(next(f))
