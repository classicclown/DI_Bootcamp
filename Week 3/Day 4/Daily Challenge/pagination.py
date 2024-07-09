class pagination:
    def __init__(self, items=None,pageSize=10):
        self.items=items
        self.pageSize=int(pageSize)
        self.start=0
        self.end=pageSize

    def getVisibleItems(self):
        start=self.start
        end=self.start+self.pageSize
        if end<=len(self.items):
            page = self.items[start:end]
        else:
            page=self.items[start:len(self.items)]
        return page

    def prevPage(self):
        if self.start<self.pageSize:
            self.start=0
        else:
            self.start-=self.pageSize

    def nextPage(self):
        self.start+=self.pageSize
        

    def firstPage(self):
        self.start=0
    
    def lastPage(self):
        last_page = len(self.items)%self.pageSize
        self.start=len(self.items)-last_page
        return last_page
    
    def goToPage(self,pageNum):
        page=int(self.pageSize*(pageNum-1))
        total_pages = len(self.items)//self.pageSize
        print(total_pages)
        print(page)
        if pageNum>total_pages:
            self.start=(total_pages*self.pageSize)
        elif pageNum<0:
            self.start=0
        else:
            self.start=page

if __name__=='__main__':
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = pagination(alphabetList, 4.5)
    p.goToPage(10)
    print(p.getVisibleItems())
    p.nextPage()
    print(p.getVisibleItems())
    p.prevPage()

  



