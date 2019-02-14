from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import design
try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle

import numpy as np
from matplotlib import pyplot as plt
from neo.io import Spike2IO

from kaveh.behavioral import oculomotor
from kaveh.sorting import spikesorter
from kaveh.toolbox import find_file
from kaveh.plots import axvlines
import os

class MyApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton_isCS.clicked.connect(self.plot_data)
        self.pushButton_browse.clicked.connect(self.save_filename)

    def plot_data(self):
        x=range(0, 10)
        y=range(0, 20, 2)
        self.plotWidget.canvas.ax.plot(x, y, 'r.')
        self.plotWidget.canvas.draw()

    def save_filename(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()[0]
        if not filename.endswith('pkl'):
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage('File type should be pkl')
            
        else:
            self.filename = filename
            self.label_filename.setText(self.filename)
            self.load_file()

    def load_file(self):
        with open(self.filename, 'rb') as input:
            try:
                sss = pickle.load(input, encoding='latin1')
            except TypeError:
                sss = pickle.load(input)
        pre_index = int(np.round(0.002 / sss.dt))
        post_index = int(np.round(0.008 / sss.dt))

        self.aligned_cs = np.array([sss.voltage[i - pre_index : i + post_index ] 
            for i in sss.cs_indices])
        self.cs_indices = sss.cs_indices
        self.plotWidget.canvas.ax.plot(self.aligned_cs[0,:])
        self.plotWidget.canvas.draw()




