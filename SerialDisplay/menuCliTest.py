from menuCli import menu

def hello():
    print 5

m=menu()

id=m.addItem("hello1", hello)
id=m.addItem("hello2", hello)
#m.execute(id)

m.list()
print
m.list(1)
print
m.list(2)
