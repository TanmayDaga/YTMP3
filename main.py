import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class Browser(QMainWindow):
    def __init__(self):
        super(Browser, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.youtube.com/'))
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")

        back_btn.triggered.connect(self.browser.back)

        navtb.addAction(back_btn)

        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")

        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")

        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navtb.addWidget(self.urlbar)

        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")

        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # download video
        videoDownload = QAction("Download Video", self)
        videoDownload.setStatusTip("Downloads Video")

        videoDownload.triggered.connect(self.download_video)
        navtb.addAction(videoDownload)

        # Download song
        audioDownload = QAction("Download Audio", self)
        audioDownload.setStatusTip("Downloads audio")

        audioDownload.triggered.connect(self.audio_download)
        navtb.addAction(audioDownload)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(title + "- Tanmay's Browser")

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())

        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def update_urlbar(self, q):

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def download_video(self):
        vid_url = self.urlbar.text()
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_():
            foldername = dialog.selectedFiles()[0]
            print(foldername)
            os.system(f'python3.8 ytd.py {vid_url} {foldername}')

    def audio_download(self):
        aud_url = self.urlbar.text()
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_():
            foldername = dialog.selectedFiles()[0]
            print(foldername)
            os.system(f'python3.8 ytmp3.py {aud_url} {foldername}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Tanmay's Browser")

    window = Browser()
    window.show()
    app.exec_()
