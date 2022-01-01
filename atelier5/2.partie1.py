class Vecteur2D: #déclaration de classe 
    def __init__(self,a=0,b=0): #déclaration de constructeur avec des paramétres par défaut a=0 et b=0 
        self.x = a #initialisation des paramétres
        self.y = b
    def __addition__(self,vect): # fonction de surchage d'addiction 
        return Vecteur2D(self.x+vect.x, self.y+vect.y)
    def affichage(self): # fonction d'affichage 
        print ( "le vecteur (%d,%d)" % (self.x,self.y))
vecteur3 = Vecteur2D(1,4) #un instant vecteur3 de classe vecteur2D
print (" voila notre vecteur vecteur3(%d,%d)"%(vecteur3.x,vecteur3.y))
vecteur4 = Vecteur2D(2,3)
print (" voila notre vecteur vecteur4(%d,%d)"%(vecteur4.x,vecteur4.y))
print ("la somme de vecteur3(%d,%d)"%(vecteur3.x,vecteur3.y) )
print ("et le  vecteur4(%d,%d) est égale"%(vecteur4.x,vecteur4.y) )
vecteur1 = Vecteur2D(vecteur3.x + vecteur4.x, vecteur3.y + vecteur4.y)
vecteur1.affichage()