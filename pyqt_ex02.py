from PyQt4 import QtGui,QtCore









if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    scene = QtGui.QGraphicsScene()
    scene.addText("Hello world")

    view = QtGui.QGraphicsView(scene)
    view.show()
    sys.exit(app.exec_())
    
