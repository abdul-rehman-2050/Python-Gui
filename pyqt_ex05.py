from PyQt4 import QtGui,QtCore


# another method of maximizing Qt view + radial gradient background 












if __name__ == '__main__':

    import sys      #require for pasing the comand line arguments to Qt
    app = QtGui.QApplication(sys.argv)
    
    scene = QtGui.QGraphicsScene()  #Create a Scene to handle 2D graphics
    scene.addText("Hello world")    #add some text on scene

    view = QtGui.QGraphicsView(scene)   #QtGraphicsScene itself cannot do anything
    view.show()     #create a GraphicsView and add scene to that view to display
    view.setWindowState(QtCore.Qt.WindowMaximized) 
   
    




    
    gradient = QtGui.QRadialGradient(0,0,10)
    gradient.setSpread(QtGui.QGradient.RepeatSpread)
    scene.setBackgroundBrush(gradient)

                       
    


    
    sys.exit(app.exec_())   #execute the app to display the gui 
    
