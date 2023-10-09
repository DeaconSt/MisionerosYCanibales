import copy 
import os
class Estado:
    def __init__(self, estado, canoa):
        self.estado = estado
        self.canoa = canoa

        if not self.es_valido():
            raise ValueError('Estado no valido')

    def es_valido(self):

        for gente in self.estado:
            for persona in gente:
                if persona >3 or persona <0:
                    return False

        for misionero, canoa in self.estado:
            if misionero and canoa > misionero:
                return False
        return True

    def viaja(self, gente):

        estado=copy.deepcopy(self.estado)

        canoa=self.canoa
        estado[canoa][0] -= gente[0]

        estado[canoa][1] -= gente[1]

        canoa =0 if canoa else 1
        
        estado[canoa][0] += gente[0]
        estado[canoa][1] += gente[1]

        return Estado(estado, canoa)

    def __str__(self):

        return "misioneros: %d canibales: %d | %s\\__/%s | misioneros: %d canibales: %d" % (
            
            self.estado[0][0],
            self.estado[0][1],
            "~" *5 *self.canoa,
            "~" *(5 - 5 * self.canoa),
            self.estado[1][0],
            self.estado[1][1],

        )

    def __eq__(self, other):

        return self.estado == other.estado and self.canoa == other.canoa

    def __ne__(self, other):

        return not self.__eq__(other)

def main():

    os.system("clear")
    inicio=Estado([[3,3],[0,0]], 0)

    final=Estado([[0,0],[3,3]], 1)


    viajes= [ [1,0], [0,1], [1,1], [2,0], [0,2] ]

    viajes_posibles=list(viajes)

    recorrido=[]
    viajes_restantes=[]

    while inicio != final and viajes_posibles:
        while viajes_posibles:

            viaje=viajes_posibles.pop()

            try:
                nuevo=inicio.viaja(viaje)

                if nuevo not in recorrido:
                    recorrido.append(inicio)
                    viajes_restantes.append(viajes_posibles)

                    inicio=nuevo
                    viajes_posibles=list(viajes)
            except ValueError:

                pass

        if not viajes_posibles and recorrido:
            inicio=recorrido.pop()
            viajes_posibles=viajes_restantes.pop()
    
    if inicio ==final:
        print("Se ha encontrado una solucion")
        for estado in recorrido:
            print(estado)
        print(inicio)

    else:
        print("No se ha encontrado una solucion")

if __name__ == "__main__":
    main()

