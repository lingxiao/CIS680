############################################################
# Module  : project 1: main
# Date    : April 2nd, 2018
# Author  : xiao ling
############################################################

from __future__ import print_function

import os
import pickle

import tensorflow as tf
import numpy as np
import matplotlib as plt
import math

from app import *

app = App()

############################################################
# toy neural net
############################################################

_input = np.array([1.0])

x = tf.placeholder('float', [None, n_input])





