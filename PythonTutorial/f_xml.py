#xml parsing	
def xml(tagname, content='',**kwargs):
	attributes = ''
	for key,value in kwargs.items():
		attributes +='{}="{}"'.format(key,value)
	return "<{0} {2}>{1}</{0}>".format(tagname, content, attributes)
print xml('foo')
print xml('foo','value')
print xml('foo','value',a=1)
print xml('foo','value',a=1,b=2)
print xml('foo','value',a=1,b=2,c=3)
	
#Local
#Enclosing function

#Global ->
#Builtins ->dict 

#Byte compiler

#del(__builtins__)
#__builtins__.list =type('[]')
