from tkinter import*

root = Tk()
root.title("Scrollbar")
root.geometry("640x480+500+200")

# Scrollbar = 상하 이동 위젯(스크롤바 + 스크로로 대상 같이 생성)
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side = "right", fill = "y")


listbox = Listbox(frame, selectmode = "extended", height = 10, yscrollcommand = scrollbar.set) # yscrollcommand = 해당위젯(리스트박스)과 스크롤바 연동
for i in range(1, 366):
    listbox.insert(END, str(i) + "일")
listbox.pack(side = "left")

scrollbar.config(command = listbox.yview) # scrollbar.config = 스크롤바와 위젯 연동

# Frame 안에 리스트박스 와 스크롤바가 따로 위젯으로 들어있고 해당 두 위젯을 yscrollcommand 와 config로 연동시켜놓은 상태

root.mainloop()