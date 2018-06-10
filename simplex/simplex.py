# -*- coding: utf-8 -*-

import sys
import numpy as np

a = np.array([[1, 1, -1],
             [2, -2, 1],
             [1, 1, -2],
             [0, -1, -1]])
a = a.astype(float)

#メイン関数
def main(arr, PErow, PEcol):
  if answerJudge(arr) == False:
    if stopJudge(arr, PEcol) == True:
      sweepOut(arr, PErow, PEcol)
      PEcol = findPEcol(arr)
      PErow = findPErow(arr,PEcol)
      main(arr, PErow, PEcol)
    else:
      print("最適解はありません")
      sys.exit()
  else:
    print("最適解は")
    for i in range(len(arr)-1):
      print("x{} = [{}]".format(i+1,arr[len(arr)-2-i][0]))
    print("Z = {}".format(arr[len(arr)-1][0]))
    sys.exit()


#ピボットエレメントの行番号を取得
def findPEcol(arr):
  for i in range(len(arr)-1):
    if arr[len(arr)-1][i] <= 0:
      PEcol = i
  PEcolumnValue = arr[len(arr)-1][0]
  for i in range(len(arr[0])-1):
    if abs(PEcolumnValue) < abs(arr[len(arr)-1][i+1]):
      if arr[len(arr)-1][i+1] <= 0:
        PEcol = i+1
        PEcolumnValue = arr[len(arr)-1][i+1]
  return PEcol
 

#ピボットエレメントの列番号を取得
def findPErow(arr, PEcol):
  PErow = 0
  for i in range(len(arr)-2):
    if arr[i+1][PEcol] > 0 and arr[PErow][0]/arr[PErow][PEcol] > arr[i+1][0]/arr[i+1][PEcol]:
      PErow = i+1
  print("PEは[{}][{}]の{}".format(PErow, PEcol, arr[PErow][PEcol]))
  return PErow


#掃き出しの計算
def sweepOut(arr, PErow, PEcol):
  b = np.empty([len(arr),len(arr[0])])
  b = b.astype(float)
  for i in range(len(arr[0])):
    b[PErow,i] /= arr[PErow,PEcol]
  for i in range(len(arr)):
    if i != PErow:
      for j in range(len(arr[0])):
        b[i][j] = arr[i][j] - b[PErow,j] * arr[i][PEcol]
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      arr[i][j] = b[i][j]
  print(arr)


#最適解の有無の判定
def stopJudge(arr, PEcol):
  for i in range(len(arr)):
    if arr[i][PEcol] > 0:
      return True
      break
    else:
      return False

#停止条件の判定
def answerJudge(arr):
  for i in range(len(arr[0])):
    if arr[len(arr)-1][i] < 0:
      return False
      break
  return True

print(a)
PEcol = findPEcol(a)
PErow = findPErow(a,PEcol)
main(a,PErow,PEcol)
