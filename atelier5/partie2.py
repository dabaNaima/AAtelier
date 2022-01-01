class Etudiant: #déclaration de classe etudiant 
    def __init__(self, nom , prenom, age , cne , moyenne): # Constructeur. Crée un étudiant de nom , de prénom , d'age de cne et de moyenne 
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne

   # création de liste *
list=[] #déclaration  de liste 
list.append (Etudiant("daba "," saida ",21," p13024515 ",15))
list.append (Etudiant("abdlhahid ","manal ",19," p11074811 ",9))
list.append (Etudiant("alae"," hafid ",23," p11254984 ",14))
list.append (Etudiant("daba "," saida ",20," p20154780 ",12))
print("la liste des étudiants saisi est ");
for obj in list : #affichage de liste 
    print (obj.nom ,obj.prenom , obj.age ,obj.cne,obj.moyenne, sep ='')
list.sort(key=lambda x: x.age) 
print("la liste des étudints trie selon leur age est ");
for obj in list : #affichage de liste 
    print (obj.nom ,obj.prenom , obj.age ,obj.cne,obj.moyenne, sep ='')

list.sort(key=lambda x: x.moyenne)
print("la liste des étudints trie selon leur moyenne est ");
for obj in list : #affichage de liste 
       print (obj.nom ,obj.prenom , obj.age ,obj.cne,obj.moyenne, sep ='')