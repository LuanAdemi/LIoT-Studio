import time
import serial
from sys import *

variables = {}
try:
    ser = serial.Serial(argv[2], 9600)
except:
    print "Kommunikationsfehler --> Ist der Arduino eingesteckt :D?"
    exit()

class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        #print(self.value.eval())
        string = self.value.eval()
        ser.write("PRINTTOLCD" + string.replace("\"",""))

class Sleep():
    def __init__(self, value):
        self.value = value

    def eval(self):
        time.sleep(float(self.value.eval()))

class String():
     def __init__(self, value):
        self.value = value

     def eval(self):
        return str(self.value)

class Output():
     def __init__(self, value):
        self.value = value

     def eval(self):
        #print(self.value.eval())
        string = self.value.eval()
        ser.write("OUTPUT" + str(string))

class PinOn():
     def __init__(self, value):
        self.value = value

     def eval(self):
        #print(self.value.eval())
        string = self.value.eval()
        ser.write("PINON" + str(string))

class PinOff():
     def __init__(self, value):
        self.value = value

     def eval(self):
        #print(self.value.eval())
        string = self.value.eval()
        ser.write("PINOFF" + str(string))

class setVar():
     def __init__(self,name,value):
         self.name = name
         self.value = value
     def eval(self):
         variables[str(self.name.eval())] = self.value.eval()
         #print(variables)
         
         

class getVar():
     def __init__(self,name):
         self.name = name

     def eval(self):
         #print(variables[self.name.eval()])
         return variables[self.name.eval()]

class Letter():
     def __init__(self, value):
        self.value = value

     def eval(self):
         if(self.value in variables):
            return variables[self.value]
         else:
            return str(self.value)

class Empty():
     def __init__(self, value):
        self.value = value

     def eval(self):
         return


class Loop():
     def __init__(self, value):
        self.value = value

     def eval(self):
         while True:
             self.value.eval()

class Read():
     def __init__(self, value):
        self.value = value

     def eval(self):
         while True:
             ser.read(10)  

class IfStatement():
      def __init__(self, expression1,expression2,program):
        self.expression1 = expression1
        self.expression2 = expression2
        self.program = program

      def eval(self):
         if(self.expression1.eval() == self.expression2.eval()):
             self.program.eval()
        
             
         
