from tkinter import*

root = Tk()
root.title("Button GUI")
root.geometry("640x480+500+200")

btn1 = Button(root, text = "버튼 1") # Button(넣을 위치(메인 프레임인 root), text = 버튼 title)
btn1.pack(side = "top") # side = 특정 위치로 공간 할당(top(기본값), bottom, left, right)

btn2 = Button(root, padx=5, pady=5, text = "버튼 2") # padx, pady = 버튼 내부 패드 생성(글자에 따른 유동적 버튼 크기)
btn2.pack(side = "top", fill = "x") # 위치 할당 시 순서대로 쌓이게 배치됨 / fill = 할당된 공간에 대한 크기 맞춤(none(기본값), x, y, both)

btn3 = Button(root, width = 5, height = 5, text = "버튼 3") # width, height = 버튼 크기 설정(글자가 크기 넘어도 크기 유지)
btn3.pack(side = "bottom", anchor = "e") # anchor = 할당된 공간 내에서 위치 지정(center(기본값), n, e, s, w, ne, nw, se, sw)

btn4 = Button(root, fg = "red", bg = "yellow", text = "버튼 4") # fg(foreground) = 버튼 폰트 색상 / bg(background) = 버튼 배경 색상
btn4.pack(side = "bottom") # 버튼 3이 제일 아래 bottom 위치 할당되어 그 위에 위치하게 됨

photo = PhotoImage(file = "star_image.png") # PhotoImage : 파일에 해당하는 것을 불러와 이미지로 저장(주소\파일명)
btn5 = Button(root, image = photo) # image = 이미지 삽입
btn5.pack(expand = True) # expand = 미사용 공간 확보(False(기본값), True)

def btncmd():
    print("Button Clicked")
btn6 = Button(root, text = "버튼 6", command = btncmd) # command = 버튼 동작 삽입
btn6.pack(expand = True, fill = "both") # expand 2개 버튼 적용시 미사용 공간 2분할

root.mainloop()