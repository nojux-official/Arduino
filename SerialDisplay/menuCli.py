class menu():
    def __init__(self):
        self.menuL=[]
    def addItem(self, name, action):
        self.menuL.append([name, action])
        return len(self.menuL)-1
    def removeItem(self, idd):
        del self.menuL[idd]
    def execute(self, idd):
        self.menuL[idd][1]()
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
