# 概要
このアプリケーションは鳥類を鳴き声から主に中南米やオーストラリアなどの熱帯地域に生息する種類の鳥を推定します．
推定結果からWeb検索を行いその鳥の画像をダウンロードします．
Transformerモデルを利用しており，GUIで音声ファイルの決定と画像の表示を行えます．

# 目的
- 音源分類の最新モデルの性能を試す．
- 推定結果から正しい鳥の画像をダウンロードできるようにする．

# アプリケーションの導入
1. リポジトリのクローン

```
git clone https://github.com/ChikaraHanakawa/SoundsClassificatin_BirdImage.git
```

2. 仮想環境の作成および実行
- venvで仮想環境を作る場合
```
python3 -m venv hoge
```
```
source hoge/bin/activate
```

- anacondaで仮想環境を作る場合

```
conda create -n hoge
```
```
conda activate hoge
```

3. 必要パッケージのインストール

```
pip install -r requirements.txt
```

```
sudo apt-get install python3-tk
```

# 使用方法
```
python3 script/main.py
```
- 表示されたウィンドウから音声ファイルを選択し，`Run app`をクリックすることでプログラムを実行
- 推定終了後に検索した画像がダウンロードされつつ表示される

# 使用モデル
音源分類：dima806のbird_sounds_classificationモデル

# 鳴き声の取得方法
こちらのサイトを利用しました．
https://xeno-canto.org

# ライセンス
このアプリケーションはdim806の研究成果を利用しています．

Apache License 2.0

    Copyright [yyyy] [name of copyright owner]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License. 
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software 
    distributed under the License is distributed on an "AS IS" BASIS, 
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
    See the License for the specific language governing permissions and limitations under the License.