import time
from tkinter import*
import tkinter.ttk as ttk # Progressbar 사용 위한 tkinter.ttk 라이브러리

root = Tk()
root.title("Progressbar")
root.geometry("640x480+500+200")

# Progressbar = 진행 상태 표시 위젯(다운로드 상태 등)
progressbar_1 = ttk.Progressbar(root, maximum = 100, mode = "determinate") # maximum(프로그레스바 최대값) / mode(determinate = 처음부터 끝까지 채워짐, indeterminate = 처음과 끝 반복이동)
progressbar_1.start(20) # 프로그레스바 시작(속도, 작을수록 빠름)
progressbar_1.pack()

def btncmd_1():
    progressbar_1.stop() # 프로그레스바 정지

btn_1 = Button(root, text = "Stop", command = btncmd_1)
btn_1.pack()

p_var2 = DoubleVar() # 프레그레스바의 현재 상태 반환(실수값)
progressbar_2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2) # variable = 프로그레스바의 현재 값을 가져올 변수
progressbar_2.pack()

def btncmd_2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기
        p_var2.set(i)
        progressbar_2.update()
        print(p_var2.get())

btn_2 = Button(root, text = "Go", command = btncmd_2)
btn_2.pack()

root.mainloop()