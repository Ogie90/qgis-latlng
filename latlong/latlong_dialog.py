
import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads my .ui file so that PyQt can populate my plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'latlong_dialog_base.ui'))


class latlongDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
     
        super(latlongDialog, self).__init__(parent)
       
        self.setupUi(self)

        self.spbLatD.valueChanged.connect(self.latDMStoDD)
        self.spbLatM.valueChanged.connect(self.latDMStoDD)
        self.spbLatS.valueChanged.connect(self.latDMStoDD)

        #za hemisferu
        self.cmbLatH.currentTextChanged.connect(self.latDMStoDD)

        self.spbLngD.valueChanged.connect(self.lngDMStoDD)
        self.spbLngM.valueChanged.connect(self.lngDMStoDD)
        self.spbLngS.valueChanged.connect(self.lngDMStoDD)

        #za hemisferu
        self.cmbLatH.currentTextChanged.connect(self.latDMStoDD)


        self.spbLatDD.editingFinished.connect(self.latDDtoDMS)
        self.spbLngDD.editingFinished.connect(self.latDDtoDMS)


    def latDMStoDD(self):
        iDeg = self.spbLatD.value()
        iMin = self.spbLatM.value()
        dSec = self.spbLatS.value()
        sHem = self.cmbLatH.currentText()

        dDD = float(iDeg) + iMin/60 + dSec/360
        if sHem == "S":
            dDD = dDD * -1

        self.spbLatDD.setValue(dDD)


        
    def lngDMStoDD(self):
        iDeg = self.spbLngD.value()
        iMin = self.spbLngM.value()
        dSec = self.spbLngS.value()
        sHem = self.cmbLngH.currentText()

        dDD = float(iDeg) + iMin/60 + dSec/360
        if sHem == "W":
            dDD = dDD * -1

        self.spbLngDD.setValue(dDD)



# za vacanje nazad, konvertovanje iz DD u DMS#

    def latDDtoDMS(self): 
        dDD = self.spbLatDD.value()

        iDeg = int(dDD)
        dMin = (dDD-iDeg) *60 #da bi se dobile minute
        iMin = int(dMin)
        dSec = (dMin-iMin) * 60

        self.spbLatD.setValue(abs(iDeg))
        self.spbLatM.setValue(abs(iMin))
        self.spbLatS.setValue(abs(dSec))

        if dDD <0:
            self.cmbLatH.setCurrentText("S")
        else:
            self.cmbLatH.setCurrentText("N")

    def lngDDtoDMS(self): 
        dDD = self.spbLngtDD.value()

        iDeg = int(dDD)
        dMin = (dDD-iDeg) *60 #da bi se dobile minute
        iMin = int(dMin)
        dSec = (dMin-iMin) * 60

        self.spbLngD.setValue(abs(iDeg))
        self.spbLngM.setValue(abs(iMin))
        self.spbLngS.setValue(abs(dSec))

        if dDD <0:
            self.cmbLngH.setCurrentText("W")
        else:
            self.cmbLngH.setCurrentText("E")


