from tkinter import*

root = Tk()
root.title("Advanced Frame")
root.geometry("640x480+500+200")

# 큰 프레임 안에 다른 작은 프레임 설정(명령어 입력 순서대로 그려짐)
Label(root, text = "Choose Your Meu").pack(side = "top")

Button(root, text = "Order").pack(side = "bottom")

frame_burger = Frame(root, relief = "solid", bd = 1) # relief = 테두리모양(flat, raised, sunken, solid, ridge, groove) / bd = 테두리 두께
frame_burger.pack(side = "left", fill = "both", expand = True)
Button(frame_burger, text = "Burger 1").pack()
Button(frame_burger, text = "Burger 2").pack()
Button(frame_burger, text = "Burger 3").pack()

frame_drink = LabelFrame(root, text = "Drink")
frame_drink.pack(side = "right", fill = "both", expand = True)
Button(frame_drink, text = "Coke").pack()
Button(frame_drink, text = "Sprite").pack()

root.mainloop()