import tkinter as tk
import math

class CalculadoraCientifica:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica")

        self.entrada = tk.Entry(master, width=40)
        self.entrada.grid(row=0, column=0, columnspan=5)

        self.criar_botoes()

    def criar_botoes(self):
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('exp', 5, 3),
            ('log', 6, 0), ('C', 6, 1)
        ]

        for (texto, linha, coluna) in botoes:
            self.criar_botao(texto, linha, coluna)

    def criar_botao(self, texto, linha, coluna):
        if texto == '=':
            botao = tk.Button(self.master, text=texto, command=self.calcular)
        elif texto == 'C':
            botao = tk.Button(self.master, text=texto, command=self.limpar)
        else:
            botao = tk.Button(self.master, text=texto, command=lambda t=texto: self.adicionar(t))

        botao.grid(row=linha, column=coluna, sticky='nsew')

    def adicionar(self, texto):
        self.entrada.insert(tk.END, texto)

    def limpar(self):
        self.entrada.delete(0, tk.END)

    def calcular(self):
        try:
            expressao = self.entrada.get()
            if 'sin' in expressao:
                valor = float(expressao.replace('sin', '').strip())
                resultado = math.sin(math.radians(valor))
            elif 'cos' in expressao:
                valor = float(expressao.replace('cos', '').strip())
                resultado = math.cos(math.radians(valor))
            elif 'tan' in expressao:
                valor = float(expressao.replace('tan', '').strip())
                resultado = math.tan(math.radians(valor))
            elif 'exp' in expressao:
                valor = float(expressao.replace('exp', '').strip())
                resultado = math.exp(valor)
            elif 'log' in expressao:
                valor = float(expressao.replace('log', '').strip())
                resultado = math.log(valor) if valor > 0 else "Erro"
            else:
                resultado = eval(expressao)

            self.limpar()
            self.entrada.insert(tk.END, str(resultado))

        except Exception as e:
            self.limpar()
            self.entrada.insert(tk.END, "Erro")

if __name__ == "__main__":
    root = tk.Tk()
    calc = CalculadoraCientifica(root)
    root.mainloop()
