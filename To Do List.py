def main():
    tasks=[]

    while True:
        print("***** To Do List *****")
        print("1.Add Task")
        print("2.Show Task")
        print("3.Mark Task as Done")
        print("4.Exit")

        option = input("Enter your option: ")

        if option == '1':
            print()
            n_tasks = int(input("How many tasks you want to add: "))
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")
            
        elif option =="2":
            print("Tasks: ")
            for j, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not done"
                print(f"{j +1}.{task['task']} - {status}")
        
        elif option =='3':
            index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        
        elif option == '4':
            print("Exiting the To Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
