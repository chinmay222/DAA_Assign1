import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

get_ipython().run_line_magic('matplotlib', 'nbagg')
pwd = os.getcwd()
os.chdir('..')
graph_data = open("points.txt", 'r').read()
lines = graph_data.split('\n')
xs = []
ys = []
for line in lines:
    if len(line) > 1:
        x,y=line.split(',')
        xs.append(float(x))
        ys.append(float(y))
os.chdir(pwd)
graph_data = open("hull.txt", 'r').read()
lines = graph_data.split('\n')
x_line = []

y_line = []
for line in lines:
    if len(line) > 1:
        x,y=line.split(',')
        x_line.append(float(x))
        y_line.append(float(y))
x_line.append(x_line[0])  
y_line.append(y_line[0]) 
x = x_line
y = y_line

fig, ax = plt.subplots()
line1, = ax.plot(x, y, color = "b")

plt.scatter(xs, ys, color='black')
def update(num, x, y, line1):
    line1.set_data(x[0:num+1], y[0:num+1])
    return [line1]

ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line1],
                  interval=500, repeat=True)
ani.save('RESULTS.gif')
plt.show() 