class Rectangle: #déclaration de classe 
    def __init__(self,longeur=4,largeur=6): #déclaration de constructeur avec des paramétres par défaut de longeur et largeur de rectangle  
        self.longeur = longeur  #initialisation des paramétres
        self.largeur= largeur
        self.nom ="rectangle"
        
    def surface_rec(self): #déclaration de lafonction calcule la surface 
        return self.longeur*self.largeur
        
    def affichage(self): # fonction d'affichage 
        print ( "la surface de réctangle qui a une longeur egal %d et une largeur egal %d est %d "  % (self.longeur, self.largeur,self.surface_rec()))
class Carre(Rectangle): #déclaration de la classe caree hérite de la classe rectangle
    def __init__(self,x=2):
        Rectangle.__init__(self,x,x)
        self.nom="carré"
rectangle1=Rectangle()
carre1=Carre()
rectangle1.affichage()
carre1.affichage()