class SimuladorBancario :
    '''--------------------
    #Atributos
    --------------------'''
    Cedula=0
    Nombres=''
    MesActual=0
    '''--------------------------------------
    # 1= TipoNormal 2=TipoPlatino y 3=TipoVip
    --------------------------------------'''
    Tipocliente=0
    '''---------------------------------
    #Metodos
    ---------------------------------'''

  Def __init__ (self,Cedula,Nombres,Tipocliente):
        self.Cedula=Cedula
        self.Nombres=Nombres
        self.TipoCliente=TipoCliente
        
    def CambiarTipocliente(self,NuevoTipocliente)
        #Aqui va el codigo del cliente
        self.Tipocliente=NuevoTipocliente
        return 'El Tipocliente se ha actualizado'+self.Tipocliente
    
    def CambiarCliente(self,nCedula,nNombres,nTipodeCliente)
        #Aqui va el codigo del nuevo cliente
        return None
        
    def ConsultarNombres(self):
        return self.Nombres
        
    def ConsultarCedula(self):
        #Aqui va el codigo del metodo
        return self.Cedula

    def ConsignarCuentaCorriente(self, monto):
        self.corriente.ConsignarMonto(monto)
        
    def CalcularSaldoTotal(self):
        # Forma1
        return self.corriente.ConsultarSaldo()+self.ahorros.ConsultarSaldo()

        # #Forma2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # saldoCorriente = self.corriente.ConsultarSaldo()
        # return saldoAhorros+saldoCorriente
        
    def PasarAhorrosACorriente(self):
        # forma1
        # self.corriente.ConsignarMonto(self.ahorros.ConsultarSaldo())
        # self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        # forma 2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # self.ConsignarCuentaCorriente(saldoAhorros)
        # self.ahorros.RetirarMonto(self, saldoAhorros)
        
        #forma 3
        saldoAhorros = self.ahorros.ConsultarSaldo()
        self.corriente.saldo += saldoAhorros
        self.ahorros.saldo = 0
        
    def ConsultarSaldoCorriente(self):
        return "Tu saldo es: "+self.corriente.ConsultarSaldo()
    
    def DuplicarAhorro(self):
        #forma 1
        self.ahorros.ConsignarMonto(self.ahorros.ConsultarSaldo())
        
        # # Forma 2
        # self.ahorros.saldo *= 2
    
    def RetirarTodo(self):
        total = self.CalcularSaldoTotal()
        self.corriente.RetirarMonto(self.corriente.ConsultarSaldo())
        self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        return "Retiraste total: "+total


   
