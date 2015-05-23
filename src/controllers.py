# -*- coding:utf8 -*-
__author__ = 'cosven'

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

from api import Api
from base.models import DataModel

from widgets.login_dialog import LoginDialog

from views import UiMainWidget
from base.player import Player


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # set app name before mediaObject was created to avoid phonon problem
        QCoreApplication.setApplicationName("NetEaseMusic-ThirdParty")
        self.ui = UiMainWidget()
        self.ui.setup_ui(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    musicbox = MainWidget()
    musicbox.show()
    sys.exit(app.exec_())
