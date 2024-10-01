import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class RenameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Renomear Arquivos")
        self.root.geometry("600x400")
        
        # Label e botão para selecionar pasta
        self.folder_label = tk.Label(root, text="Nenhuma pasta selecionada.")
        self.folder_label.pack(pady=10)
        
        self.select_folder_btn = tk.Button(root, text="Selecionar Pasta", command=self.select_folder)
        self.select_folder_btn.pack(pady=5)
        
        # Tabela
        self.table = ttk.Treeview(root, columns=("ID", "Nome Atual", "Novo Nome"), show="headings")
        self.table.heading("ID", text="ID")
        self.table.heading("Nome Atual", text="Nome Atual")
        self.table.heading("Novo Nome", text="Novo Nome")
        self.table.pack(pady=10, fill="both", expand=True)
        
        # Botão para encontrar nomes na planilha
        self.find_names_btn = tk.Button(root, text="Encontrar Nomes", command=self.find_new_names, state="disabled")
        self.find_names_btn.pack(pady=5)

        # Botão para renomear
        self.rename_btn = tk.Button(root, text="Renomear Arquivos", command=self.rename_files, state="disabled")
        self.rename_btn.pack(pady=5)

        self.folder_path = None
        self.files = []
        self.new_names = None

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.folder_label.config(text=f"Pasta Selecionada: {self.folder_path}")
            self.load_files()

    def load_files(self):
        # Simbolo de loading
        self.folder_label.config(text="Carregando arquivos...")
        self.root.update()

        # Listar arquivos na pasta
        self.files = os.listdir(self.folder_path)
        self.table.delete(*self.table.get_children())  # Limpar tabela anterior
        for idx, file in enumerate(self.files):
            self.table.insert("", "end", values=(idx + 1, file, ""))

        # Confirmação e habilitar botão "Encontrar Nomes"
        messagebox.showinfo("Concluído", f"Carregados {len(self.files)} arquivos.")
        self.find_names_btn.config(state="normal")

    def find_new_names(self):
        try:
            planilha_path = filedialog.askopenfilename(title="Selecionar Planilha", filetypes=[("Excel files", "*.xlsx")])
            if not planilha_path:
                return
            
            # Ler a planilha
            df = pd.read_excel(planilha_path)
            
            # Colunas com os nomes atuais e novos
            old_names = df['nome_atual'].tolist()
            new_names = df['novo_nome'].tolist()
            
            # Comparar e exibir na tabela
            for idx, (file, new_name) in enumerate(zip(self.files, new_names)):
                if file in old_names:
                    self.table.set(self.table.get_children()[idx], column="Novo Nome", value=new_name)
                else:
                    self.table.set(self.table.get_children()[idx], column="Novo Nome", value="Erro: Não Encontrado")

            messagebox.showinfo("Concluído", "Novos nomes carregados.")
            self.rename_btn.config(state="normal")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar nomes: {str(e)}")

    def rename_files(self):
        try:
            for idx, item in enumerate(self.table.get_children()):
                old_name = self.table.item(item)['values'][1]
                new_name = self.table.item(item)['values'][2]

                if "Erro" not in new_name:
                    old_file_path = os.path.join(self.folder_path, old_name)
                    new_file_path = os.path.join(self.folder_path, new_name)
                    
                    # Renomear arquivos
                    os.rename(old_file_path, new_file_path)
                    self.table.set(item, column="Nome Atual", value=new_name)  # Atualizar nome na tabela
                    self.table.set(item, column="Novo Nome", value="Renomeado")
                else:
                    self.table.set(item, column="Novo Nome", value="Erro: Arquivo não renomeado")

            messagebox.showinfo("Concluído", "Todos os arquivos renomeados com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao renomear arquivos: {str(e)}")

# Inicializar aplicação Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = RenameApp(root)
    root.mainloop()
