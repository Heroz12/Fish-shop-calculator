# GUI-calculator.py


from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk() # T ตัวใหญ่ k ตัวเล็ก
GUI.title('โปรแกรมคำนวณราคาปลา รถพุ่มพวง')
GUI.geometry('700x600')

bg = PhotoImage(file='car.png')

BG = Label(GUI,image=bg)
BG.pack()

L1 = Label(GUI,text='กรุณากรอกจำนวนราคากิโลกรัม',font=(None,20))
L1.pack()

v_quantity1 = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity1, font=(None,20))
E1.pack()

L2 = Label(GUI,text='กรุณากรอกจำนวนปลา',font=(None,20))
L2.pack()

v_quantity2 = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E2 = ttk.Entry(GUI, textvariable= v_quantity2, font=(None,20))
E2.pack()

def cal():
	try:
		quan = float(v_quantity2.get())
		kpb = float(v_quantity1.get())
		calc = quan * kpb # 39 บาทต่อกิโล * จำนวนปลาที่กรอกมา
		#quan = float(E1.get())
		#kpb = float(E2.get())
		#print(type(quan))
		#print(type(kpb))
		calc = quan * kpb
		print(calc)
		messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc))
		v_quantity1.set(' ')
		v_quantity2.set(' ')
	except:
		messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quantity1.set('')
		v_quantity2.set('')
B = ttk.Button(GUI, text='คำนวณ',command=cal)
B.pack(ipadx=30, ipady=20, pady=20) # ipadx ขยายความกว้าง x/y ภายใน




GUI.mainloop()  # เพื่อให้โปรแกรมรันตลอดเวลา