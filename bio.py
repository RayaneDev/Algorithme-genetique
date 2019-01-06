from random import randint, random
import math

class Cell :

    def __init__(self, target, genes, adn = None) :

        self.genes = genes
        self.target = target

        if adn is None :
            self.adn = ""

            for i in range (0, len(target)) :
                self.adn += self.genes[randint(0, len(self.genes) - 1)]
        else :
            self.adn = adn

        self.rate()

    def rate (self) :

        self.rating = 1

        print (self.target, self.adn, len(self.target), len(self.adn))

        for i in range (0, len(self.adn)) :
            if self.adn[i] == self.target[i] :
                self.rating += 1


        return self.rating

class Population :

    def __init__(self, number, target, mutation_rate) :

        self.genes = "abcdefghijklmnopqrstuvwxyz "
        self.target = target
        self.cells = []
        self.number = number
        self.m_rate = mutation_rate

        for i in range (0, number) :

            self.cells.append(Cell(self.target, self.genes))

    def next (self) :

        # Sélection des meilleures cellules
        cells = []

        for i in range (0, len(self.cells)) :
            l = random()
            if l <= self.cells[i].rating / (len(self.target) + 1) :
                cells.append(self.cells[i])

        # Croisements (il faut s'assurer qu'il y ait au moins 2 cellules)
        childs = []

        if len(cells) > 1 :
            while len(childs) < self.number :
                i = 0

                while i < len(cells) - 1 :

                    index_a = math.ceil(len(cells[i].adn)/2)
                    index_b = math.floor(len(cells[i+1].adn)/2) if len(self.target) % 2 == 0 else math.floor(len(cells[i+1].adn)/2)+1

                    a, b = cells[i].adn[:index_a], cells[i+1].adn[index_b:]

                    a = list(a)
                    b = list(b)

                    # Mutations aléatoires

                    for x in range (0, len(a)) :
                        l = random()

                        if l <= self.m_rate :
                            a[x] = self.genes[randint(0, len(self.genes) - 1)]

                    for x in range (0, len(b)) :
                        l = random()

                        if l <= self.m_rate :
                            b[x] = self.genes[randint(0, len(self.genes) - 1)]

                    a = ''.join(a)
                    b = ''.join(b)

                    childs.append(Cell(self.target, self.genes, a+b))
                    i += 2
                    if len(childs) == self.number :
                        break
        else :
            return 0
        print(len(childs))
        self.cells = childs


size = 100
target = "entropie" # Mot généré au bout de 5 itérations avec les paramètres actuels
mutation_rate = 0.02

p = Population(size, target, mutation_rate) # Taille, cible, taux de mutation


first = 0
index = 0

for x in range (0, 10) :
    for i in range (0, len(p.cells)) :
        if p.cells[i].adn == target :
            first = x
            index = i
            break
        print (p.cells[i].adn)
        p.next()
    if p.cells[index].adn == target :
        break


print (target, 'créé en', first, 'itérations !')
