from service.TaskService import TaskService

class TaskController:

    def __init__(self):
        self.service = TaskService();

    def run(self):
        while True:
            print("\nMENU DE TAREFAS")
            print("1. Adicionar tarefa")
            print("2. Listar tarefas")
            print("3. Buscar por ID")
            print("4. Atualizar tarefa")
            print("5. Deletar todas")
            print("6. Deletar tarefa")
            print("0. Sair")

            choice = int(input("Digite uma opção: "))

            if choice == 1:
                title = input("Digite o título da tarefa: ")
                description = input("Digite a descrição: ")
                task = self.service.add(title, description)
                print(f"Tarefa adicionada: {task}")

            elif choice == 2:
                tasks = self.service.get_all()
                if tasks:
                    for task in tasks:
                        print(task)
                else:
                    print("Nenhuma tarefa encontrada.")

            elif choice == 3:
                id = int(input("Digite o id: "))
                task = self.service.get_by_id(id)
                print(f"Tarefa de id {id}: {task}" if task else "Tarefa não encontrada.")

            elif choice == 4: 
                id = int(input("Digite o id da tarefa a ser atualizada: "))
                title = input("Digite o título da tarefa: ")
                description = input("Digite a descrição: ")
                completed = bool(input("Ela está completa? ").lower)
                if completed == "sim":
                    completed = True
                else:
                    completed = False
                task = self.service.update(id, title, description, completed)
                if task:
                    print(f"Tarefa atualizada." if task else "Tarefa não encontrada.")

            elif choice == 5:
                self.service.delete_all()
                print("Todas as tarefas foram excluídas.")

            elif choice == 6:
                id = int(input("Digite o id da tarefa a ser excluída: "))
                task = self.service.delete_by_id(id)
                print(f"Tarefa de id {id} excluída." if task else "Tarefa não encontrada.")
            
            elif choice == 0:
                print("Saindo...")
                break

            else:
                print("Opção inválida.")
                break

                    