
# create html file
# html file has DocType,Body,Head which are all <Tag>
from pydoc import Doc

# 1- we create 3 classe
# 2 -create class Tag
# 3- 3 method init, str and display for tag
# 4- create doctype which name is constant, no content and att and no end_tag

class Tag(object):

    def __init__(self,name,content,**att):
        self.name = name
        self.start_tag = '<{}>'.format(name)
        self.content = content
        self.end_tag = '</{}>'.format(name)
        # we get att like key and value, then convert in to string and append it to a list.
        # the join the att list to local parametar and add it to start_tag.
        self.attributes = list()
        if att:
            for ky in att:
                self.attributes.append(f"{str(ky)} = {att[ky]}")
                # how to use f-string method: name = 'Tushar'  age = 23
                # print(f"Hello, My name is {name} and I'm {age} years old.")

    def __str__(self):
        if self.attributes:
            att = ' '.join(self.attributes)
            self.start_tag = '<{} {}>'.format(self.name,att)
        return'{}{}{}'.format(self.start_tag, self.content, self.end_tag)

    def display(self,dump=False,file=None):
        if dump:
            print(self)
        if file:
            print(self,file=file)
        return str(self)
 # at end we write 'return str(self) because in html class we want to pass the export of display
 # to content of html new_tag but export of display needs to be a return.


class DocType(Tag):

    def __init__(self,version=5):
        if version == 5:
            name1 = '!DOCTYPE html'
        super().__init__(name=name1, content='') # because name and content are steady.
        self.end_tag = ''

        # if we have different name or content for doctype, use method below instead.

    #    def __init__(self,name,content,version=5):
    #       super().__init__(name = name , content = content)


class Head(Tag):
    def __init__(self):
        super().__init__(name='head',content='\n')
        # name are constant. content is consisted of some tags. so define head_content as list().
        self.head_content = list()

    def add_content(self,name,content,single=False,**att):
        # define def add_content to add new_tags to self.head_content and
        # at final join self.head_content as list to self.content in display method.
        new_tag = Tag(name=name, content=content, **att)
        if single:
            new_tag.content = ''
            new_tag.end_tag = ''
        self.head_content.append(str(new_tag))

    def display(self,dump=False):
        for i in self.head_content:
            self.content += i +'\n'
        super().display(dump)
        return str(self)




class Body(Tag):
    def __init__(self):
        super().__init__(name='body', content='\n')
        # name are constant. content is consisted of some tags. so define body_content as list().
        self.body_content = list()

    def add_content(self, name, content, single=False,child=None, **att):
        # define def add_content to add new_tags to self.body_content and
        # at final join self.body_content as list to self.content in display method.
        new_tag = Tag(name=name, content=content, **att)
        if child:
            for ch in child:
                new_tag.content += '\n' + ch
        if single:
            new_tag.content = ''
            new_tag.end_tag = ''
        new_tag.end_tag = '\n' + new_tag.end_tag
        self.body_content.append(str(new_tag))

# child difine by user. a child can be parent and have multi child but it is still a child.
# a parent Tag is outest Lag that write to content of body.

    def define_child(self,name,content,single=False,child=None,**att):
        new_tag = Tag(name=name, content=content, **att)
        if child:
            for ch in child:
                new_tag.content += '\n' + ch
        if single:
            new_tag.content = ''
            new_tag.end_tag = ''
        new_tag.start_tag = '\t' + new_tag.start_tag
        new_tag.content = '\n' + '\t' + new_tag.content
        new_tag.end_tag = '\n' + '\t' + new_tag.end_tag + '\n'
        return str(new_tag)


    def display(self,dump=False):
        for i in self.body_content:
            self.content += i + '\n'
        super().display(dump)
        return str(self)


# simple_tag = Tag('mate','simple content', Class = 'ali' , Class2 = "ali2")
# #print(simple_tag)
# simple_tag.display()
# 
# headsimple = Head()
# headsimple.add_content('meta','salam',single=True, Property="og:site_name" , Content="varzesh3")
# headsimple.display()
# 
# bodysimple = Body()
# a1 = bodysimple.define_child('child1','i am child111111')
# a2 = bodysimple.define_child('child2','',child=(a1,), Property=" -----")
# bodysimple.add_content('meta','',single=False, child= (a2,), Property="og:site_name" , Content="varzesh3")
# bodysimple.add_content('meta','salam',single=False, Property="og:site_name" , Content="varzesh3")
# bodysimple.display()
# 
# 
# doc = DocType(5)
# doc.display()


# in html class, we dont make any new parameter or function. we just get data and pass them to
# doc or body and head and also call their method like add_content or display.
class Html(object):
    def __init__(self,version=5):
        self.doc = DocType(5)
        self.head=Head()
        self.body=Body()
    
    def add_content(self,name,content,section='body',single=False,child=None,**att):
        if section == 'head':
            if child:
                raise NotImplementedError("head part do not have child")
            else:
                self.head.add_content(name=name,content=content,single=single,**att)

        elif section == 'body':
            self.body.add_content(name=name,content=content,single=single,child=child,**att)

        else:
            raise NotImplementedError("wrong section")

    def define_child(self,name,content,single=False,child=None,**att):
        new_tag = Tag(name=name, content=content, **att)
        if child:
            for ch in child:
                new_tag.content += '\n' + ch
        if single:
            new_tag.content = ''
            new_tag.end_tag = ''
        new_tag.start_tag = '\t' + new_tag.start_tag
        new_tag.content = '\n' + '\t' + new_tag.content
        new_tag.end_tag = '\n' + '\t' + new_tag.end_tag + '\n'
        return str(new_tag)

    def display(self,dump=False,file='index.html'):
        if dump:
            self.doc.display(dump=True)
            new_tag=Tag('html','\n')
            new_tag.content += self.head.display(dump=False) + '\n'
            new_tag.content += self.body.display(dump=False) + '\n'
            print(str(new_tag))
    # if we want to write it in html file. we open file and use print method to write str on file.
        if file:
            with open (file,'a+') as h_file:
                self.doc.display(dump=False)
                new_tag = Tag('html', '\n')
                new_tag.content += self.head.display(dump=False) + '\n'
                new_tag.content += self.body.display(dump=False) + '\n'
                print(str(new_tag),file = h_file)

html = Html(5)

html.head.add_content('meta','salam',single=True, Property="og:site_name" , Content="varzesh3")

a1 = html.define_child('child1','i am child111111')
a2 = html.define_child('child2','',child=(a1,), Property=" -----")
html.body.add_content('meta','',single=False, child= (a2,), Property="og:site_name" , Content="varzesh3")
#bodysimple.add_content('meta','salam',single=False, Property="og:site_name" , Content="varzesh3")
html.display(dump=False,file = 'index')





