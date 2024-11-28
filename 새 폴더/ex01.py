import serial
import time
import tkinter as tk
from tkinter import messagebox

# 아두이노 포트를 설정하세요
arduino_port = 'COM10'  # 실제 포트로 변경
baud_rate = 9600

# 직렬 포트 연결
try:
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # 초기화 시간 대기
except Exception as e:
    messagebox.showerror("Error", f"아두이노 연결 오류: {e}")
    exit()

# LED 제어 함수
def control_led(command):
    try:
        arduino.write(command.encode())  # 아두이노로 데이터 전송
    except Exception as e:
        messagebox.showerror("Error", f"데이터 전송 오류: {e}")

# GUI 설정
root = tk.Tk()
root.title("LED Controller")
root.geometry("500x400")  # 창 크기 조정

# 버튼 정의 (8개 버튼, LED ON/OFF)
buttons = [
    {"text": "LED1 ON", "command": "1", "bg": "green"},
    {"text": "LED1 OFF", "command": "2", "bg": "red"},
    {"text": "LED2 ON", "command": "3", "bg": "green"},
    {"text": "LED2 OFF", "command": "4", "bg": "red"},
    {"text": "LED3 ON", "command": "5", "bg": "green"},
    {"text": "LED3 OFF", "command": "6", "bg": "red"},
    {"text": "LED4 ON", "command": "7", "bg": "green"},
    {"text": "LED4 OFF", "command": "8", "bg": "red"},
    {"text": "LED5 ON", "command": "9", "bg": "green"},
    {"text": "LED5 OFF", "command": "A", "bg": "red"},
    {"text": "LED6 ON", "command": "B", "bg": "green"},
    {"text": "LED6 OFF", "command": "C", "bg": "red"},
    {"text": "LED7 ON", "command": "D", "bg": "green"},
    {"text": "LED7 OFF", "command": "E", "bg": "red"},
    {"text": "LED8 ON", "command": "F", "bg": "green"},
    {"text": "LED8 OFF", "command": "G", "bg": "red"}
]

# 버튼 생성 (8개의 LED 버튼)
for i, btn in enumerate(buttons):
    button = tk.Button(
        root,
        text=btn["text"],
        bg=btn["bg"],
        fg="white",
        font=("Arial", 12),
        command=lambda cmd=btn["command"]: control_led(cmd)
    )
    button.grid(row=i // 4, column=i % 4, padx=10, pady=10, ipadx=20, ipady=10)

# 종료 버튼
exit_button = tk.Button(
    root,
    text="종료",
    bg="gray",
    fg="white",
    font=("Arial", 12),
    command=lambda: (arduino.close(), root.destroy())
)
exit_button.grid(row=5, column=0, columnspan=4, pady=10)  # 종료 버튼 위치 조정

# GUI 실행
root.mainloop()
