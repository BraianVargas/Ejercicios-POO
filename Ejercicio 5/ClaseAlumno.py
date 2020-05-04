class Alumno:
    __Nombre=None
    __Año=None
    __Division=None
    __Inacistencias=None

    # Variables de clase
    __InacMax=15
    __TotalClases=190

    # Constructor
    def __init__(self, nom,año,div,inac):
        self.__Nombre=nom
        self.__Año=año
        self.__Division=div
        self.__Inacistencias=inac

    # Metodos De clase
    @classmethod 
    def getMaxInac(cls):
        return cls.__InacMax
    @classmethod
    def getTotalClases(cls):
        return cls.__TotalClases
    @classmethod
    def setTotalClases(cls,total):
        cls.__TotalClases=total
    
    def Porcentaje(self, año, div, ban):
        porcent=0.0
        nom=''
        if(int(self.__Año)==año):
            if(int(self.__Division)==div):
                if(int(self.__InacMax) < int(self.__Inacistencias)):
                    try:
                        porcent = ( int(self.__Inacistencias) * 100 ) / (self.__InacMax)
                    except ZeroDivisionError:
                        porcent = ( int(self.__Inacistencias) * 100 )
                    nom=self.__Nombre
                    if(ban==1):
                        return (porcent)
                    else:
                        return nom

    @classmethod
    def ModificaMaximo(cls, max):
        cls.__InacMax=max
        print("Se modificó correctamente la cantidad de asistencias")

    def Mostrar(self):
        print('Nombre: {}'.format(self.__Nombre))
        print('Año: {}°'.format(self.__Año))
        print('Division: {}°'.format(self.__Division))
        print('Inasistencias: {}'.format(self.__Inacistencias))
        print('Maximas inasistencias permitidas: {}'.format(self.__InacMax))
        print('Total de clases: {}'.format(self.__TotalClases))
    