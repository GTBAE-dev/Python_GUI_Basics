from tkinter import*
import tkinter.ttk as ttk # Combobox 사용 위한 tkinter.ttk 라이브러리

root = Tk()
root.title("Combobox")
root.geometry("640x480+500+200")

Label(root, text = "When's Your Birthday?").pack()
# Combobox = 리스트 중 하나 선택 가능, 값 입력 가능한 위젯
months = [str(i) + "월" for i in range(1, 13)]
month_combobox = ttk.Combobox(root, height = 5, values = months) # height(보여지는 갯수) / values(보여질 값)
month_combobox.set("Month") # set(최초 보여질 제목 설정)
month_combobox.pack()

day = [str(i) + "일" for i in range(1, 32)]
day_combobox = ttk.Combobox(root, height = 10, values = day, state = "readonly") # state = readonly (선택만 가능하게 설정, 없으면 값 입력 가능)
day_combobox.current(0) # current(0) = 최초 0번째 index 선택
day_combobox.pack()

def btncmd():
    print(month_combobox.get())
    print(day_combobox.get())

btn = Button(root, text = "My birthday is..", command = btncmd)
btn.pack()

root.mainloop()