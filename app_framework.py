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
        self.pushButton_browse.clicked.connect(self.save_filename)
        self.pushButton_isCS.clicked.connect(self.handle_yes)
        self.pushButton_notCS.clicked.connect(self.handle_no)
        self.pushButton_next.clicked.connect(self.handle_next)
        self.pushButton_previous.clicked.connect(self.handle_previous)


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
        pre_index = int(np.round(0.005 / sss.dt))
        post_index = int(np.round(0.01 / sss.dt))

        self.aligned_cs = np.array([sss.voltage[i - pre_index : i + post_index ] 
            for i in sss.cs_indices])
        self.cs_indices = sss.cs_indices
        self.curr_index = 0
        self.t_axis = np.arange(self.aligned_cs.shape[1])*sss.dt
        self.plotWidget.canvas.ax.plot(self.t_axis, self.aligned_cs[self.curr_index,:])
        self.plotWidget.canvas.ax.set_xlabel('Time (s)')
        self.plotWidget.canvas.draw()
        self.open_new_info_file('./out_test')
    
    def open_new_info_file(self, filename):
        '''
        Opens an output file to save the information about the accepted 
        or rejected complex spikes.
        '''
        #self.output = open(filename, 'w')
        

    def handle_yes(self):
        self.output.write('dasdas')
        self.output.close()

    def handle_no(self):
        return

    def handle_next(self):
        if self.curr_index != self.cs_indices.size-1:
            self.curr_index = self.curr_index + 1
            self.plotWidget.canvas.ax.cla()
            self.plotWidget.canvas.ax.plot(self.t_axis, self.aligned_cs[self.curr_index,:])
            self.plotWidget.canvas.ax.set_xlabel('Time (s)')
            self.plotWidget.canvas.draw()


    def handle_previous(self):
        if self.curr_index != 0:
            self.curr_index = self.curr_index - 1
            self.plotWidget.canvas.ax.cla()
            self.plotWidget.canvas.ax.plot(self.t_axis, self.aligned_cs[self.curr_index,:])
            self.plotWidget.canvas.ax.set_xlabel('Time (s)')
            self.plotWidget.canvas.draw()






