from tkinter import*

root = Tk()
root.title("Checkbox")
root.geometry("640x480+500+200")

# Checkbox = 체크 / 체크해제 가능한 위젯
chkvar1 = IntVar() # 체크 유무 int값 반환받을 변수
checkbox1 = Checkbutton(root, text = "Close for today", variable = chkvar1, activebackground = "green") # variable = 체크 유무에 따른 값 반환할 변수 설정, activebackground = 클릭시 배경 색상 변경
checkbox1.select() # 초기 자동 선택 처리
checkbox1.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(root, text = "Close for this week", variable = chkvar2, activeforeground = "green") # activeforeground = 클릭시 글자 색상 변경
checkbox2.deselect() # 초기 자동 해제 처리(기본값 = 해제 상태)
checkbox2.pack()

def btncmd():
    print(chkvar1.get()) # 0: 체크 해제, 1: 체크
    print(chkvar2.get())

btn = Button(root, text = "Click", command = btncmd)
btn.pack()

root.mainloop()