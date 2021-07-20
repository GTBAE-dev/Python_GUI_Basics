from tkinter import*

root = Tk()
root.title("Listbox")
root.geometry("640x480+500+200")

# Listbox = 여러 줄에 걸쳐 임의의 목록을 관리하는 위젯
listbox = Listbox(root, selectmode= "extended", height = 0) # height = 한번에 보여줄 줄의 갯수(0은 모두)
# selectmode = browse(단일 선택, 방향키 이동시 선택) / single(단일 선택, 방향키 이동, 스페이스바 선택), multiple(다중 선택, 클릭, 방향키 이동 후 스페이스바 선택), extended(다중선택, shift+방향키, 드래그 선택)
# delete(start_index, end_index) = start 부터 end까지 삭제 / 
listbox.insert(0, "Apple") # insert(index, "문자열") = index에 문자열 입력
listbox.insert(1, "Strawberry")
listbox.insert(3, "Banana")
listbox.insert(END, "Watermelon")
listbox.insert(END, "Grape")
listbox.pack()


def btncmd():
    print(listbox.size(), "objects exist") # size() = listbox 내 객체 갯수 반환
    print(listbox.get(0, 2), "in row 1 to 3") # get(start_index, end_index) = start 부터 end까지 튜플형태로 반환
    listbox.delete(0) # delete(start_index, end_index) = start 부터 end까지 삭제(END 는 맨뒤 항목 삭제)
    print(listbox.get(0, 2), "in row 1 to 3")
    print(listbox.curselection()) # curselection() = 현재 선택된 객체 index 반환

btn = Button(root, text = "Click", command = btncmd)
btn.pack()

root.mainloop()