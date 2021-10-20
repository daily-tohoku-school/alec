# 概要
- 20211022（金）13:05 〜
- anyenv
- nodenv
- Node.js
- pyenv
- Python
<p></p>

# コマンドで OS のバージョンを確認
`$ uname -a`
<p></p>

`Linux raspberrypi 4.19.97-v7l+ #1294 SMP Mon Jan 30 13:21:14 GMT 2020 armv7l GNU/Linux`
<p></p>

# anyenv
## 参考サイト
- [anyenv まとめ](https://qiita.com/SUZUKI_Masaya/items/51366be1510f7fde7cdf)
<p></p>

## anyenv インストール
```
$ git clone https://github.com/riywo/anyenv ~/.anyenv
```
<p></p>

## パスを通す
ホームディレクトリの `.profile` を開いて最終行に以下を追加

```
if [ -d $HOME/.anyenv ]
then
    export PATH="$HOME/.anyenv/bin:$PATH"
    eval "$(anyenv init -)"
fi
```

```
$ source ~/.profile
$ anyenv install --init
$ anyenv
```
<p></p>

## プラグイン用ディレクトリを作成
```
$ mkdir -p $(anyenv root)/plugins
```
<p></p>

## anyenv-update インストール
```
$ git clone https://github.com/znz/anyenv-update.git $(anyenv root)/plugins/anyenv-update
$ anyenv update
```
<p></p>

# nodenv
## nodenv インストール
```
$ anyenv install -l
$ anyenv install nodenv
$ source ~/.profile
$ anyenv version
```
<p></p>

# Node.js
## 16.10.0 インストール
```
$ nodenv install -l
$ nodenv install 16.10.0
$ nodenv rehash
$ nodenv versions
$ nodenv global 16.10.0
$ node -v
$ npm version
```
<p></p>
<div class="page-break"></div>

# pyenv
## 必要パッケージのインストール
```
$ sudo apt install -y git openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev
```
<p></p>

## pyenv インストール
```
$ anyenv install -l
$ anyenv install pyenv
$ source ~/.profile
$ anyenv version
```
<p></p>

# Python
## 3.10.0 インストール
```
$ pyenv install -l
$ pyenv install 3.10.0
$ pyenv rehash
$ pyenv versions
$ pyenv global 3.10.0
$ python -V
```
<p></p>
