# python_calc

# Python GUI using PyQt

## Install

##### PIP install PyQt5

## Test installation of PyQt5
#### import module
     
import sys  
from PyQt5.QtWidgets import QApplication  
from PyQt5.QtWidgets import QLabel  
from PyQt5.QtWidgets import QWidget  
    
#### Create GUI
app = QApplication(sys.argv)  
window = QWidget()  
window.setWindowTitle('PyQt5 App')  
window.setGeometry(100, 100, 280, 80)  
window.move(600, 15)  
helloMsg = QLabel('This is Test', parent=window)   
helloMsg.move(60, 30)  
window.show()  
    
    
#### Retain GUI Window


sys.exit(app.exec_())

# Calculator Using PyQt5 

## View of application
  
      
#### 1. Create view.py
     
#### 2. Import following modules

from PyQt5.QtCore import Qt  
from PyQt5.QtWidgets import QMainWindow      
from PyQt5.QtWidgets import QWidget    
from PyQt5.QtWidgets import QGridLayout    
from PyQt5.QtWidgets import QLineEdit    
from PyQt5.QtWidgets import QPushButton     
from PyQt5.QtWidgets import QVBoxLayout 

    
#### 3. Create GUI class and extend QMainWindow class

class GUI(QMainWindow):

 - ##### Add constructor and Parameter

    - SuperClass Constructor  
    - setWindowTitle  
    - setFixedSize  
    - generalLayout  
    - centralWidget  
    - createDisplayLED  
    - createButtons  

 - ##### Define Methods
   ##### (Which will create method for Display Panel, Buttons layout and method for set/get/clear display)

    - createDisplayLED()  
    - createButtons()  
    - setDisplayText()  
    - getDisplayText()  
    - clearDisplay()  


  

