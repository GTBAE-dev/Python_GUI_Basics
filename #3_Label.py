from tkinter import*

root = Tk()
root.title("Label")
root.geometry("640x480+500+200")

# label = 글자 혹은 이미지를 보여주는 위젯, 동작 X

label1 = Label(root, bg = "red", text = "Hello")
label1.pack()

photo1 = PhotoImage(file = "star_image.png")
label2 = Label(root, image = photo1)
label2.pack()

def change():
    label1.config(text = "See You") # cofig = configure = 객체 초기 설정값 변경 함수

    global photo2 # 전역변수로 지정: 함수가 끝나도 존재하도록
    photo2 = PhotoImage(file = "star_image_filled.png")
    label2.configure(image = photo2) # 전역변수로 지정 안해주면 이미지 사라지는 이유: garbage collection(불필요한 메모리 공간 해제)

btn = Button(root, text = "클릭", command = change)
btn.pack()

root.mainloop()