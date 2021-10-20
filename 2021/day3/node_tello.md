# 概要
- 20211027（水）13:05 〜
- Tello を Node.js で制御
<p></p>

# 参考サイト
- [Tello SDK 1.3.0.0](https://terra-1-g.djicdn.com/2d4dce68897a46b19fc717f3576b7c6a/Tello%20%E7%BC%96%E7%A8%8B%E7%9B%B8%E5%85%B3/For%20Tello/Tello%20SDK%20Documentation%20EN_1.3_1122.pdf)
- [Google Homeに話しかけてドローンを音声操作してみる](https://qiita.com/miso_develop/items/a482dc4d168ec0a33818)
<p></p>

# Tello 制御のための設定
## ディレクトリ作成
```
$ mkdir Tello && cd &_
$ mkdir node_tello && cd $_
$ nodenv local 16.10.0
```
<p></p>

## UDP パッケージ・インストール
```
$ npm install dgram
```
<p></p>
<div class="page-break"></div>

## Tello 制御プログラム
`index.js` を作成し以下を記述
<p></p>

```
"use strict"

const dgram = require("dgram")
const sock = dgram.createSocket("udp4")

// Telloの固定情報
const tello = {
    ip: "192.168.10.1",
    port: 8889
}

// Telloにコマンド送信する関数
const send = async (buf, ms = 0) => {
    console.log(buf)
    const command = new Buffer(buf)
    sock.send(command, 0, command.length, tello.port, tello.ip)
    await wait(ms)
}
const wait = ms => new Promise(res => setTimeout(res, ms))

// Telloに操作したいコマンドを記述
const main = async () => {
    await send("command", 100)
    await send("takeoff", 4000)
    await send("land")
    process.exit()
}
main()
```
<p></p>

## 実行
Tello を起動し、RaspberryPi と繋げる

```
node index.js
```
<p></p>
<div class="page-break"></div>
