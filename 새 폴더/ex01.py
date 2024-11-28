import serial
import time
import tkinter as tk
from tkinter import messagebox

# 아두이노 포트를 설정하세요
arduino_port = 'COM16'  # 실제 포트로 변경
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
root.geometry("400x300")

# 버튼 정의
buttons = [
    {"text": "LED1 ON", "command": "1", "bg": "green"},
    {"text": "LED1 OFF", "command": "2", "bg": "red"},
    {"text": "LED2 ON", "command": "3", "bg": "green"},
    {"text": "LED2 OFF", "command": "4", "bg": "red"},
    {"text": "LED3 ON", "command": "5", "bg": "green"},
    {"text": "LED3 OFF", "command": "6", "bg": "red"},
    {"text": "LED4 ON", "command": "7", "bg": "green"},
    {"text": "LED4 OFF", "command": "8", "bg": "red"}
]

# 버튼 생성
for i, btn in enumerate(buttons):
    button = tk.Button(
        root,
        text=btn["text"],
        bg=btn["bg"],
        fg="white",
        font=("Arial", 12),
        command=lambda cmd=btn["command"]: control_led(cmd)
    )
    button.grid(row=i // 2, column=i % 2, padx=10, pady=10, ipadx=20, ipady=10)

# 종료 버튼
exit_button = tk.Button(
    root,
    text="종료",
    bg="gray",
    fg="white",
    font=("Arial", 12),
    command=lambda: (arduino.close(), root.destroy())
)
exit_button.grid(row=4, column=0, columnspan=2, pady=10)

# GUI 실행
root.mainloop()
