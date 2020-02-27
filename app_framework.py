from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
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
import gc
import csv

class MyApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton_browse.clicked.connect(self.save_filename)
        self.pushButton_isCS.clicked.connect(self.handle_yes)
        self.pushButton_notCS.clicked.connect(self.handle_no)
        self.pushButton_next.clicked.connect(self.handle_next)
        self.pushButton_previous.clicked.connect(self.handle_previous)
        self.lineEdit_goto.returnPressed.connect(self.handle_goto)
        self.lineEdit_goto.setValidator(QIntValidator())

    def closeEvent(self, event):
        if hasattr(self, 'output_f'):
            self.output_f.seek(0)
            csvwriter = csv.writer(self.output_f, delimiter = ',')
            csvwriter.writerows(self.isCS)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.handle_yes()
        if event.key() == Qt.Key_S:
            self.handle_no()
        if event.key() == Qt.Key_L:
            self.handle_previous()
        if event.key() == Qt.Key_Apostrophe:
            self.handle_next()

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
        
        
        self.cs_indices = sss.cs_indices
        self.dt = sss.dt
        self.curr_index = 0
        self.isCS = np.zeros((sss.cs_indices.size, 2), dtype = self.cs_indices.dtype) # 0: no answer | 1: Yes | -1: No 
        self.isCS[:,0] = self.cs_indices
       
        def pad(some_list, target_len):

            return np.concatenate((some_list[:target_len], [0]*(target_len - len(some_list))))

        # Prepare plotting parameter
        pre_index_zoomed = int(np.round(0.01 / sss.dt))
        post_index_zoomed = int(np.round(0.02 / sss.dt))
        wave_size_zoomed = post_index_zoomed + pre_index_zoomed

        pre_index = int(np.round(0.08 / sss.dt))
        post_index = int(np.round(0.09 / sss.dt))
        wave_size = post_index + pre_index

        #print(wave_size) 
        self.aligend_cs_zoomed = np.array([pad(sss.voltage[i - pre_index_zoomed : i + post_index_zoomed ], wave_size_zoomed) 
            for i in sss.cs_indices])

        self.aligend_cs = np.array([pad(sss.voltage[i - pre_index : i + post_index ], wave_size) 
            for i in sss.cs_indices])
        
        #self.aligend_cs_zoomed = np.array([sss.voltage[i - pre_index_zoomed : i + post_index_zoomed ] 
        #    for i in sss.cs_indices])

        #self.aligend_cs = np.array([sss.voltage[i - pre_index : i + post_index ] 
        #    for i in sss.cs_indices])
        #print(self.aligend_cs.shape)
        
        
        # Plot firt complex spike zoomed in 
        self.t_axis_zoomed = np.arange(-1*pre_index_zoomed, self.aligend_cs_zoomed.shape[1] - pre_index_zoomed)*sss.dt
        self.t_axis = np.arange(-1*pre_index, self.aligend_cs.shape[1] - pre_index)*sss.dt
        
        output_filename = self.filename + '.GMM.CS.csv'

        #output_filename = self.filename + '.csv'

        self.open_info_file(output_filename)
        self.update_plots()
        self.update_labels()
    
    def open_info_file(self, filename):
        '''
        Opens an output file to save the information about the accepted; If not exists, create a new file
        '''
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                csv_content = np.array(list(reader), dtype = self.cs_indices.dtype)  
            if csv_content.shape != (0,):
                self.isCS = csv_content
        self.output_f = open(filename, 'w+', newline='')
        

    def handle_goto(self):
        goto_index = int(self.lineEdit_goto.text())
        if goto_index < 0:
            self.curr_index = self.cs_indices.size + goto_index
        else:
            self.curr_index = goto_index
        self.update_plots()
        self.update_labels()



    def handle_yes(self):
        
        gc.collect()
        self.isCS[self.curr_index, 1] = 1
        
        if self.curr_index < self.cs_indices.size - 1:
            self.curr_index = self.curr_index + 1
            self.update_plots()
            self.update_labels()
        
        self.output_f.seek(0)
        csvwriter = csv.writer(self.output_f, delimiter = ',')
        csvwriter.writerows(self.isCS)
        #self.output.write(str(self.isCS.tolist()))
        #self.output.seek(0)
        #self.output.close()

    def handle_no(self):
        gc.collect()
        self.isCS[self.curr_index, 1] = -1
        if self.curr_index < self.cs_indices.size - 1:
            self.curr_index = self.curr_index + 1
            self.update_plots()
            self.update_labels()
            
        self.output_f.seek(0)
        csvwriter = csv.writer(self.output_f, delimiter = ',')
        csvwriter.writerows(self.isCS)
        #self.output.write(str(self.isCS.tolist()))
        #self.output.write(str(self.isCS.tolist()))
        #self.output.seek(0)
        #self.output.close()

    def handle_next(self):
        gc.collect() # garbage collection
        if self.curr_index < self.cs_indices.size - 1:
            self.curr_index = self.curr_index + 1
            self.update_plots()
            self.update_labels()
            
    def handle_previous(self):
        gc.collect() # garbage collection
        if self.curr_index > 0:
            self.curr_index = self.curr_index - 1
            self.update_plots()
            self.update_labels()
            
    def update_plots(self):
       
        self.to_plot_zoomed = self.aligend_cs_zoomed[self.curr_index,:]
        self.to_plot =  self.aligend_cs[self.curr_index,:]

        self.plotWidget.canvas.ax.cla()
        self.plotWidget.canvas.ax.plot(self.t_axis_zoomed, self.to_plot_zoomed )
        self.plotWidget.canvas.ax.plot(0, 0 , 'r*')
        self.plotWidget.canvas.ax.set_xlabel('Time (s)')
        self.plotWidget.canvas.draw()

        self.plotWidget_2.canvas.ax.cla()
        self.plotWidget_2.canvas.ax.plot(self.t_axis, self.to_plot)
        self.plotWidget_2.canvas.ax.plot(0, 0 , 'r*')
        self.plotWidget_2.canvas.ax.set_xlabel('Time (s)')
        self.plotWidget_2.canvas.draw()

    def update_labels(self):
        if self.isCS[self.curr_index, 1] == 0:
            self.label_isCS.setText('???')
        if self.isCS[self.curr_index, 1] == 1:
            self.label_isCS.setText('YES')
            self.label_isCS.setStyleSheet('background-color: green')
        if self.isCS[self.curr_index, 1] == -1:
            self.label_isCS.setText('NO')
            self.label_isCS.setStyleSheet('background-color: red')
        self.label_spikeindex.setText('{}'.format(self.curr_index))
        self.label_spiketime.setText('{} s'.format(self.cs_indices[self.curr_index]*self.dt))

