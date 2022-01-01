class Point: #déclaration de classe 
    def __init__(self,x=0.0,y=0.0): #déclaration de constructeur avec des paramétres par défaut   
        self.px = float(x)  #initialisation des paramétres
        self.py= float(y)
class Segment:  
       def __init__(self,x1,y1,x2,y2): #constructeur utilise 2 objet de classe point 
            self.orig=Point(x1,y1)
            self.extrem=Point(x2,y2)
             
       def affichage(self): # fonction d'affichage
            print (" voici le segement: [(%d,%d),(%d,%d)]" % (self.orig.px,self.orig.py,self.extrem.px,self.extrem.py))
segment1= Segment(1,2,3,4)
segment1.affichage()