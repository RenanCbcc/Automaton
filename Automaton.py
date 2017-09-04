# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
𝛿1  = [['s0','a','s1'],['s1','b','s2'],['s2','a','s3'],['s2','b','s2'],['s3','a','s4'],['s4','b','s3']]
AFD1 = [['a', 'b'], ['s0', 's1', 's2', 's3','s4'], 𝛿1, 's0', ['s3']]

𝛿2  = [['q0', '1', 'q0'], ['q0', '2', 'q0'], ['q0', '3', 'q0'], ['q0', '4', 'q0'], ['q0', '6', 'q0'], ['q0', '7', 'q0'],
       ['q0', '8', 'q0'], ['q0', '9', 'q0'], ['q0', '0', 'q1'], ['q0', '5', 'q1'], ['q1','0','q1'], ['q1','5','q1'],['q1','1','q0'],['q1','2','q0'],['q1','3','q0'],['q1','4','q0'],['q1','6','q0'],['q1','7','q0'],['q1','8','q0'],['q1','9','q0']]

AFD2 = [['0','1', '2', '3','4','5','6','7','8','9'], ['q0','q1'], 𝛿2, 'q0', ['q1']]


class Edge():
    def __init__(self, origin, simbol, destination):
        self.origin = origin
        self.destination = destination
        self.simbol = simbol

    def getOrigin(self):
        return self.origin

    def getDestination(self):
        return self.destination

    def setSimbol(self, simbol):
        self.simbol = simbol

    def getSimbol(self):
        return self.simbol

    def setOrigin(self, vertice):
        self.origin = vertice

    def setDestination(self, destination):
        self.destination = destination

    def __str__(self):
        return "A(%s----%s---->%s)" % (self.getOrigin(), self.getSimbol(), self.getDestination())


class Automaton:
    def __init__(self, AFD):
        self.Σ︀ = AFD[0]
        self.Q = AFD[1]
        self.𝛿 = AFD[2]
        self.q = AFD[3]
        self.f = AFD[4]
        self.lista_Arestas = []
        self.__inicialize()

    def __add_Edge(self, origin, simbol, destination):  # Método recebe dois identificadores
        self.lista_Arestas.append(Edge(origin, simbol, destination))

    def __search_Edge(self, v, s):
        for w in self.lista_Arestas:
            if w.getOrigin() == v and s == w.getSimbol():
                return w.getDestination()

    def __inicialize(self):
        for q in self.𝛿:
            self.__add_Edge(q[0], q[1], q[2])

    def process(self, word):
        q0 = self.q  # Whree q0 is a string
        while (len(word) != 0):
            print("𝛿(" + q0 + "," + ''.join(word) + ") =")
            if self.__search_Edge(q0, word[0]) is not None:  # Exist a transition
                w = word.pop(0)
                if (len(word)!=0):
                    print("𝛿(" + "(" + q0 + "," + w + ")," + ''.join(word) + ") =")
                else:
                    print("𝛿(" + "(" + q0 + "," + w + "),ε" + ''.join(word) + ") =")
                q0 = (self.__search_Edge(q0, w))  # receives a new destination
            else:
                print("𝛿(" + q0 + "," + ''.join(word) + ") = ε")
                return

        if self.f.count(q0) > 0:
            print("𝛿(" + q0 + ",ε) = "+''.join(self.f))
       


"""
automaton = Automaton(AFD1)
automaton.process(['a', 'b','b','b','b','a'])
"""


automaton = Automaton(AFD1)
automaton.process(['a', 'b','b','a','a','b','a','b','a','a'])


"""
automaton = Automaton(AFD1)
automaton.process(['a', 'b','a','b'])
"""               
              
                 
    
            
                
                
      
