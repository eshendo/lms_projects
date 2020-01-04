import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui_file import Ui_MainWindow
from math import pow, sqrt


class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ops = []
        self.nums = []
        self.pred = None
        self.unr = False
        self.operations = ["+", "-", "/", "*", "@", "^", "!"]
        self.btns = [
                     self.pushButton_10, self.text,  self.pushButton,
                     self.pushButton_7, self.pushButton_2, self.pushButton_4,
                     self.pushButton_3, self.text1, self.pushButton_5, self.pushButton_9,
                     self.pushButton_6, self.pushButton_11, self.pushButton_12,  self.pushButton_8,
                     self.pushButton_13,  self.pushButton_14, self.pushButton_15,  self.pushButton_12
                    ]


        for btn in self.btns:
            btn.clicked.connect(self.pressed)

        self.pushButton_17.clicked.connect(lambda: self.label.setText(""))

    def pressed(self):
        op = self.sender().text()
        if op in self.operations and self.pred not in self.operations:
            if self.nums != []:
                print(self.nums)
                if len(self.nums) == 2 and len(self.ops) == 1:
                    num = self.calculate()
                    if num != "Devision by 0":
                        self.label.setText(str(num) + op)
                        self.nums = [str(num)]
                        self.ops = [op]
                    else:
                        self.label.setText(num + " Press C")
                        self.nums = []
                        self.ops = []
                    self.pred = op

                else:
                    self.label.setText(self.label.text() + op)
                    self.ops.append(op)
                self.pred = op
                self.unr = 0
                
            elif op == "-":
                self.unr = True
                self.nums.append("-")
                self.label.setText(self.label.text() + op)
                self.pred = op
    
        elif op == "-":
            self.unr = True
            self.nums.append("-")
            self.label.setText(self.label.text() + op)
            self.pred = op

        else:
            if op not in self.operations:
                if (self.pred in self.operations or self.nums == []) and self.unr == 0:
                    self.nums.append(op)
                else:
                    self.nums[-1] += op
                self.label.setText(self.label.text() + op)
                self.pred = op
                self.unr = 0


    def calculate(self):
        if self.ops[0] == "+":
            return int(self.nums[0]) + int(self.nums[1])
            
        elif self.ops[0] == "-":
            return int(self.nums[0]) - int(self.nums[1])
            
        elif self.ops[0] == "*":
            return int(self.nums[0]) * int(self.nums[1])
            
        elif self.ops[0] == "/":
            try:
                return int(self.nums[0]) // int(self.nums[1])
                
            except:
                return "Devision by 0"
        

    def rec(self, nums, opers):
        new_opers = opers[1:]
        if opers[0] == "+":
            new_nums = nums[2:]
            new_nums.insert(0, int(nums[0])+int(nums[1]))
            
        elif opers[0] == "-":
            new_nums = nums[2:]
            new_nums.insert(0, int(nums[0])-int(nums[1]))
            
        elif opers[0] == "*":
            new_nums = nums[2:]
            new_nums.insert(0, int(nums[0])*int(nums[1]))
            
        elif opers[0] == "/":
            try:
                new_nums = nums[2:]
                new_nums.insert(0, int(nums[0])/int(nums[1]))
                
            except:
                return "Devision by 0"
        elif opers[0] == "!":
            res = 1
            for i in range(1, int(nums[0])+1):
                res*=i
            new_nums = nums[1:]
            new_nums.insert(0, res)

        elif opers[0] == "^":
            new_nums = nums[2:]
            new_nums.insert(0, pow(int(nums[0]), int(nums[1])))
            
        elif opers[0] == "unr":
            new_nums = nums[1:]
            new_nums.insert(0, -int(nums[0]))
           
        elif opers[0] == "@":
            try:
                new_nums = nums[1:]
                new_nums.insert(0, sqrt(int(nums[0])))
                
            except:
                return "Error"

        if len(new_nums) == 1:
            return new_nums[0]
        return self.rec(new_nums, new_opers)


        





app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
