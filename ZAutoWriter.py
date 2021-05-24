#Auto Writer
#1-Letter to the Editor
#2-Letter Cancelling order
#3-Business Letter

import tkinter


def hi():
    print(startEntry2.get())
    print()
    print(startEntry3.get())
    print()
    print(startEntry1.get())
    print()
    print('Subject:', startEntry4.get())   #sample format for a letter to the editor
    print('Dear Editor,\n\nI am',startEntry.get(),'''.member of NGO AWAAZ. I am writing to you in
order to highlight the deteriorating condition of river Yamuna.
The city of Delhi is getting contaminated water from river Yamuna.
The residents are to be blamed for this. They pollute the river with
garbage, sewage and filth. The river water is full of bacteria, plastic,
chemicals and other waste materials. It is unfit for consumption.
The people have been demanding a Water Treatment plant.
The authorities have not yet responded to the repeated requests.
\nI request you to highlight the problem in your newspaper and arouse public interest. We
all need to get together in order to get the plant set up in the
area.\n\nThank You\nYours sincerely\n''',startEntry.get(),'\nMember AWAAZ')

def hii():
    print(startEntry2.get())
    print()
    print(startEntry3.get())
    print()
    print(startEntry1.get())
    print()
    print('Subject:', startEntry4.get()) #sample format for letter of cancellation
    print('Sir,\n\nI am',startEntry.get(),'''. I am writing to you to inform that I would
like to cancel the order of 13 physics textbooks
which was placed earlier this week. The order number is 2144v.
The school has decided to provide books by themselves,
and hence I won’t be needing them.Please send the refund
amount by cheque to the address mentioned below. I am incredibly
sorry for all the trouble and inconvenience caused.\n\n',
'Yours sincerely,\n''',startEntry.get())

def hiii():
    print(startEntry2.get())
    print()
    print(startEntry3.get())
    print()
    print(startEntry1.get())
    print()
    print('Subject:', startEntry4.get()) #sample format for a letter to the editor
    print('Sir,\n\nI am',startEntry.get(),'''. Thank you so much for taking the time to
          meet with me to discuss selling my handmade sweaters
          in your wonderful shop. We discussed a trial consignment
          arrangement in which a portion of the sales would go
          to the store. This is more than agreeable to me.
          Let me know how you want to proceed. I’m
          available most afternoons at 555-555-5555,
          or you can email me at email@email.com, and I’ll respond to
          your message ASAP. \n\n','Yours sincerely,\n''',startEntry.get())


#designing the GUI
    
root=tkinter.Tk()
root.geometry('200x400')
startLabel =tkinter.Label(root,text="Enter Name:")
startEntry=tkinter.Entry(root)

startLabel1 =tkinter.Label(root,text="Enter Receiver's Address:")
startEntry1=tkinter.Entry(root)

startLabel2 =tkinter.Label(root,text="Enter Sender's Address:")
startEntry2=tkinter.Entry(root)

startLabel3 =tkinter.Label(root,text="Date")
startEntry3=tkinter.Entry(root)

startLabel4 =tkinter.Label(root,text="Subject:")
startEntry4=tkinter.Entry(root)

startLabel5 =tkinter.Label(root,text="Receiver's name:")
startEntry5=tkinter.Entry(root)


startLabel.pack()
startEntry.pack()

startLabel1.pack()
startEntry1.pack()

startLabel2.pack()
startEntry2.pack()

startLabel3.pack()
startEntry3.pack()

startLabel4.pack()
startEntry4.pack()

startLabel5.pack()
startEntry5.pack()

enterButton= tkinter.Button(root,text="Letter to the editor", command=hi)
CoolButton= tkinter.Button(root,text="Letter cancelling order", command=hii)
SupercoolButton=tkinter.Button(root, text="Business Letter",command=hiii)

enterButton.pack()
CoolButton.pack()
SupercoolButton.pack()

root.mainloop()
