from menuCli import menu

menus=[]

def switchMenu(menuId=0):
    global m, menus, idd
    m=menus[menuId]
    idd=0

def hello1():
    print 5
def hello2():
    print 6
def hello3():
    print 7

m=menu()
m.addItem("start", hello1)
m.addItem("hellos", switchMenu, 1)
m.addItem("exit", hello3)
menus.append(m)

m=menu()
m.addItem("hello1", hello1)
m.addItem("hello2", hello2)
m.addItem("hello3", hello3)
menus.append(m)

switchMenu()

mId=2

while True:
    a=raw_input(">")
    if(a=="u" and idd>0):
        idd-=1
    elif(a=="d" and mId>idd):
        idd+=1
    elif(a=="s"):
        m.execute(idd)
    #elif(a=="u")
    m.listItems(idd, 4)
