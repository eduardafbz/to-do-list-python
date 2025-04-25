from service.TaskService import TaskService

class TaskController:

    def __init__(self):
        self.service = TaskService();
    
    def print_separator(self):
        print("-" * 40)

    def print_section(self, title):
        self.print_separator()
        print(f"{title:^40}")
        self.print_separator()

    def print_task(self, task):
        self.print_separator()
        print(f"ID: {task.id}")
        print(f"Título: {task.title}")
        print(f"Descrição: {task.description}")
        print(f"Status: {'Completa' if task.completed else 'Incompleta'}")
        print(f"Criado em: {task.createdAt}")
        print(f"Atualizado em: {task.updatedAt}")
        self.print_separator()

    def menu(self):
        self.print_section("MENU DE TAREFAS")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Buscar por ID")
        print("4. Atualizar tarefa")
        print("5. Deletar todas")
        print("6. Deletar tarefa")
        print("0. Sair")

    def start_task_menu(self):
        while True:
            self.menu()
            choice = int(input("\nDigite uma opção: "))

            if choice == 1:
                title = input("Digite o título da tarefa: ")
                description = input("Digite a descrição: ")
                task = self.service.add(title, description)
                self.print_separator()
                print(f"Tarefa adicionada: ")
                self.print_task(task)
                self.print_separator()

            elif choice == 2:
                tasks = self.service.findAll()
                if tasks:
                    for task in tasks:
                        self.print_task(task)
                else:
                    self.print_separator()
                    print("Nenhuma tarefa encontrada.")
                    self.print_separator()

            elif choice == 3:
                id = int(input("Digite o id: "))
                task = self.service.findById(id)
                self.print_separator()
                if task:
                    print(f"Tarefa de id {id}: ")
                    self.print_task(id)
                else:
                    print("Tarefa não encontrada.")
                self.print_separator()

            elif choice == 4: 
                id = int(input("Digite o id da tarefa a ser atualizada: "))
                title = input("Digite o título da tarefa: ")
                description = input("Digite a descrição: ")
                completed = bool(input("Ela está completa? ").strip().lower())
                if completed == "sim":
                    completed = True
                else:
                    completed = False
                task = self.service.update(id, title, description, completed)
                if task:
                    self.print_separator()
                    print(f"Tarefa atualizada." if task else "Tarefa não encontrada.")
                    self.print_separator()

            elif choice == 5:
                self.service.deletAll()
                self.print_separator()
                print("Todas as tarefas foram excluídas.")
                self.print_separator()

            elif choice == 6:
                id = int(input("Digite o id da tarefa a ser excluída: "))
                task = self.service.deleteById(id)
                self.print_separator()
                print(f"Tarefa de id {id} excluída." if task else "Tarefa não encontrada.")
                self.print_separator()
            
            elif choice == 0:
                self.print_separator()
                print("Saindo...")
                self.print_separator()
                break

            else:
                self.print_separator()
                print("Opção inválida.")
                self.print_separator()
                break

                    