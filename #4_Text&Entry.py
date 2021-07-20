from tkinter import*

root = Tk()
root.title("Text & Entry")
root.geometry("640x480+500+200")

# Text = 여러 줄 텍스트 입력 가능 위젯
txt = Text(root)
txt.pack(expand = True, fill = BOTH, padx = 5, pady = 5)
txt.insert(END, "INSERT TEXT") # insert(index, "문자열") = index 위치에 문자열 삽입
# delete(start_index, end_index) = 문자열 삭제 / get(start_index, end_index) = 문자열 반환

# Entry = 한 줄 텍스트 입력 가능 위젯(엔터 불가/ ID & PW 입력 시)
e = Entry(root)
e.pack(fill = "x", padx = 5, pady = 5)
e.insert(0, "INSERT ENTRY")

def btncmd():
    print(txt.get("1.0", END)) # 1.0 = 1번째 줄(row), 0 번째 Column 좌표
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, 1) # Entry 좌표 설정 방법(Column)

btn = Button(root, text = "Click", command = btncmd)
btn.pack(fill = "x", padx = 5, pady = 5)

root.mainloop()