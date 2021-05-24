from tkinter import *
import math
import parser
import tkinter.messagebox

#main window geometry
root=Tk()
root.title("SciCalc")
root.config(background='Black')
root.resizable(width=False, height=False)
root.geometry("480x570+0+0")
calc = Frame(root)
calc.grid()


#main Class for calculator functions
class Calc():



    def __init__(self):
        self.total =0
        self.current = ''
        self.input_value=True
        self.check_sum = False
        self.op=''
        self.result=False


    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current= secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current)



    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())



    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)


    def valid_function(self):
        if self.op=='add':
            self.total +=self.current

        if self.op=='sub':
            self.total -=self.current

        if self.op=='multi':
            self.total *=self.current
            
        if self.op=='divide':
            self.total /=self.current
            
        if self.op=='mod':
            self.total %=self.current

        if self.op=='pow':
            self.total **= self.current
            
        if self.op=='inv':
            self.total = self.current**(-1)
            
        if self.op=='perc':
            self.total = (self.current/100*self.total)
           
        if self.op=='cubrt':
            self.total = self.current**(1/3)

        if self.op=='nth':
            self.total = self.current**(1/self.total)
            
        self.input_value=True
        self.check_sum=False
        self.display(self.total)


    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def clear_entry(self):
        self.result=False
        self.current='0'
        self.display(0)
        self.input_value=True
        
    def allclear_entry(self):
        self.clear_entry()
        self.total=0
        

    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)  

    def pi2(self):
        self.result=False
        self.current=(math.pi*2)
        self.display(self.current)

    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)


    def mathPM(self):
        self.result=False
        self.current= -(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result=False
        self.current= math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result=False
        self.current= math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result=False
        self.current= math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result=False
        self.current= math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result=False
        self.current= math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def squart(self):
        self.result=False
        self.current= math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def sinh(self):
        self.result=False
        self.current= math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def exp(self):
        self.result=False
        self.current= math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def log(self):
        self.result=False
        self.current= math.log(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result=False
        self.current= math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result=False
        self.current= math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result=False
        self.current= math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result=False
        self.current= math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result=False
        self.current= math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result=False
        self.current= math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result=False
        self.current= math.log1p(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result=False
        self.current= math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def gamma(self):
        self.result=False
        self.current= math.gamma(float(txtDisplay.get()))
        self.display(self.current)


    def fct(self):
        self.result=False
        self.current= math.factorial(float(txtDisplay.get()))
        self.display(self.current)

    def asin(self):
        self.result=False
        self.current= math.asin(float(txtDisplay.get()))
        self.display(self.current)

    def acos(self):
        self.result=False
        self.current= math.acos(float(txtDisplay.get()))
        self.display(self.current)

    def atan(self):
        self.result=False
        self.current= math.atan(float(txtDisplay.get()))
        self.display(self.current)
        
    def cubrt(self):
        self.result=False
        self.current= (float(txtDisplay.get()))**(1/3)
        self.display(self.current)

    def antilog(self):
        self.result=False
        self.current= 10**(float(txtDisplay.get()))
        self.display(self.current)
        
added_value=Calc()

txtDisplay = Entry(calc, font=('arial',20,'bold'), bg='gray',bd=30,width=28,relief=GROOVE, justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,'0')


#buttons formatting (grid format)
numberpad = "789456123"
i=0
btn=[]
for j in range (2,5):
    for k in range(3):
        btn.append(Button(calc, width=6,height=2,font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RAISED,text= numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]['command']=lambda x = numberpad [i]: added_value.numberEnter(x)
        i+=1













#+++++++++++++++++++++++++btns std+++++++++++++++++++++++++++++++++

btnClear=Button(calc, text='C',command=added_value.clear_entry,width=6,
height=2,font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RIDGE).grid(row=1,column=0, pady=1)

btnAllClear=Button(calc, text='AC',command=added_value.allclear_entry,width=6,
height=2,font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RIDGE).grid(row=1,column=1, pady=1)

btnSq=Button(calc, text='√',command=added_value.squart,width=6 ,height=2,
font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RIDGE).grid(row=2,column=8, pady=1)

btnAdd=Button(calc, text='+',width=6 ,command= lambda: added_value.operation('add'),
height=2,font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RIDGE).grid(row=1,column=3, pady=1)

btnSub=Button(calc, text='-',width=6 ,command= lambda: added_value.operation('sub'),
height=2,font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RIDGE).grid(row=2,column=3, pady=1)

btnMult=Button(calc, text='*',width=6 ,command= lambda: added_value.operation('multi'),
height=2,font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RIDGE).grid(row=3,column=3, pady=1)

btnDiv=Button(calc, text='÷',width=6 ,command= lambda: added_value.operation('divide'),
height=2,font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RIDGE).grid(row=4,column=3, pady=1)

btnZero=Button(calc, text='0',width=6 ,command= lambda: added_value.numberEnter(0),
height=2,font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RAISED).grid(row=5,column=0, pady=1)

btnDot=Button(calc, text='.',width=6 ,command= lambda: added_value.numberEnter('.'),
height=2,font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RIDGE).grid(row=5,column=1, pady=1)

btnPM=Button(calc, text='±',command=added_value.mathPM,width=6 ,height=2,
font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RIDGE).grid(row=5,column=2, pady=1)

btnEquals=Button(calc, text='=',command=added_value.sum_of_total,width=6 ,height=2,
font=('Gadugi',20,'italic'),bg='gray',bd=4,relief=RIDGE).grid(row=5,column=3, pady=1)




#+++++++++++++++++++++++++btns sci+++++++++++++++++++++++++++++++++



btnPi=Button(calc, text='π',width=6 ,
               command=added_value.pi,height=2,font=('Gadugi',20,'italic'),
               bg='gray',bd=4,relief=RAISED).grid(row=1,column=4, pady=1)
btnCos=Button(calc, text='cos',width=6 ,command=added_value.cos,height=2,font=('Gadugi',20,'italic'),
              bg='gray',bd=4,relief=RIDGE).grid(row=1,column=5, pady=1)

btntan=Button(calc, text='tan',width=6 ,
             command=added_value.tan,height=2,font=('Gadugi',20,'italic'),
             bg='gray',bd=4,relief=RIDGE).grid(row=1,column=6, pady=1)
btnsin=Button(calc, text='sin',width=6 ,
                 command=added_value.sin,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=1,column=7, pady=1)
btn2Pi=Button(calc, text='2π',width=6 ,
               command=added_value.pi2,height=2,font=('Gadugi',20,'italic'),
               bg='gray',bd=4,relief=RAISED).grid(row=2,column=4, pady=1)
btnCosh=Button(calc, text='Cosh',width=6 ,
              command=added_value.cosh,height=2,font=('Gadugi',20,'italic'),
              bg='gray',bd=4,relief=RIDGE).grid(row=2,column=5, pady=1)
btntanh=Button(calc, text='tanh',width=6 ,
             command=added_value.tanh,height=2,font=('Gadugi',20,'italic'),
             bg='gray',bd=4,relief=RIDGE).grid(row=2,column=6, pady=1)
btnsinh=Button(calc, text='sinh',width=6 ,
                 command=added_value.sinh,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=2,column=7, pady=1)
btnlog=Button(calc, text='ln',width=6 ,
               command=added_value.log,height=2,font=('Gadugi',20,'italic'),
               bg='gray',bd=4,relief=RIDGE).grid(row=3,column=4, pady=1)
btnExp=Button(calc, text='Exp',width=6 ,
                command=added_value.exp,height=2,font=('Gadugi',20,'italic'),
              bg='gray',bd=4,relief=RIDGE).grid(row=3,column=5, pady=1)
btnMod=Button(calc, text='Mod',width=6 ,
                command= lambda: added_value.operation('mod'), height=2,font=('Gadugi',20,'italic'),
             bg='gray',bd=4,relief=RIDGE).grid(row=3,column=6, pady=1)
btnE=Button(calc, text='e',width=6 ,
                 command=added_value.e,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RAISED).grid(row=3,column=7, pady=1)
btnlog2=Button(calc, text='log2',width=6 ,
               command=added_value.log2,height=2,font=('Gadugi',20,'italic'),
               bg='gray',bd=4,relief=RIDGE).grid(row=4,column=4, pady=1)
btndeg=Button(calc, text='deg',width=6 ,
              command=added_value.degrees,height=2,font=('Gadugi',20,'italic'),
              bg='gray',bd=4,relief=RIDGE).grid(row=4,column=5, pady=1)
btnacosh=Button(calc, text='acosh',width=6 ,
             command=added_value.acosh,height=2,font=('Gadugi',20,'italic'),
             bg='gray',bd=4,relief=RIDGE).grid(row=4,column=6, pady=1)
btnasinh=Button(calc, text='asinh',width=6 ,
                 command=added_value.asinh,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=4,column=7, pady=1)
btnlog10=Button(calc, text='log10',width=6 ,
               command=added_value.log10,height=2,font=('Gadugi',20,'italic'),
               bg='gray',bd=4,relief=RIDGE).grid(row=5,column=4, pady=1)
btnlog1p=Button(calc, text='log1p',width=6 ,
              command=added_value.log1p,height=2,font=('Gadugi',20,'italic'),
              bg='gray',bd=4,relief=RIDGE).grid(row=5,column=5, pady=1)
btnexpm1=Button(calc, text='expm1',width=6 ,
             command=added_value.expm1,height=2,font=('Gadugi',20,'italic'),
             bg='gray',bd=4,relief=RIDGE).grid(row=5,column=6, pady=1)
btnlgamma=Button(calc, text='lgamma',width=6 ,
                 command=added_value.lgamma,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=5,column=7, pady=1)
btnxy=Button(calc, text='x^y',width=6 ,
                 command=lambda: added_value.operation('pow'),height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=0,column=4, pady=1)
btnxfact=Button(calc, text='x!',width=6 ,
                 command=added_value.fct,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=0,column=5, pady=1)
btnarccos=Button(calc, text='acos',width=6 ,
                 command=added_value.acos,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=0,column=6, pady=1)
btnarcsin=Button(calc, text='asin',width=6 ,
                 command=added_value.asin,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=0,column=7, pady=1)
btnarctan=Button(calc, text='atan',width=6 ,
                 command=added_value.atan,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=0,column=8, pady=1)
btninv=Button(calc, text='x^(-1)',width=6 ,
                 command=lambda: added_value.operation('inv'),height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=1,column=8, pady=1)
btnperc=Button(calc, text='%',width=6 ,
                 command=lambda: added_value.operation('perc'),height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=1,column=2, pady=1)
bt3rdroot=Button(calc, text='x^1/3',width=6 ,
                 command=added_value.cubrt,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=3,column=8, pady=1)
btnthroot=Button(calc, text='x^1/y',width=6 ,
                 command=lambda: added_value.operation('nth'),height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=4,column=8, pady=1)
btnantilog=Button(calc, text='anti\nlog',width=6 ,
                 command=added_value.antilog,height=2,font=('Gadugi',20,'italic'),
                 bg='gray',bd=4,relief=RIDGE).grid(row=5,column=8, pady=1)












#+++++++++++++++++++++++++++Menu++++++++++++++++++++++++++++++++

def exitm():
    exitm = tkinter.messagebox.askyesno("SciCalc","Do you want to exit?")
    if exitm > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("1000x570+0+0")

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x550+0+0")


menubar = Menu(calc)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "Mode",menu=filemenu)
filemenu.add_command(label= "Standard",command=Standard)
filemenu.add_command(label= "Scientific",command=Scientific)

menubar.add_cascade(label= "Exit", command = exitm)

menubar.add_cascade(label = "Help")



root.config(menu=menubar)

root.mainloop()
