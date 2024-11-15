from .tv import TV
class Control:
    def __init__(self):
        self._tv=None
    def enlazar(self, tv):
        self._tv=tv
        TV.setControl(self)
    def turnOn(self):
        TV.turnOn()
    def turnOff(self):
        TV.turnOff()
    def canalUp(self):
        TV.canalUp()
    def canalDown(self):
        TV.CanalDown()
    def volumenUp(self):
        TV.volumenUp()
    def volumenDown(self):
        TV.volumenDown()
    def setTv(self, tv):
        self._tv=tv
    def getTv(self):
        return self._tv