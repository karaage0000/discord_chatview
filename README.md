# discord KikisenView

discordの聞き専チャットなどを出力するためのツールです。  
常に前面表示（Always on Top）に対応しており、配信や作業補助に使用できます。

---

## 機能説明
- 常に前面表示（Always on Top）
- URL入力でWebページ表示
- 軽量なシンプルUI
---
## 動作環境
- Python 3.8 以上
- Windows / macOS / Linux
---

## 必要なライブラリ
以下をインストールしてください：

```bash
pip install PyQt5 PyQtWebEngine
```

pipがインストールされていない場合(Windows)
```
1. [公式Pythonサイト](https://www.python.org/downloads/) から最新のPythonをダウンロード
2. インストーラー実行時に「**Add Python to PATH**」にチェックを入れる
3. 「Install Now」をクリックしてインストール
```

## 使い方

1.main.pyを任意のフォルダに配置  
2.main.pyを右クリック -> Pythonで開くを選択  
3.https://streamkit.discord.com/overlay  の「chat widget」に移動    
4.見たいチャットを選んでURLを取得  
5.ツールのURL入力欄に4.のURLを入れて実行ボタンをクリック
