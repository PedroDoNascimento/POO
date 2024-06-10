class calc:
    def somar(self, a , b):
        return a + b
    def subtrair(self, a , b):
        return a - b
    def multiplicar(self, a , b):
        return a * b
    def dividir(self, a , b):
        return a / b

calc = calc()
print(calc.somar(10, 5)) 
res = calc.subtrair(5, 10)
print(res)
