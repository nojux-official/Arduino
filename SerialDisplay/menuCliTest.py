from menuCli import menu

def hello1():
    print 5
def hello2():
    print 6
def hello3():
    print 7

m=menu()

m.addItem("hello1", hello1)
m.addItem("hello2", hello2)
mId=m.addItem("hello3", hello3)
#m.execute(0)

idd=0

while True:
    a=raw_input(">")
    if(a=="u" and idd>0):
        idd-=1
    elif(a=="d" and mId>idd):
        idd+=1
    elif(a=="s"):
        m.execute(idd)
    #elif(a=="u")
    m.list(idd, 4)
