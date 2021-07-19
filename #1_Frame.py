# tkinter: 파이썬 내장 GUI 툴킷 라이브러리(Tcl(Tool command Language), Tk(크로스 플랫폼 Lightweight GUI 모듈) 지원)
from tkinter import*

root = Tk() # Tk 클래스 객체 생성

root.title("Basic GUI") # 제목 설정 함수
root.geometry("640x480+500+200") # 화면크기(가로x세로) & 초기 팝업 좌표(+ x좌표 + y좌표)함수, 띄우쓰기 X
root.resizable(False, False) # 창 크기 변경 가능 유무 조절 함수(가로, 세로)

root.mainloop() # 메인루프 메소드: 이벤트를 처리하면 창 종료시까지 반복