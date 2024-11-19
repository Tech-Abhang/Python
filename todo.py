def task():
    tasks=[]

    #greeting
    print("WELCOME TO THE TASK MANAGEMENT APP")

    total_task= int(input("Enter number of tasks you want to add : "))
    #To get number for input by user

    for i in range(1,total_task+1):
        task_name=input(f"enter yout task {i} : ")
        tasks.append(task_name)

    print(f"Today`s tasks are {tasks}")

    while True: #to keep modifing todo list
        operation = int(input("Enter 1 to ADD \n Enter 2 to UPDATE \n Enter 3 to DELETE \n Enter 4 to VIEW \n Enter 5 to EXIT \n enter number : " ))
        if operation == 1:
            add=input("Task you would like to add : ")
            tasks.append(add)
            print("Task is added ")

        elif operation ==2:
            task_name=input("Task you would like to update : ")
            if task_name in tasks:
                up=input("enter new task you want to replace : ")
                ind=tasks.index(task_name)
                tasks[ind]=up
                print(f"Updated task : {up}")
        
        elif operation == 3:
            task_name=input("Task you would like to delete : ")
            tasks.remove(task_name)
            print("Required task is removed")

        elif operation == 4:
            print(f"yout to-do taks are : {tasks}")

        elif operation == 5:
            print("hope you complete your tasks, Have a nice day !")
            break
task()
