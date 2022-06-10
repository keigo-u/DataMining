import matplotlib.pyplot as plt #モジュールのインポート

Figure = plt.figure() #全体のグラフを作成
ax1 = Figure.add_subplot(2,2,1) #1つ目のAxを作成
ax2 = Figure.add_subplot(2,2,2) #2つ目のAxを作成
ax3 = Figure.add_subplot(2,2,3) #3つ目のAxを作成
ax4 = Figure.add_subplot(2,2,4) #4つ目のAxを作成

x = [1,2,3,4,5,6,7,8,9] #x軸用のデータ
y=[1,4,9,16,25,36,49,64,81] #y軸用のデータ

ax1.plot(x,y) #1つ目のAxにデータのプロット
ax2.plot(x,y) #2つ目のAxにデータのプロット
ax3.plot(x,y) #3つ目のAxにデータのプロット
ax4.plot(x,y) #4つ目のAxにデータのプロット
plt.show()