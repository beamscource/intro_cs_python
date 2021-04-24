class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)

#Version C

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)
    
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
          return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)
    def lecture(self, stuff):         
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)

#Version A

##class Professor(Lecturer): 
##    def say(self, stuff): 
##        return self.name + ' says: ' + self.lecture(stuff)
    
##class ArrogantProfessor(Professor): 
####    def say(self, stuff): 
####        return 'It is obvious that ' + Professor.say(stuff)
##    def lecture(self, stuff):         
##        return 'It is obvious that ' + Person.say(self, stuff)

#Version B

##class Professor(Lecturer): 
##    def say(self, stuff): 
##        return self.name + ' says: ' + self.lecture(stuff)
    
##class ArrogantProfessor(Professor): 
##    def say(self, stuff): 
##          return self.name + ' says: ' + self.lecture(stuff)
##    def lecture(self, stuff):         
##        return 'It is obvious that ' + Lecturer.lecture(self, stuff)

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

# VErsion C
##>>> pe.say('the sky is blue')
##Prof. eric says: I believe that eric says: the sky is blue 
##
##>>> ae.say('the sky is blue')
##Prof. eric says: It is obvious that I believe that eric says: the sky is blue

#Problem B
##>>> ae.say('the sky is blue')
##eric says: It is obvious that I believe that eric says: the sky is blue
##
##>>> ae.lecture('the sky is blue')
##It is obvious that I believe that eric says: the sky is blue

# Problem A
##>>> e.say('the sky is blue')
##eric says: the sky is blue
##
##>>> le.say('the sky is blue')
##eric says: the sky is blue
##
##>>> le.lecture('the sky is blue')
##I believe that eric says: the sky is blue
##
##>>> pe.say('the sky is blue')
##eric says: I believe that eric says: the sky is blue
##
##>>> pe.lecture('the sky is blue')
##I believe that eric says: the sky is blue
##
##>>> ae.say('the sky is blue')
##eric says: It is obvious that eric says: the sky is blue
##
##>>> ae.lecture('the sky is blue')
##It is obvious that eric says: the sky is blue
