#Library
from tkinter import *
import random
from tkinter import messagebox
                                                     #Screen Showing  using tkinter
screen = Tk()
screen.title("Matching Pairs Game......")
screen.iconbitmap('brain.ico') # Logo
screen.maxsize(height="400",width="400") #SIZE OF A DISPLAY

                                                               #CREATING  PAIRS 
pairs = [1,1,2,2,3,3,4,4,5,5,6,6]
# Shuffle Our pairs
random.shuffle(pairs)
# print(pairs) # Checking the shuffles values

#Create a frame for button
my_frame=Frame(screen)
my_frame.pack(pady=5) 

                                                                #Variables
count=0
win=0
attempts=0
ans_list=[]
ans_dict={}

                                                                #FUNCTIONS
#RESET fUNCTION
def reset():
    global pairs, win, my_label, btn_list, attempts
    win =0
    attempts=0
    random.shuffle(pairs)
    my_label.config(text=" ")
    for i in btn_list:
        i.config(text =" ", state="normal", bg="SystemButtonFace")

#BUTTON CLICK FUNCTION
def button_click(b,number):
    global count,ans_list,ans_dict,attempts
    if b["text"]==' 'and count <2:
        b["text"]=pairs[number]    
        # Add Number to ans_list i.e index
        ans_list.append(number)
        # Add number to ans_dict I.e value and index
        ans_dict[b]=pairs[number]
                                                     #Adding Emojis for Dict Values
        for i in ans_dict.values():
            if i == 1:
                b["text"] = "\U0001F352"  #cherry
            elif i==2:
                b["text"] = "\U0001f600"  #smiling face
            elif i==3:
                b["text"] = "\U0001F30E"  #earth
            elif i==4:
                b["text"] = "\U0001F378"  #drink
            elif i==5:
                b["text"] = "\U0001F47B"  #ghost
            elif i==6:
                b["text"] = "\U0001F33B"  #flower  
        #Icremnt counter
        count+=1
        # print(ans_list)#Print list 
        # print(ans_dict)#print dict

    #START TO DETEMINE CORRECT OR NOT
    if len(ans_list)==2:
         # checking the match
        attempts+= 1
         # print(attempts)
        if pairs[ans_list[0]] == pairs[ans_list[1]]:
            my_label.config(text = "MATCH..... attempt:"+ str(attempts))
            
            for key in ans_dict:
                key["state"]='disabled'
                key.config(bg="lavender")
                
            count=0
            ans_list=[]
            ans_dict={}
            #Checking  The Winning No.
            global win
            win += 1
            if(win == 6):
                my_label.config(text="GAME OVER !") 
                ANSWER = messagebox.askquestion("Number of attempts : " + str(attempts),"Do you want to play again??")
                if ANSWER == 'no':    
                    screen.quit()
                else:
                    reset()
        else:
            my_label.config(text="Oops....No Match ,attempt:"+ str(attempts))
            count=0
            ans_list = []
            #CREATE POP UP
            messagebox.showinfo('WRONG..',"oops!! No Match, press enter to continue")
            
            

            #Reset the butons
            for k in ans_dict:
                k["text"]=" "
            ans_dict={}





        

#Buttons
b0=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b0,0),relief="groove")
b1=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b1,1),relief="groove")
b2=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b2,2),relief="groove")
b3=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b3,3),relief="groove")

b4=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b4,4),relief="groove")
b5=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b5,5),relief="groove")
b6=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b6,6),relief="groove")
b7=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b7,7),relief="groove")

b8=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b8,8),relief="groove")
b9=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b9,9),relief="groove")
b10=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b10,10),relief="groove")
b11=Button(my_frame,text=' ',font=("arial",18),height=3,width=6,command=lambda: button_click(b11,11),relief="groove")

#btn list
btn_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]

#Grid the Buttons
#1st row
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)

#2nd row
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)

#3rdrow
b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)


# Below Label
my_label=Label(screen,text="")
my_label.pack(pady=20)

#Execution
screen.mainloop()

