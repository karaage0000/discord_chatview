import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QColor

class TransparentResizableWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 常に前面 + 透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)

        # メインコンテナ（半透明）
        self.container = QWidget()
        self.container.setStyleSheet("""
            background-color: rgba(255, 255, 255, 180);
            border-radius: 12px;
        """)
        self.setCentralWidget(self.container)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        self.container.setLayout(main_layout)

        # --- URLバー ---
        top_bar = QHBoxLayout()
        top_bar.setSpacing(8)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("URLを入力")
        self.url_input.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255,255,255,220);
                border: none;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
            }
        """)

        self.load_button = QPushButton("▶")
        self.load_button.setFixedWidth(40)
        self.load_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.load_button.clicked.connect(self.load_url)
        self.url_input.returnPressed.connect(self.load_url)

        top_bar.addWidget(self.url_input)
        top_bar.addWidget(self.load_button)

        main_layout.addLayout(top_bar)

        # --- Web表示 ---
        self.view = QWebEngineView()
        self.view.setAttribute(Qt.WA_TranslucentBackground, True)
        self.view.page().setBackgroundColor(QColor(0, 0, 0, 0))

        main_layout.addWidget(self.view)

        # ★ ここは resize（可変サイズ）
        self.resize(800, 600)

    def load_url(self):
        url_text = self.url_input.text().strip()
        if url_text:
            if not url_text.startswith(("http://", "https://")):
                url_text = "http://" + url_text

            self.view.load(QUrl(url_text))

            # 少し薄くする
            self.url_input.setStyleSheet("""
                QLineEdit {
                    background-color: rgba(255,255,255,120);
                    border-radius: 8px;
                    padding: 6px;
                }
            """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransparentResizableWindow()
    window.show()
    sys.exit(app.exec_())
