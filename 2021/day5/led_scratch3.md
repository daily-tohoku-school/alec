# 概要
- 20211027（水）13:05 〜
- カメラモジュール
- ML2Scratch
<p></p>

# Raspberry Pi OS 旧バージョンをインストール
- 現行の OS ( Release date: May 7th 2021 )にインストールされている Chromium が、カメラモジュールを認識しないため
<p></p>

## 参考サイト
- [旧バージョンのRaspbianのイメージファイルのダウンロード先](https://raspida.com/old-raspbian-download)
<p></p>

## ダウンロード
- [http://ftp.jaist.ac.jp/pub/raspberrypi/NOOBS/images/NOOBS-2020-02-14/](http://ftp.jaist.ac.jp/pub/raspberrypi/NOOBS/images/NOOBS-2020-02-14/)
- NOOBS_v3_3_1.zip をダウンロード
- zip を展開
<p></p>

## インストール
- 展開した中身のフォルダとファイルをフォーマットした microSD カードにコピー
- microSD カードを Raspberry Pi 本体にセットし、電源を入れてインストール開始
<p></p>

## コマンドで確認
`$ uname -a`
<p></p>

`Linux raspberrypi 4.19.97-v7l+ #1294 SMP Mon Jan 30 13:21:14 GMT 2020 armv7l GNU/Linux`<div class="page-break"></div>
<p></p>
<div class="page-break"></div>

# カメラ設定と確認
## 設定
Raspberry Pi アイコン -> 設定 -> Raspberry Pi の設定 -> インターフェイス -> カメラ -> 有効 -> 再起動
<p></p>

## 確認
`$ vcgencmd get_camera`
<p></p>

`supported=1 detected=1` と表示されれば OK
<p></p>

## 試しに静止画を撮影する
`$ sudo raspistill -o image.jpg`
<p></p>

- 撮影した画像はホームディレクトリに保存される。
<p></p>
<div style="page-break-before:always"></div>

# ML2Scratch で機械学習
## 参考サイト
- [How to use(使い方)](https://github.com/champierre/ml2scratch#how-to-use%E4%BD%BF%E3%81%84%E6%96%B9)
<p></p>

## 手順
### 準備
- [https://stretch3.github.io/](https://stretch3.github.io/) を Chromium で開く
<center><img src="./img/strech01.png" width="500px"></center>
<p></p>

- 左下の拡張ボタンをクリック > ML2SCRATCH
<center><img src="./img/strech02.png" width="500px"></center>
<p></p>

- カメラの使用の許可
<p></p>

- `ラベル`、`ラベル1の枚数`、`ラベル2の枚数`、`ラベル3の枚数`をチェックオン
- コードエリアに`ラベル X を学習する`ブロックを配置する
- `ラベル X を学習する`ブロックの上に`スペースキーが押された時`ブロックを連結する
<center><img src="./img/strech03.png" width="500px"></center>
<p></p>
<div style="page-break-before:always"></div>

### 学習
- `グー`をカメラに映し、`ラベル 1 を学習する`ブロックを 20 枚の画像データを作成するまでクリック
- `チョキ`をカメラに映し、`ラベル 2 を学習する`ブロックを 20 枚の画像データを作成するまでクリック
- `パー`をカメラに映し、`ラベル 3 を学習する`ブロックを 20 枚の画像データを作成するまでクリック
<p></p>

### 予測
- 学習データ（モデル）を使って予測した結果がステージの`ラベル`に表示されます。
<center><img src="./img/strech04.png" width="500px"></center>
<p></p>

## モデルの保存
- `学習データをダウンロード`ブロックを使ってローカルに保存しておくこともできる。
<p></p>
<div style="page-break-before:always"></div>
