from sys import argv

script, func = argv

tasks = ["Water the plants", "Do homework", "Watch TV"]

def list():
    target = open('task.txt', 'r')
    to_do = target.read()
    print to_do
    target.close()




def add():
    target = open('task.txt', 'a')
    task.append(argv)





# for num, task in enumerate(tasks):
#     target.write(task)
#     target.write("\n")
