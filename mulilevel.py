class grandparent:
    def trait(self):
        print('grandparent traits')
        		
class parent(grandparent):
	def traits(self):
		print('parent traits')
		
class child(parent):
	def traitss(self):
		print('child traits')
  
c=child()
c.trait()
c.traits()
c.traitss()