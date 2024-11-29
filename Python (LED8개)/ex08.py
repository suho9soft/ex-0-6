import serial
import threading
import tkinter as tk
from tkinter import messagebox

# 초기 시리얼 포트 설정
arduino = None
serial_thread = None  # 스레드를 추적할 변수
led_states = ['0'] * 8  # 8개의 LED 상태를 저장

def open_serial():
    global arduino, serial_thread
    try:
        arduino = serial.Serial('COM17', 9600)
        text_box.insert(tk.END, "Serial port opened.\n")
        text_box.see(tk.END)
        # 시리얼 읽기 스레드 시작
        serial_thread = threading.Thread(target=read_from_arduino)
        serial_thread.daemon = True
        serial_thread.start()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open serial port: {e}")

def close_serial():
    global arduino
    if arduino and arduino.is_open:
        arduino.close()
        text_box.insert(tk.END, "Serial port closed.\n")
        text_box.see(tk.END)
    else:
        messagebox.showinfo("Info", "Serial port is already closed.")

def read_from_arduino():
    global arduino
    try:
        while arduino and arduino.is_open:
            if arduino.in_waiting > 0:
                data = arduino.readline().decode('utf-8').strip()
                text_box.insert(tk.END, data + '\n')
                text_box.see(tk.END)
    except serial.SerialException:
        text_box.insert(tk.END, "Serial connection lost.\n")
        text_box.see(tk.END)

def update_led(index, state):
    global arduino, led_states
    if arduino and arduino.is_open:
        led_states[index] = '1' if state else '0'  # 상태 업데이트
        arduino.write(''.join(led_states).encode())  # LED 상태 전체를 전송
        text_box.insert(tk.END, f"LED {index + 1} {'ON' if state else 'OFF'}\n")
        text_box.see(tk.END)
    else:
        messagebox.showinfo("Info", "Serial port is not open.")

# GUI 설정
root = tk.Tk()
root.title("Arduino Serial Communication")
root.configure(bg='#2E2E2E')  # 배경 색상 설정

# 아두이노가 보낸 데이터를 출력하는 부분
text_box = tk.Text(root, height=10, width=50, bg='#1E1E1E', fg='#00FF00', insertbackground='white')
text_box.pack()

# 아두이노와 연결하는 부분
open_button = tk.Button(root, text="Open Serial Port", command=open_serial, bg='#4CAF50', fg='#FFFFFF', font=('Arial', 12, 'bold'))
open_button.pack(pady=5)

# 아두이노와 연결을 끊는 부분
close_button = tk.Button(root, text="Close Serial Port", command=close_serial, bg='#F44336', fg='#FFFFFF', font=('Arial', 12, 'bold'))
close_button.pack(pady=5)

# LED 제어 버튼 생성
led_buttons = []
for i in range(8):  # 8개의 버튼 생성
    frame = tk.Frame(root, bg='#2E2E2E')
    frame.pack(pady=2)
    label = tk.Label(frame, text=f"LED {i + 1}", bg='#2E2E2E', fg='#FFFFFF', font=('Arial', 10))
    label.pack(side=tk.LEFT, padx=5)
    btn_on = tk.Button(frame, text="ON", command=lambda i=i: update_led(i, True), bg='#4CAF50', fg='#FFFFFF', font=('Arial', 10, 'bold'))
    btn_on.pack(side=tk.LEFT, padx=5)
    btn_off = tk.Button(frame, text="OFF", command=lambda i=i: update_led(i, False), bg='#F44336', fg='#FFFFFF', font=('Arial', 10, 'bold'))
    btn_off.pack(side=tk.LEFT, padx=5)

# 파이썬에서 GUI가 유지되기 위해 실행되는 메인스레드
root.mainloop()
