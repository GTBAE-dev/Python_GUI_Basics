from tkinter import*

root = Tk()
root.title("Menubar")
root.geometry("640x480+500+200")

# Menu = 메뉴바 위젯
def create_new_file():
    print("New file created")

menu = Menu(root)
menu_file = Menu(menu, tearoff = 0) # tearoff = 메뉴창 분리 기능
menu_file.add_command(label = "New file", command = create_new_file) # 메뉴 창 내 항목 추가
menu_file.add_command(label = "New Window")
menu_file.add_separator() # 메뉴 창 내 구분좌 삽입
menu_file.add_command(label = "Open file...")
menu_file.add_separator()
menu_file.add_command(label = "Save all", state = "disable") # state(disable) = 비활성화 처리
menu_file.add_command(label = "Exit", command = root.quit) # root.quit = 종료 처리
menu.add_cascade(label = "File", menu = menu_file) # 메뉴 줄 내 항목 메뉴 삽입

menu.add_cascade(label = "Edit")

menu_lang = Menu(menu, tearoff = 0) # Radiobutton 형태의 메뉴
menu_lang.add_radiobutton(label = "Python")
menu_lang.add_radiobutton(label = "C++")
menu_lang.add_radiobutton(label = "Java")
menu.add_cascade(label = "Language", menu = menu_lang)

menu_view = Menu(menu, tearoff = 0) # Checkbox 형태의 메뉴
menu_view.add_checkbutton(label = "Show/Hide")
menu.add_cascade(label = "View", menu = menu_view)

root.config(menu = menu) # config(menu) = 설정한 메뉴 그리기
root.mainloop()