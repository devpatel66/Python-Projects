import datetime

def displayTodos():
    data = getTodosData()
    print("---------------Your Todos---------------")
    for i in data:
        # if(data.index(i) == 0): continue
        print(i)
    
    print("----------------------------------------")


def getTodosData():
    data = []
    with open("todos.txt", "r") as file:
        for i,line in enumerate(file):
            # if(i==0): continue
            data.append(line)
    
    if(len(data) <= 1 ): 0
    return data

def getTodoById(id):
    data = ""
    id = f"id : {id} , "
    with open("todos.txt", "r") as file:
        for i,line in enumerate(file):
            if(i==0): continue
            startIndex = line.index("id")
            endIndex = line.index("Task")
            if(line[startIndex:endIndex] == id):
                data = line
                break
    if(data == ""):return 0
    return data

def addTodo(taskName):
    status = "Pending"
    id = 0
    with open("todos.txt", "r") as file:
        for i,line in enumerate(file):
            id+=1
            # print(i,len(line))
            if(i==0): continue
            startIndex = line.index("id")
            endIndex = line.index("Task")
            s = f"id : {id} , "
            if(line[startIndex:endIndex] == s):
                id+=1
                
    # print("ttodo",getTodoById(id))
    if(getTodoById(id)):
        id+=1
        print("Todo already exists")
        
    date = datetime.date.today()
    task = f"id : {id} , Task : {taskName} , Status :  {status} , Created At: {date}"
    print(task)
    with open("todos.txt", "a") as file:
        file.write(f"{task}\n")

def updateTodo(id,taskName):
    data = getTodoById(id)
    if(data == 0):
        print("Todo not found,Check the id")
        return 0
    startIndex = data.index("Task")
    endIndex = data.index("Status")
    data=data.replace(data[startIndex:endIndex], f"Task : {taskName} , ")
    
    todosData = getTodosData()
    
    if(todosData == 0):
        print("Todo List is Empty")
        return 0
    
    s = f"id : {id} , "
    for i in range(len(todosData)):
        startIndex = todosData[i].index("id")
        endIndex = todosData[i].index("Task")
        if(s == todosData[i][startIndex:endIndex]):
            todosData[i] = data
    with open("todos.txt", "w") as file:
        for i in todosData:
            file.write(i)
    print(data)

def deleteTodo(id):
    todosData = getTodosData()
    s = f"id : {id} , "
    for i in range(len(todosData)):
        startIndex = todosData[i].index("id")
        endIndex = todosData[i].index("Task")
        if(s == todosData[i][startIndex:endIndex]):
            todosData.remove(todosData[i])
            break
    with open("todos.txt", "w") as file:
        for i in todosData:
            file.write(i)

def markTodoAsCompleted(id):
    data = getTodoById(id)
    if(data == 0):
        print("Todo not found,Check the id")
        return 0
    if(data.find("Done") > 0): 
        print("\nTodo already completed \n\n")
        return 0
    startIndex = data.index("Pending")
    endIndex = data.index("Created At")
    
    data = data.replace(data[startIndex:endIndex], "Done , ")
    
    todosData = getTodosData()
    
    if(todosData == 0):
        print("Todo List is Empty")
        return 0
    
    s = f"id : {id} , "
    for i in range(len(todosData)):
        startIndex = todosData[i].index("id")
        endIndex = todosData[i].index("Task")
        if(s == todosData[i][startIndex:endIndex]):
            todosData[i] = data
    with open("todos.txt", "w") as file:
        for i in todosData:
            file.write(i)

    print("\nTodo masked as completed")


if __name__ == '__main__':
    while True:
        print("1. Display Todos\n2. Add Todo\n3. Update Todo\n4. Delete Todo\n5. Mark Todo as Completed\n6. Exit")
        try:
            option = int(input("Choose the options : "))
        except Exception:
            print("Invalid option")
            continue
        match option:
            case 1 :
                displayTodos()
            case 2 :
                taskName = input("Enter the task : ")
                addTodo(taskName)
            case 3 :
                id = int(input("Enter the id : "))
                print(getTodoById(id))
                taskName = input("Enter the task : ")
                updateTodo(id,taskName)
            case 4 :
                displayTodos()
                id = int(input("Enter the id : "))
                deleteTodo(id)
            case 5 :
                displayTodos()
                id = int(input("Enter the id : "))
                markTodoAsCompleted(id)
            case 6 :
                break
            case _ :
                print("Invalid option")
