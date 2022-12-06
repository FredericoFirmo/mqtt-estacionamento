from PyQt5 import QtCore, QtGui, QtWidgets
from paho.mqtt import client as mqtt_client
from Tela import Ui_MainWindow
from mqttSubscriber import Subscriber


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    client = Subscriber.connect_mqtt()
    status = Subscriber.subscribe(client,ui,MainWindow)
    client.loop_start()
    #client.loop_stop()
    sys.exit(app.exec_())