class Vecteur2D: #déclaration de classe 
    def __init__(self,a=0,b=0): #déclaration de constructeur avec des paramétres par défaut a=0 et b=0 
        self.x = a #initialisation des paramétres
        self.y = b
print ("le vecteur1 sans paramétres est ")
vecteur1 = Vecteur2D()
print ("x=%d,y=%d"%(vecteur1.x,vecteur1.y))
print ("vecteur2 avec ses propre paramétes est ")
vecteur2 = Vecteur2D(4,5)
print ("x=%d,y=%d"%(vecteur2.x,vecteur2.y))