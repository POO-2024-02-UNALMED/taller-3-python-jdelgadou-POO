class Control:
    def __init__(self):
        self._tv=0
    def enlazar(self, TV):
        self._tv=TV
        TV.setControl(self)
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.CanalDown()
    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()
    def setTv(self, TV):
        self._tv=TV
    def getTv(self):
        return self._tv