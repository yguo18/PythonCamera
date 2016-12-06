# -×- coding:utf8 -*-
'''
Created on 2016年12月6日

@author: yguo
'''
import camera
from numpy import loadtxt, vstack, hstack, eye, array
from scipy import ones, random, dot
from matplotlib.pyplot import figure, plot, show

points = loadtxt('house.p3d').T
points = vstack((points, ones(points.shape[1])))

#设置照相机参数
P = hstack((eye(3),array([[0], [0], [-10]])))
cam = camera.Camera(P)
x = cam.project(points)

# 绘制投影
figure()
plot(x[0], x[1], 'k.')

# 创建变换
r = 0.05*random.rand(3)
rot = cam.rotation_matrix(r)
figure()
for t in range(20):
    cam.P = dot(cam.P, rot)
    x = cam.project(points)
    plot(x[0], x[1], 'k.')
    show()