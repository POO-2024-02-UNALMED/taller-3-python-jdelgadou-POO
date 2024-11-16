from __future__ import annotations
class TV:
    _numTV=0
    def __init__(self,Marca,estado):
        self._marca=Marca
        self._estado=estado
        self._canal=1
        self._precio=500
        self._volumen=1
        self._control=0
        TV._numTV+=1
    def getMarca(self):
        return self._marca
    def getCanal(self):
        return self._canal
    def getPrecio(self):
        return self._precio
    def getVolumen(self):
        return self._volumen
    def getControl(self):
        return self._control
    @classmethod
    def getNumTV(cls):
        return TV.numTV
    def getEstado(self):
        return self._estado
    def setMarca(self,Marca):
        self._marca=Marca
    def setCanal(self,canal):
        if self._estado==True and 1<=canal<=120:
            self._canal=canal
    def setPrecio(self,precio):
        self._precio=precio
    def setVolumen(self,volumen):
        if self._estado==True and 0<=volumen<=7:
            self._volumen=volumen
    def setControl(self,Control):
        self._control=Control
    @classmethod
    def setNumTV(cls, numero):
        TV.numTV=numero
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    def canalUp(self):
        if self._estado==True and 1<=self._canal<120:
                self._canal+=1
    def canalDown(self):
        if self._estado==True and 1<self._canal<=120:
                self._canal-=1
    def volumenUp(self):
        if self._estado==True and 0<=self._volumen<7:
                self._volumen+=1
    def volumenDown(self):
        if self._estado==True and 1<self._volumen<=7:
                self._volumen-=1