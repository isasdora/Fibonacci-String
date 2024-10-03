def fibonacci(num):
    if num < 0:
        return False 
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

num = int(input("Informe um número para verificar se pertence a sequência de Fibonacci: "))

if fibonacci(num):
    print(f"O número {num} pertence a sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence a sequência de Fibonacci.")