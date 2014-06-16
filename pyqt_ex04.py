from PyQt4 import QtGui,QtCore


# How to display a maximized view in Qt












if __name__ == '__main__':

    import sys      #require for pasing the comand line arguments to Qt
    app = QtGui.QApplication(sys.argv)
    
    scene = QtGui.QGraphicsScene()  #Create a Scene to handle 2D graphics
    scene.addText("Hello world")    #add some text on scene

    view = QtGui.QGraphicsView(scene)   #QtGraphicsScene itself cannot do anything
   # view.show()     #create a GraphicsView and add scene to that view to display
    view.showMaximized()
    




    scene.setBackgroundBrush(QtCore.Qt.yellow)  #accessing the color 
    


    
    sys.exit(app.exec_())   #execute the app to display the gui 
    
