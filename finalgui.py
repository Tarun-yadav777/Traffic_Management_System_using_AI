from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
import shutil
import os
import subprocess

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(927, 843)
        Form.setStyleSheet("QWidget{\n"
"background-color:#3d3d3d;\n"
"}")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 927, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)

        self.title.setFont(font)
        self.title.setStyleSheet("QLabel{\n"
"color:white\n"
"}")
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 119, 911, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.type = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.type.setFont(font)
        self.type.setStyleSheet("QLabel{\n"
"color:white\n"
"}\n"
"")
        self.type.setObjectName("type")
        self.verticalLayout_2.addWidget(self.type)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 210, 911, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.picture = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.picture.setFont(font)
        self.picture.setStyleSheet("QCheckBox{\n"
"color:white;}")
        self.picture.setObjectName("picture")
        self.horizontalLayout.addWidget(self.picture)
        self.video = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.video.setFont(font)
        self.video.setStyleSheet("QCheckBox{\n"
"color:white\n"
"}")
        self.video.setObjectName("video")
        self.horizontalLayout.addWidget(self.video)
        self.cam = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.cam.setFont(font)
        self.cam.setStyleSheet("QCheckBox{\n"
"color:white\n"
"}")
        self.cam.setObjectName("cam")
        self.horizontalLayout.addWidget(self.cam)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 299, 911, 81))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"color:white\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 389, 911, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filepath = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.filepath.setStyleSheet("QLineEdit{\n"
"Background-color:white\n"
"\n"
"}")
        self.filepath.setObjectName("filepath")
        self.horizontalLayout_2.addWidget(self.filepath)
        self.browse = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.browse.setStyleSheet("QPushButton{\n"
"color:white\n"
"}")
        self.browse.setObjectName("browse")
        self.browse.clicked.connect(self.browsefile)
        self.horizontalLayout_2.addWidget(self.browse)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(330, 470, 241, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.move = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.move.setStyleSheet("QPushButton{\n"
"color:white\n"
"}")
        self.move.setObjectName("move")
        self.move.clicked.connect(self.movefile)
        self.horizontalLayout_3.addWidget(self.move)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(9, 519, 911, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.status = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.status.setStyleSheet("QLabel{\n"
"color:white\n"
"}")
        self.status.setText("")
        self.status.setObjectName("status")
        self.horizontalLayout_4.addWidget(self.status)
        self.statusButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.statusButton.setStyleSheet("QPushButton{\n"
"color:white\n"
"}")
        self.statusButton.setObjectName("statusButton")
        self.statusButton.clicked.connect(self.checkmoved)
        self.horizontalLayout_4.addWidget(self.statusButton)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(9, 579, 911, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.detectiontype = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.detectiontype.setFont(font)
        self.detectiontype.setStyleSheet("QLabel{\n"
"color:white\n"
"}")
        self.detectiontype.setObjectName("detectiontype")
        self.verticalLayout_4.addWidget(self.detectiontype)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(9, 639, 911, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.detection = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.detection.setFont(font)
        self.detection.setStyleSheet("QCheckBox{\n"
"color:white\n"
"}")
        self.detection.setObjectName("detection")
        self.horizontalLayout_5.addWidget(self.detection)
        self.tracking = QtWidgets.QCheckBox(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.tracking.setFont(font)
        self.tracking.setStyleSheet("QCheckBox{\n"
"color:white\n"
"}")
        self.tracking.setObjectName("tracking")
        self.horizontalLayout_5.addWidget(self.tracking)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(9, 689, 911, 141))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.startdetect = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.startdetect.setStyleSheet("QPushButton{\n"
"color:white\n"
"}")
        self.startdetect.setObjectName("startdetect")
        self.startdetect.clicked.connect(self.detectionfunc)
        self.horizontalLayout_6.addWidget(self.startdetect)
        self.scrollArea = QtWidgets.QScrollArea(self.horizontalLayoutWidget_6)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 807, 137))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.status_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.status_2.setGeometry(QtCore.QRect(14, 5, 781, 131))
        self.status_2.setStyleSheet("QLabel{\n"
"color:white\n"
"}")
        self.status_2.setText("")
        self.status_2.setObjectName("status_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Traffic Management System using YOLO"))
        self.title.setText(_translate("Form", "Object Detection using YOLO (You Look Only Once)"))
        self.type.setText(_translate("Form", "Select the Resource for the Object Detection :-"))
        self.picture.setText(_translate("Form", "on Picture"))
        self.video.setText(_translate("Form", "on Video"))
        self.cam.setText(_translate("Form", "on WebCam"))
        self.label.setText(_translate("Form", "Browse, Move and Check file status : -"))
        self.browse.setText(_translate("Form", "Browse"))
        self.move.setText(_translate("Form", "Move File"))
        self.statusButton.setText(_translate("Form", "Check File Status"))
        self.detectiontype.setText(_translate("Form", "Select type of Detection you want to do :-"))
        self.detection.setText(_translate("Form", "Object Detection"))
        self.tracking.setText(_translate("Form", "Object Tracking"))
        self.startdetect.setText(_translate("Form", "Start"))

    def browsefile(self):
            if self.picture.isChecked():
                    fname_picture = QFileDialog.getOpenFileName(self, 'Open File', 'C:\\Users\\tarun',
                                                                'Images (*.png, *.jpg)')
                    self.filepath.setText(fname_picture[0])
            if self.video.isChecked():
                    fname_video = QFileDialog.getOpenFileName(self, 'Open File', 'C:\\Users\\tarun',
                                                              'Video Files (*.avi *.mp4)')
                    self.filepath.setText(fname_video[0])

    def getfilename(self):
            return self.filepath.text()

    def movefile(self):
            source_path = self.getfilename()
            picture_path = 'C:\\Users\\tarun\\jupyter_projects\Yolo\\tensorflow-yolov4-tflite\\data\\images'
            video_path = 'C:\\Users\\tarun\\jupyter_projects\\Yolo\\tensorflow-yolov4-tflite\\data\\video'
            if self.picture.isChecked():
                    shutil.copy(source_path, picture_path)
            if self.video.isChecked():
                    shutil.copy(source_path, video_path)

    def checkmoved(self):
            source_path = self.getfilename()
            file_name = source_path.split("/")[-1]
            picture_path = 'C:\\Users\\tarun\\jupyter_projects\Yolo\\tensorflow-yolov4-tflite\\data\\images\\{}'.format(
                    file_name)
            video_path = 'C:\\Users\\tarun\\jupyter_projects\\Yolo\\tensorflow-yolov4-tflite\\data\\video\\{}'.format(
                    file_name)
            if self.picture.isChecked():
                    if os.path.exists(picture_path):
                            self.status.setText('File Copy Successfully')
            if self.video.isChecked():
                    if os.path.exists(video_path):
                            self.status.setText('File Copy Unsuccessful')

    def detectionfunc(self):
            source_path = self.getfilename()
            file_name = source_path.split("/")[-1]
            detect_picture = 'python detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --images ./data/images/{} --countboth'.format(
                    file_name)
            detect_video = 'python detect_video.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --video ./data/video/{} --output ./detections/{} --countboth'.format(
                    file_name, file_name)
            detect_cam = 'python detect_video.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --video 0 --output ./detections/results.avi --countboth'
            track_video = 'python object_tracker.py --video ./data/video/{} --output ./detections/{} --model yolov4'.format(
                    file_name, file_name)
            track_cam = 'python object_tracker.py --video 0 --output ./outputs/webcam.avi --model yolov4'
            if self.detection.isChecked():
                    if self.picture.isChecked():
                            result = subprocess.run(detect_picture, shell=True, capture_output=True, text=True)
                            self.status_2.setText(result.stdout)

                    if self.video.isChecked():
                            result = subprocess.run(detect_video, shell=True, capture_output=True, text=True)
                            self.status_2.setText(result.stdout)

                    if self.cam.isChecked():
                            result = subprocess.run(detect_cam, shell=True, capture_output=True, text=True)
                            self.status_2.setText(result.stdout)

            if self.tracking.isChecked():
                    if self.video.isChecked():
                            result = subprocess.run(track_video, shell=True, capture_output=True, text=True)
                            self.status_2.setText(result.stdout)
                    if self.cam.isChecked():
                            result = subprocess.run(track_cam, shell=True, capture_output=True, text=True)
                            self.status_2.setText(result.stdout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
