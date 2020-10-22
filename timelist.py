

# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy

# 调用pandas numpy库,获取一段时间内的时间列表
import pandas as pd
import numpy as np
import sys


pd.set_option('display.max_rows', None) #不限制行数
pd.set_option('display.max_columns', None)#  不显示列数


class Logger(object):
    def __init__(self, filename='default.xls', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger('a1.xls', sys.stdout)
sys.stderr = Logger('a.log_file', sys.stderr)


tm_rng = pd.bdate_range('2000-10-22 12:00:00', '2011-10-22 12:00:00', freq = '1H')
tm_series = pd.Series(np.random.randn(len(tm_rng)), index=tm_rng)

print(tm_series)

