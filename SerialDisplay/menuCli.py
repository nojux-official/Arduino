class menu():
    def __init__(self):
        self.menuL=[]
    def truncate(self, n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier
    def addItem(self, name, action, *args, **kwargs):
        self.menuL.append([name, action, args, kwargs])
        return len(self.menuL)-1
    def removeItem(self, idd):
        del self.menuL[idd]
    def execute(self, idd):
        self.menuL[idd][1](*self.menuL[idd][2], **self.menuL[idd][3])
    def listItems(self, selected=0, limit=2):
        page=self.truncate(selected/limit)+1
        for i in range(page*limit-limit, page*limit):
            if(i==len(self.menuL)):
                break
            item=self.menuL[i][0]
            if(i==selected): prefix="->"
            else: prefix="  "
            print prefix, item
