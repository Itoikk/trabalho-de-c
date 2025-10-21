import tkinter as tk

# Função que utiliza as 3 entradas (exemplo: soma)
def minha_funcao(a, b, c):
    return a + b + c

# Criar a janela principal
root = tk.Tk()
root.title("Programa com 3 Entradas")

# Criar 3 campos de entrada
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

# Label para mostrar o resultado
label = tk.Label(root, text="Resultado: ")

# Função chamada pelo botão
def on_click():
    try:
        # Obter valores das entradas e converter para float
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())
        # Usar na função
        result = minha_funcao(a, b, c)
        # Atualizar o label com o resultado
        label.config(text=f"Resultado: {result}")
    except ValueError:
        label.config(text="Erro: Insira números válidos")

# Botão para executar
button = tk.Button(root, text="Calcular Soma", command=on_click)

# Organizar os widgets na janela
entry1.pack(pady=5)
entry2.pack(pady=5)
entry3.pack(pady=5)
button.pack(pady=10)
label.pack(pady=5)

# Iniciar o loop da interface
root.mainloop()