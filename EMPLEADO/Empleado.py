from Fecha import Fecha

class Empleado:
    #Aqui va el codigo del Empleado
    '''-------------------
    #Atributos
    -------------------'''
    nombre=''
    apellido=''
    '''------------------
    #1= Masculino y 2= Femenino
    ------------------'''
    sexo=0
    salario=0
    '''-----------------------
    #Asociasiones
    -----------------------'''
    fechaNacimiento=Fecha()
    fechaIngreso=Fecha()

    '''-----------------------
    #Metodos
    -----------------------'''

    def CambiarSalario(self,nuevoSalario):
        #Aqui va el codigo del metodo
        return 0 
    def CambiarEmpleado(self,nNombre,nApellido,nSexo,nSalario):
        #Aqui va el codigo del nuevo empleado 
        return None
    def ConsultarSalario(self):
        #Aqui va el codigo del metodo
        return self.salario
    def  ConsultarNombre(self):
        return self.nombre
    def ConsultarApellido(self):
        return self.apellido
    def ConsultarNombreCompleto(self):
        return self.nombre 
    def AumentoSalarial(self):
        nSalario= self.slario=0.05
        nSalario= nSalario + self.salario
        self.salario=nSalario
    return "El nuevo slario es de "+self.salario
    def DuplicarSalario(self):
        #Aqui va el codigo 
        #Forma 1
        #self.salario = self.salario*2
        #Forma 2 pro
        self.salario *= 2
    def CalcularSalarioAnual(self):
        #Aqui va el codigo
        # Forma 1
    salarioAnual = self.salario*12
    return salarioAnual
    #Forma 2
    #return self.salario*12
    
    def ConsultarDiaCumpleaños(self):
        return ''El dia de su cumpleaños es: ''+self.fechaNacimiento.ConsultarDia()
    
    def CalcularImpuesto(self):

        #Forma 1
        total=self.CalcularSalarioAnual()
        return (total * 19,5) / 100
        #Forma 2
        #return self.CalcularSalarioAnual() * = 0.195
        

    
    
