# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QCMetricsFunction.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QcMetricsForm(object):
    def setupUi(self, QcMetricsForm):
        QcMetricsForm.setObjectName("QcMetricsForm")
        QcMetricsForm.resize(640, 480)
        self.layoutWidget = QtWidgets.QWidget(QcMetricsForm)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 80, 401, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.QCOpenButton = QtWidgets.QPushButton(self.layoutWidget)
        self.QCOpenButton.setObjectName("QCOpenButton")
        self.horizontalLayout.addWidget(self.QCOpenButton)
        self.QClineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.QClineEdit.setObjectName("QClineEdit")
        self.horizontalLayout.addWidget(self.QClineEdit)
        self.QCImportButton = QtWidgets.QPushButton(self.layoutWidget)
        self.QCImportButton.setObjectName("QCImportButton")
        self.horizontalLayout.addWidget(self.QCImportButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.QCSucLabel = QtWidgets.QLabel(self.layoutWidget)
        self.QCSucLabel.setObjectName("QCSucLabel")
        self.verticalLayout.addWidget(self.QCSucLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.QCCatLabel = QtWidgets.QLabel(self.layoutWidget)
        self.QCCatLabel.setObjectName("QCCatLabel")
        self.horizontalLayout_2.addWidget(self.QCCatLabel)
        self.QCcomboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.QCcomboBox.setObjectName("QCcomboBox")
        self.horizontalLayout_2.addWidget(self.QCcomboBox)
        self.QCAnalysisButton = QtWidgets.QPushButton(self.layoutWidget)
        self.QCAnalysisButton.setObjectName("QCAnalysisButton")
        self.horizontalLayout_2.addWidget(self.QCAnalysisButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(QcMetricsForm)
        QtCore.QMetaObject.connectSlotsByName(QcMetricsForm)

    def retranslateUi(self, QcMetricsForm):
        _translate = QtCore.QCoreApplication.translate
        QcMetricsForm.setWindowTitle(_translate("QcMetricsForm", "QC Metrics"))
        self.QCOpenButton.setText(_translate("QcMetricsForm", "Open"))
        self.QCImportButton.setText(_translate("QcMetricsForm", "Import"))
        self.QCSucLabel.setText(_translate("QcMetricsForm", "导入成功/失败提示"))
        self.QCCatLabel.setText(_translate("QcMetricsForm", "Category:"))
        self.QCAnalysisButton.setText(_translate("QcMetricsForm", "Analysis"))
