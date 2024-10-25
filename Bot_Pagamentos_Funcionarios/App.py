import sys
import os
import tkinter as tk
from tkinter import messagebox, Toplevel

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Classes_funcionarios.Funcionario import Funcionario
from Classes_funcionarios.FuncionarioHora import FuncionarioHorista
from Classes_funcionarios.FuncionarioMensal import FuncionarioMensalista
from Classes_funcionarios.FuncionarioComissionado import FuncionarioComissionado


class App:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Funcionários")
        master.geometry("800x600")
        master.resizable(False, False)
        master.configure(bg="#f0f0f0")

        self.frame = tk.Frame(master, bg="#ffffff", padx=30, pady=30, width=1000)
        self.frame.pack(padx=10, pady=10)

        self.label_titulo = tk.Label(self.frame, text="Cadastro de Funcionários", font=("Helvetica", 16, "bold"), bg="#ffffff")
        self.label_titulo.pack(pady=(0, 20))

        self.label_nome = tk.Label(self.frame, text="Nome:", font=("Helvetica", 12), bg="#ffffff")
        self.label_nome.pack(anchor='w')
        self.entry_nome = tk.Entry(self.frame, font=("Helvetica", 12))
        self.entry_nome.pack(fill='x', pady=(0, 10))

        self.label_matricula = tk.Label(self.frame, text="Matrícula:", font=("Helvetica", 12), bg="#ffffff")
        self.label_matricula.pack(anchor='w')
        self.entry_matricula = tk.Entry(self.frame, font=("Helvetica", 12))
        self.entry_matricula.pack(fill='x', pady=(0, 10))

        self.label_tipo = tk.Label(self.frame, text="Tipo de Funcionário:", font=("Helvetica", 12), bg="#ffffff")
        self.label_tipo.pack(anchor='w')
        self.tipo_var = tk.StringVar(value="horista")
        self.radio_horista = tk.Radiobutton(self.frame, text="Horista", variable=self.tipo_var, value="horista", font=("Helvetica", 12), bg="#ffffff", command=self.atualizar_campos)
        self.radio_horista.pack(anchor='w')
        self.radio_mensal = tk.Radiobutton(self.frame, text="Mensal", variable=self.tipo_var, value="mensal", font=("Helvetica", 12), bg="#ffffff", command=self.atualizar_campos)
        self.radio_mensal.pack(anchor='w')
        self.radio_comissionado = tk.Radiobutton(self.frame, text="Comissionado", variable=self.tipo_var, value="comissionado", font=("Helvetica", 12), bg="#ffffff", command=self.atualizar_campos)
        self.radio_comissionado.pack(anchor='w')

        self.label_salario = tk.Label(self.frame, text="Salário/Valor Hora:", font=("Helvetica", 12), bg="#ffffff")
        self.label_salario.pack(anchor='w')
        self.entry_salario = tk.Entry(self.frame, font=("Helvetica", 12))
        self.entry_salario.pack(fill='x', pady=(0, 10))

        self.label_horas = tk.Label(self.frame, text="Horas Trabalhadas (se aplicável):", font=("Helvetica", 12), bg="#ffffff")
        self.entry_horas = tk.Entry(self.frame, font=("Helvetica", 12))

        self.label_vendas = tk.Label(self.frame, text="Vendas:", font=("Helvetica", 12), bg="#ffffff")
        self.entry_vendas = tk.Entry(self.frame, font=("Helvetica", 12))

        self.label_taxa_comissao = tk.Label(self.frame, text="Taxa de Comissão (%):", font=("Helvetica", 12), bg="#ffffff")
        self.entry_taxa_comissao = tk.Entry(self.frame, font=("Helvetica", 12))

        # Botões serão posicionados no final
        self.button_frame = tk.Frame(self.frame, bg="#ffffff")
        self.button_frame.pack(side='bottom', pady=20)

        self.button_cadastrar = tk.Button(self.button_frame, text="Cadastrar Funcionário", command=self.cadastrar_funcionario, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="raised")
        self.button_cadastrar.pack(side='left', padx=5)

        self.button_lista = tk.Button(self.button_frame, text="Lista de Funcionários", command=self.mostrar_lista_funcionarios, font=("Helvetica", 12), bg="#FF9800", fg="white", relief="raised")
        self.button_lista.pack(side='left', padx=5)

        self.funcionarios = []

        # Atualiza os campos de entrada inicialmente
        self.atualizar_campos()

    def atualizar_campos(self):
        tipo = self.tipo_var.get()
        
        if tipo == "horista":
            self.label_horas.pack(anchor='w')
            self.entry_horas.pack(fill='x', pady=(0, 10))
            self.label_vendas.pack_forget()
            self.entry_vendas.pack_forget()
            self.label_taxa_comissao.pack_forget()
            self.entry_taxa_comissao.pack_forget()

        elif tipo == "mensal":
            self.label_horas.pack_forget()
            self.entry_horas.pack_forget()
            self.label_vendas.pack_forget()
            self.entry_vendas.pack_forget()
            self.label_taxa_comissao.pack_forget()
            self.entry_taxa_comissao.pack_forget()

        elif tipo == "comissionado":
            self.label_horas.pack_forget()
            self.entry_horas.pack_forget()
            self.label_vendas.pack(anchor='w')
            self.entry_vendas.pack(fill='x', pady=(0, 10))
            self.label_taxa_comissao.pack(anchor='w')
            self.entry_taxa_comissao.pack(fill='x', pady=(0, 10))

    def cadastrar_funcionario(self):
        nome = self.entry_nome.get()
        matricula = self.entry_matricula.get()
        
        try:
            salario = float(self.entry_salario.get())
            horas = int(self.entry_horas.get()) if self.entry_horas.winfo_ismapped() else 0
            vendas = float(self.entry_vendas.get()) if self.entry_vendas.winfo_ismapped() else 0
            taxa_comissao = float(self.entry_taxa_comissao.get()) if self.entry_taxa_comissao.winfo_ismapped() else 0.05
        except ValueError:
            messagebox.showerror("Erro", "Salário, horas, vendas e taxa de comissão devem ser números válidos.")
            return

        if not nome or not matricula:
            messagebox.showerror("Erro", "Nome e matrícula não podem estar vazios.")
            return

        if self.tipo_var.get() == "horista":
            funcionario = FuncionarioHorista(nome, matricula, horas, salario)
        elif self.tipo_var.get() == "mensal":
            funcionario = FuncionarioMensalista(nome, matricula, salario)
        elif self.tipo_var.get() == "comissionado":
            funcionario = FuncionarioComissionado(nome, matricula, salario, vendas, taxa_comissao)

        self.funcionarios.append(funcionario)
        messagebox.showinfo("Cadastro", f"Funcionário {nome} cadastrado com sucesso!")

        self.limpar_campos()

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_salario.delete(0, tk.END)
        self.entry_horas.delete(0, tk.END)
        self.entry_vendas.delete(0, tk.END)
        self.entry_taxa_comissao.delete(0, tk.END)
        self.tipo_var.set("horista")
        self.atualizar_campos()

    def mostrar_lista_funcionarios(self):
        if not self.funcionarios:
            messagebox.showinfo("Lista de Funcionários", "Nenhum funcionário cadastrado.")
            return
        
        lista_window = Toplevel(self.master)
        lista_window.title("Lista de Funcionários")
        lista_window.geometry("1000x600")
        lista_window.configure(bg="#ffffff")

        for index, funcionario in enumerate(self.funcionarios):
            salario = funcionario.calcular_salario()
            info = f"Nome: {funcionario.nome}, Matrícula: {funcionario.matricula}, Tipo: {funcionario.__class__.__name__}, Salário: R${salario:.2f}"
            label = tk.Label(lista_window, text=info, justify='left', bg="#ffffff",  font=("Helvetica", 14))
            label.pack(pady=5)

            button_frame = tk.Frame(lista_window, bg="#ffffff")
            button_frame.pack(pady=5)

            button_editar = tk.Button(button_frame, text="Editar", command=lambda idx=index: self.editar_funcionario(idx, lista_window), bg="#FFC107", fg="black")
            button_editar.pack(side=tk.LEFT, padx=5)

            button_excluir = tk.Button(button_frame, text="Excluir", command=lambda idx=index: self.excluir_funcionario(idx, lista_window), bg="#F44336", fg="white")
            button_excluir.pack(side=tk.LEFT, padx=5)

    def editar_funcionario(self, index, lista_window):
        funcionario = self.funcionarios[index]
        lista_window.destroy()  # Fechar a janela de listagem ao clicar em "Editar"

        editar_window = Toplevel(self.master)
        editar_window.title("Editar Funcionário")
        editar_window.geometry("400x400")
        editar_window.configure(bg="#ffffff")

        label_nome = tk.Label(editar_window, text="Nome:", font=("Helvetica", 12), bg="#ffffff")
        label_nome.pack(anchor='w')
        entry_nome = tk.Entry(editar_window, font=("Helvetica", 12))
        entry_nome.pack(fill='x', pady=(0, 10))
        entry_nome.insert(0, funcionario.nome)

        label_matricula = tk.Label(editar_window, text="Matrícula:", font=("Helvetica", 12), bg="#ffffff")
        label_matricula.pack(anchor='w')
        entry_matricula = tk.Entry(editar_window, font=("Helvetica", 12))
        entry_matricula.pack(fill='x', pady=(0, 10))
        entry_matricula.insert(0, funcionario.matricula)

        label_salario = tk.Label(editar_window, text="Salário/Valor Hora:", font=("Helvetica", 12), bg="#ffffff")
        label_salario.pack(anchor='w')
        entry_salario = tk.Entry(editar_window, font=("Helvetica", 12))
        entry_salario.pack(fill='x', pady=(0, 10))
        
        if isinstance(funcionario, FuncionarioHorista):
            entry_salario.insert(0, funcionario.valor_hora)
        elif isinstance(funcionario, FuncionarioMensalista):
            entry_salario.insert(0, funcionario.salario_mensal)
        elif isinstance(funcionario, FuncionarioComissionado):
            entry_salario.insert(0, funcionario.salario_base)

        button_atualizar = tk.Button(editar_window, text="Atualizar Informações", font=("Helvetica", 12), bg="#4CAF50", fg="white",
                                     command=lambda: self.atualizar_funcionario(index, entry_nome, entry_matricula, entry_salario, editar_window))
        button_atualizar.pack(pady=20)

    def atualizar_funcionario(self, index, entry_nome, entry_matricula, entry_salario_base, editar_window):
        nome = entry_nome.get()
        matricula = entry_matricula.get()

        try:
            salario_base = float(entry_salario_base.get())
        except ValueError:
            messagebox.showerror("Erro", "O salário deve ser um número válido.")
            return

        funcionario = self.funcionarios[index]

        # Atualizando os atributos do funcionário
        funcionario.nome = nome
        funcionario.matricula = matricula

        # Atualizando o salário de acordo com o tipo de funcionário
        if isinstance(funcionario, FuncionarioMensalista):
            funcionario.salario_mensal = salario_base  # Atualiza o salário mensal
        elif isinstance(funcionario, FuncionarioComissionado):
            funcionario.salario_base = salario_base  # Atualiza o salário base
        elif isinstance(funcionario, FuncionarioHorista):
            funcionario.valor_hora = salario_base  # Se for horista, atualiza o valor por hora

        # Fechar a janela de edição
        editar_window.destroy()
        self.atualizar_lista_funcionarios()

    def excluir_funcionario(self, index, lista_window):
        del self.funcionarios[index]
        messagebox.showinfo("Exclusão", "Funcionário excluído com sucesso.")
        
        lista_window.destroy()
        self.mostrar_lista_funcionarios()

root = tk.Tk()
app = App(root)
root.mainloop()
