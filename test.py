import serial
import time

ser = serial.Serial('COM11', 9600, parity=serial.PARITY_EVEN, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE)

if ser.is_open:
    print('串口已经打开')

# data_to_send = [0x03, 0x03, 0x02, 0x76, 0x00, 0x01, 0x65, 0x8A]
# data_to_send2 = [0x03, 0x03, 0x02, 0xE0, 0x00, 0x01, 0x85, 0xA6]
# data_to_send = [0x01, 0x03, 0x00, 0x01, 0x00, 0x03, 0x55, 0xE9]

data_to_send = [0x68, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x68, 0x04, 0x08, 0x37, 0x33, 0x34, 0x34, 0x00, 0x02, 0xAA, 0xE9, 0x46, 0x16]

data_to_send_clr = [0x68, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x68, 0x04, 0x04, 0x33, 0xF3, 0xF3, 0x3B, 0x2F, 0x16]

# ser.write(bytes(data_to_send_clr))

time.sleep(1)
ser.write(bytes(data_to_send))

t = time.time()

print(t)

for _ in range(24):

    print(hex(int.from_bytes(ser.read(),byteorder='big')))
