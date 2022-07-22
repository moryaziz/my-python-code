class tag(object):
    def __init__(self,name ,content):
        self.start_tag = name
        self.content = content

    def __str__(self):
        return '{}{}'.format(self.start_tag,self.content)

class doc(tag):
    def __init__(self,name1="head",content="",version = 5):
        super().__init__(name = name1,content = content)
    #def __init__(self,name,content,version = 5):
        #super().__init__(name,content)


simple_tag = tag(1,2)
#print(simple_tag)
docsample = doc()
print(docsample)

