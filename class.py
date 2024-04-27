class MyHome:
    def __init__(self,name) :
        self.name = name
    def father(self):
        print( f"father name is {self.name}")

homeMates = MyHome("my Name")
# print(homeMates.name)
homeMates.father()