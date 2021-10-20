# 概要
- 20211027（水）13:05 〜
- Tello を Python で制御
<p></p>

# 参考サイト
- [Tello SDK 1.3.0.0](https://terra-1-g.djicdn.com/2d4dce68897a46b19fc717f3576b7c6a/Tello%20%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/For%20Tello/Tello%20SDK%20Documentation%20EN_1.3_1122.pdf)
- [Tello SDKを利用してPythonでTello(ドローン)を飛ばそう！SDK1.3日本語説明付き！](https://se-lina.hatenablog.com/entry/2020/08/16/110723)
<p></p>

# Tello 制御のための設定
## ディレクトリ作成
```
$ mkdir Tello && cd &_
$ mkdir python_tello && cd $_
$ pyenv local 3.10.0
```
<p></p>
<div class="page-break"></div>

## Tello 制御プログラム
`index.py` を作成し以下を記述
<p></p>

```
import socket
import time

#Create a UDP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1' , 8889)

#command-mode : 'command'
socket.sendto('command'.encode('utf-8'),tello_address)
print ('start')

socket.sendto('takeoff'.encode('utf-8'),tello_address)
print ('takeoff')

time.sleep(5)
socket.sendto('land'.encode('utf-8'),tello_address)
print ('land')
```
<p></p>

## 実行
Tello を起動し、RaspberryPi と繋げる

```
python index.py
```
<p></p>
<div class="page-break"></div>
