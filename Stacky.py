from math import*
fn={'/':lambda x: (x.pop)/(x.pop), '*':lambda x: (x.pop)*(x.pop), '+':lambda x: (x.pop)+(x.pop)}
class Ser(object):
 def __init__(self):
  self.stack=[]
  self.fn=fn
 def pop(self):
  return self.stack.pop()
 def push(self,val):
  self.stack+=[val]
 def eval(self,code):
  i=0
  self.code=code
  while i<len(code):
   oldstack=self.stack[:]
   try:
    c=code[i]
    if c=='"':
     s = ""
     i+=1
     while i<len(code) and code[i]!='"':
      s+=code[i]
      i+=1
     self.push(s)
    elif c==" ":
     i+=1
    elif c.isdigit():
     if code.find(c)<0 or code[code.find(c)-1].isdigit():
      s=c
      i+=1
      while i<len(code) and code[i].isdigit():
       s+=code[i]
       i+=1
     self.push(s)
    else:
     self.fn.get(c,lambda x:x)(self)
   except SystemExit:
    exit()
   except:
    self.stack=oldstack[:]
   finally:
    i+=1
   while len(self.stack)>0:
    print self.pop()
 
 
def ex(code):
 Stacky=Ser()
 Stacky.eval(code)
ex(raw_input())
