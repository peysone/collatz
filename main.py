"""
Ciąg Collatza zdefiniowany jest następująco:
Rozpoczynamy od podanej ze standardowego wejścia liczby x (od 1 do 100).
Jeśli x jest liczbą parzystą, to kolejny wyraz ciągu będzie obliczony jako x/2.
W przeciwnym przypadku kolejny wyraz ciągu będzie równy 3x+1.
W ten sam sposób obliczamy kolejne wyrazy ciągu, aż pojawi się liczba 1.

Napisz program, który wypisze długość ciągu Collatza dla podanego ze standardowego wejścia x.
X może przyjmować wartości od 1 do 100.
"""

def collatz(x):
    length = 1
    while True:
        if x == 1:
            break
        elif x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        length += 1
    return length

x = int(input("Podaj liczbę x (1-100): "))

if x >= 1 and x <= 100:
    length = collatz(x)
    print(f"Długość ciągu Collatza dla liczby {x} to {length}.")
else:
    print("Liczba x powinna być z zakresu 1-100.")
