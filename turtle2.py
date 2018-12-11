from turtle import *

degree = 1      # 角度の初期値
distance = 50   # 距離の初期値


for i in range(40):   # 40回繰り返す
    forward(distance)
    right(degree)
    degree += 2
    distance -= 1

input()
