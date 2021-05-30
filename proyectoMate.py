from __future__ import annotations
from typing import List, Set, Tuple

class Relacion:
             
    """
        @author Kevin Jimenez
        @date   25/05/2021
        @todo   Cosas que falten por arreglar/mejorar (si fuera necesario)
        @note   Se agrego la funcionalidad: Si el codominio no se especifica  se le asigna el dominio:
                Keiner Sebastian Castro Roman 29/05/2021
        @param dominio: List[int]    Breve descripcion (si hiciera falta)
        @param codominio: List[int]  Breve descripcion (si hiciera falta)
        @param grafico: Set[tuple]   Breve descripcion (si hiciera falta)
        @return Lo que devuelve.
    """
    def __init__(self, dominio: List[int], codominio: List[int], grafico: Set[tuple]) -> None:
        self.dominio = dominio
        self.matriz: List[List] = list()
        
        if (codominio == []):
            self.codominio = dominio
        else:
            self.codominio = codominio
        
        self.grafico = grafico

        for i in range(len(self.dominio)):
            self.matriz.append([])
            for j in range(len(self.codominio)):
                self.matriz[i].append(0)
        for e in self.grafico:
            try:
                self.matriz[self.dominio.index(e[0])][self.codominio.index(e[1])] = 1
            except ValueError:
                print(f"No se pudo agregar {e}")


    def __neg__(self):
        return "asd"

    """ 
        @author Keiner Sebastian Castro Roman
        @date   29/05/2021
    """
    def __invert__(self) -> Set[Tuple]:
        inversa: Set[Tuple] = set()
        for x in self.grafico:
            inversa.add((x[1],x[0]))
        return inversa

    def __or__(self,other: Relacion) -> Set[Tuple] | None:
        if(self.codominio == other.codominio):
            return self.grafico | self.grafico
        print("Las funciones no comparten codominio")
        return None


    def __and__(self,other: Relacion) ->  Set[Tuple]:
        return self.grafico & other.grafico


    def __sub__(self, other:  Relacion) ->  Set[Tuple]:
        return self.grafico - other.grafico

    
    def __mul__(self,other:  Relacion):
        pass
        

    def __LE__(self,o):
        pass

    #-------------------------------------------------------
    # METODOS
    """ 
        Metodo para imprimir la matriz de la Relacion
        @author Keiner Sebastian Castro Roman
        @date   25/05/2021
    """
    def imprime_matriz(self) -> None:   
        encabezado = "     "
        for i in self.codominio:
            encabezado = encabezado + str(i) + "  "
        print(encabezado) 
        print("---------------") 

        for i,d in enumerate(self.dominio):
            f = str(d) + " |  "
            for j in range(len(self.codominio)):
                f += str(self.matriz[i][j]) + "  "
            print(f)    
    
    def es_simetrica(self):
        pass

    def es_reflexiva(self):
        pass

    def es_transitiva(self):
        pass

    def es_total(self):
        pass

    def es_equivalencia(self):
        pass
    
    def es_orden(self):
        pass

    def clase_equivalencia(self, x):
        pass

    def clases_equivalencia(self):
        pass


A = Relacion([1, 2, 3, 4], [2, 4, 6, 8], {(1,2), (1,6), (2,2), (3,4), (3,6), (4,2), (4,8)})
B = Relacion([1, 2, 3, 4], [], {(1,1), (2,2), (3,3), (4,4)})
C = Relacion([1, 2, 3, 4], [], {(1,2), (2,1), (3,1), (1,3)})

D = B | C
print(D)