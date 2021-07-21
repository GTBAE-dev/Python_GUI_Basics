from tkinter import*

root = Tk()
root.title("Radiobutton")
root.geometry("640x480+500+200")

Label(root, text = "Choose Your Menu").pack()

# Radiobutton = 여러 객체 중 택 1 가능한 위젯(ex. 4지 선다)
burger_var = IntVar() # 라디오버튼으로 묶여있는 객체들의 value 저장(체크박스는 개별로 인식하여 각각으로 처리)
btn_burger1 = Radiobutton(root, text = "Hamburger", value = 1, variable = burger_var)
btn_burger1.select() # 기본적으로 첫 버튼 선택되게 처리
btn_burger2 = Radiobutton(root, text = "Cheese burger", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "Chicken burger", value = 3, variable = burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text = "Choose Your Drink").pack()
drink_var = StringVar() # String 형태로 라디오버튼 value 받환
btn_drink1 = Radiobutton(root, text = "Coke", value = "Coke", variable = drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text = "Sprite", value = "Sprite", variable = drink_var)
btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text = "Order", command = btncmd)
btn.pack()

root.mainloop()
