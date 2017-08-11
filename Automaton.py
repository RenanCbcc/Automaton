# -*- coding: utf-8 -*-
𝛿  = [['q0','a', 'q1'],['q1', 'a', 'qf'],['q0', 'b', 'q2'],['q1', 'b', 'q2'],['q2','a','q1'],['q2','b','qf'],['qf','a','qf'],['qf','b','qf']]
AFD = [['a', 'b'], ['q0', 'q1', 'q2', 'qf'], 𝛿, 'q0', ['qf']]

class Edge():
	def __init__(self,origin,simbol,destination):
		self.origin = origin
		self.destination = destination
		self.simbol = simbol
				
	def getOrigin(self):
		return self.origin
		
	def getDestination(self):
		return self.destination
	
	def setSimbol(self,simbol):
		self.simbol = simbol
		
	def	getSimbol(self):
		return self.simbol
		
	def setOrigin(self,vertice):
		self.origin = vertice
		
	def setDestination(self,destination):
		self.destination = destination
	
	def __str__(self):
         return "A(%s----%s---->%s)" % (self.getOrigin(),self.getSimbol(),self.getDestination())
         
    
class Automaton:
    def __init__(self,AFD):
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
            if  w.getOrigin() == v and s == w.getSimbol():
                return w.getDestination()
    
    def __inicialize(self):
      for q in self.𝛿:
        self.__add_Edge(q[0],q[1],q[2])
    
    def process(self,word):        
        q0 = self.q # Whree q0 is a string
        while(len(word)!=0):
          print("𝛿("+q0+","+''.join(word)+") =")
          if self.__search_Edge(q0,word[0]) is not None: #Exist a transition
            w = word.pop(0)
            print("𝛿(" + "("+q0+","+w+"),"+''.join(word)+") =")
            q0 = (self.__search_Edge(q0,w)) # receives a new destination
          else:
            print("𝛿("+q0+","+''.join(word)+") = ε")
            return
            
        if self.f.count(q0) > 0:
          print("𝛿("+q0+ ",ε) = qf")
                
            
automaton = Automaton(AFD)     
automaton.process(['a','b','a','a'])                     
              
                 
    
            
                
                
      