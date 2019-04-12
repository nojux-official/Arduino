class menu():
    def __init__(self):
        self.menuL=[]
    def addItem(self, name, action):
        self.menuL.append([name, action])
        return len(self.menuL)-1
    def execute(self, id):
        self.menuL[id][1]()
    def list(self, selected, limit=2):
        counter=0
        if(len(self.menuL)-1==selected):
            counter-=1
        while len(self.menuL)>selected+counter and counter<=limit:
            item=self.menuL[selected+counter]
            if(counter>limit): break
            print item[0]
            counter+=1

def hello():
    print 5

m=menu()

id=m.addItem("hello1", hello)
id=m.addItem("hello2", hello)
#m.execute(id)

m.list(1)
