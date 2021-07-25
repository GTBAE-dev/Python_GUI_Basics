from tkinter import*
import tkinter.messagebox as msgbox

root = Tk()
root.title("Messagebox")
root.geometry("640x480+500+200")

# Messagebox = 알림, 경고, 에러 등 메시지를 보여주는 위젯
def info():
    msgbox.showinfo("Notice", "info message") # 정보 알람 (제목, 내용)

Button(root, command = info, text = "Notice").pack()

def warn():
    msgbox.showwarning("Warning", "Warning message") # 경고 알람

Button(root, command = warn, text = "Warning").pack()

def error():
    msgbox.showerror("Error", "Error Message") # 에러 알람

Button(root, command = error, text = "error").pack()

def okcancel():
    msgbox.askokcancel("ok/cancel", "Return true if answer is ok") # 확인/취소 가능 메시지 박스

Button(root, command = okcancel, text = "ok/cancel").pack()

def retrycancel():
    msgbox.askretrycancel("retry/cancel", "Return true if answer is retry") # 재시도/취소 가능 메시지 박스

Button(root, command = retrycancel, text = "retry/cancel").pack()

def yesno():
    msgbox.askyesno("yes/no", "Return true if answer is yes") # 예/아니오 가능 메시지 박스

Button(root, command = yesno, text = "yes/no").pack()

def yesnocancel():
    response = msgbox.askyesnocancel("yes/no/cancel", "yes = true / no = False / cancel = None") # 예/아니오/취소 가능한 메시지 박스
    if response == 1:
        print("yes", response)
    elif response == 0:
        print("no", response)
    else:
        print("cancel", response)

Button(root, command = yesnocancel, text = "yes/no/cancel").pack()

root.mainloop()