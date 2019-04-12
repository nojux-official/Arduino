class menu():
    def __init__(self):
        self.menuL=[]
    def addItem(self, name, action):
        self.menuL.append([name, action])
        return len(self.menuL)-1
    def execute(self, id):
        self.menuL[id][1]()
    def list(self, selected=0, limit=2):
        counter=0
        thisI=True
        if(len(self.menuL)-1==selected):
            counter-=1
            thisI=False
        while len(self.menuL)>selected+counter and counter<=limit:
            if(selected+counter==selected):
                thisI=True
            cache=""
            if(thisI): cache+="->"
            else: cache+="  "
            item=self.menuL[selected+counter]
            if(counter>limit): break
            print cache, item[0]
            thisI=False
            counter+=1

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
