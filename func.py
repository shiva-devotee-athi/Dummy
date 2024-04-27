# def getMyName (name):
#     return f"Naan Than {name}"
# print(getMyName("vijay"))

# names_l = ('Olivia', 'Nathan', 'Bethany', 'Jacob')
# print(type(names_l))


class MyNumbers:
 def __iter__(self):
    self.a = 1
    return self

 def __next__(self):
    if self.a <=30:
        x= self.a
        self.a += 1 
        return x
    else:
        raise StopIteration
        

myVar = MyNumbers()
myIter = iter(myVar)

for x in myIter:
  print(x)


