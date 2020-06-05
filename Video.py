class Video:
    def __init__ (self = "", title = "", categoryId = "", status = ""):
        self.title = title
        self.categoryId = categoryId
        self.status = status

    def getTitle(self):
        return self.title
    
    def getCategoryId(self):
        return self.categoryId

    def getStatus(self):
        return self.status
        
    def setTitle(self, title):
        self.title = title
    
    def setCategoryId(self, categoryId):
        self.categoryId = categoryId
    
    def setStatus(self, status):
        self.status = status    

