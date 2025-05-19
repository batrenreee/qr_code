import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout, QFrame
)
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt
from youtubesearchpython import VideosSearch
import qrcode

class QRUygulama(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎵 Şarkı QR Oluşturucu")
        self.setGeometry(100, 100, 500, 600)
        self.setStyleSheet("background-color: #f0f2f5; font-family: 'Segoe UI';")
        self.arayuz_olustur()

    def arayuz_olustur(self):
        self.layout = QVBoxLayout()

        self.title = QLabel("🎶 Şarkı QR Kodu Oluştur")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        self.title.setStyleSheet("color: #333; margin: 20px;")

        self.entry = QLineEdit()
        self.entry.setPlaceholderText("Şarkı adını gir (örnek: Tarkan - Kuzu Kuzu)")
        self.entry.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border: 2px solid #ccc;
            border-radius: 10px;
            margin-bottom: 15px;
        """)

        self.button = QPushButton("🔍 QR Oluştur")
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.button.clicked.connect(self.qr_olustur)

        self.qr_frame = QFrame()
        self.qr_frame.setFrameShape(QFrame.StyledPanel)
        self.qr_frame.setStyleSheet("background-color: white; border-radius: 15px; padding: 15px;")
        self.qr_label = QLabel()
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.qr_frame_layout = QVBoxLayout()
        self.qr_frame_layout.addWidget(self.qr_label)
        self.qr_frame.setLayout(self.qr_frame_layout)

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.qr_frame)
        self.setLayout(self.layout)

    def qr_olustur(self):
        sarki_adi = self.entry.text().strip()
        if not sarki_adi:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir şarkı adı gir.")
            return

        try:
            video_search = VideosSearch(sarki_adi, limit=1)
            sonuc = video_search.result()
            if not sonuc['result']:
                QMessageBox.critical(self, "Hata", "Şarkı bulunamadı.")
                return

            video = sonuc['result'][0]
            link = video['link']
            title = video['title'].lower()

            keywords = ["music", "official", "song", "lyrics", "audio", "remix", "feat", "ft."]
            if not any(k in title for k in keywords):
                QMessageBox.information(self, "Bilgi", "Bu video bir şarkı olmayabilir.")
                return

            qr = qrcode.make(link)
            qr.save("sarki_qr.png")

            pixmap = QPixmap("sarki_qr.png").scaled(250, 250, Qt.KeepAspectRatio)
            self.qr_label.setPixmap(pixmap)

            QMessageBox.information(self, "Başarılı", "QR kod oluşturuldu!")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Hata oluştu:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = QRUygulama()
    pencere.show()
    sys.exit(app.exec_())
