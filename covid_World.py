import socket
import time
def Led_A_ON():
     #Show to LabelA----------------
 try:          # 例外處理
  ip = '192.168.11.17'     # 連線IP     
  port =9000            # 連線通訊埠
  Senddata ="/LED=ON"     # 取得傳送資料
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket物件
  client.connect((ip,port))      # 連線服務端
  client.send(str(Senddata).encode())       # 傳送資料
  client.close()        # 關閉連線
 except:
  print("no")
def Led_A_OFF():
     #Show to LabelA----------------
 try:          # 例外處理
  ip = '192.168.1.17'     # 連線IP     
  port =80          # 連線通訊埠
  Senddata ="/LED=OFF"     # 取得傳送資料
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket物件
  client.connect((ip,port))      # 連線服務端
  client.send(str(Senddata).encode())       # 傳送資料
  client.close()        # 關閉連線
 except:
  print("no")
Led_A_ON()
time.sleep(3)
Led_A_OFF