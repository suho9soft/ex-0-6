import serial
import threading
import tkinter as tk
from tkinter import messagebox

# 초기 시리얼 포트 설정
arduino = None
serial_thread = None  # 스레드를 추적할 변수

def open_serial():
    global arduino, serial_thread
    try:
        arduino = serial.Serial('COM16', 9600)
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
        # arduino라는 변수가 생성이 되고 아두이노와 확실히 연결이 되었다면~
        while arduino and arduino.is_open:
            if arduino.in_waiting > 0:
                data = arduino.readline().decode('utf-8').strip()
                text_box.insert(tk.END, data + '\n')
                text_box.see(tk.END)
    except serial.SerialException:
        text_box.insert(tk.END, "Serial connection lost.\n")
        text_box.see(tk.END)

def led_on():
    global arduino
    if arduino and arduino.is_open:
        arduino.write(b'1')
    else:
        messagebox.showinfo("Info", "Serial port is not open.")

def led_off():
    global arduino
    if arduino and arduino.is_open:
        arduino.write(b'0')
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

# 아두이노에게 데이터를 전송하는 부분
btn_on = tk.Button(root, text="LED ON", command=led_on, bg='#4CAF50', fg='#FFFFFF', font=('Arial', 12, 'bold'))
btn_on.pack(pady=5)

btn_off = tk.Button(root, text="LED OFF", command=led_off, bg='#F44336', fg='#FFFFFF', font=('Arial', 12, 'bold'))
btn_off.pack(pady=5)

# 파이썬에서 GUI가 유지되기 위해 실행되는 메인스레드
root.mainloop()
