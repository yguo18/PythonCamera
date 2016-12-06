# -*- coding:utf8 -*-
'''
Created on 2016.12.6

@author: yguo
'''
from scipy import linalg, dot
from numpy import eye
class Camera(object):
    '''表示针孔相机的类'''
    def __init__(self,P):
        """初始化P=[K|t]照相机模型"""
        self.P = P
        self.K = None # 标定矩阵
        self.R = None # 旋转
        self.t = None # 平移
        self.c = None # 照相机中心
        
    def project(self,X):
        """ X (4Xn的数组)的投影点，并且进行坐标归一化 """
        x = dot(self.P, X)
        for i in range(3):
            x[i] /= x[2]
        return x
        
    def rotation_matrix(self, a):
        """创建用于围绕a轴旋转的三维旋转矩阵 """
        R = eye(4)
        R[:3,:3] = linalg.expm([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
        return R
if __name__ == '__main__':
    print('3')