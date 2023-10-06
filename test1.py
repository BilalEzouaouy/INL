import matplotlib.pyplot as plt
import numpy as np
import time

# plt.ion()  # Turn on interactive mode for live updating
# fig, ax = plt.subplots()
# x_data = []
# y_data = []
# line, = ax.plot(x_data, y_data)

# def update_plot(x, y):
#     line.set_xdata(x)
#     line.set_ydata(y)
#     ax.relim()
#     ax.autoscale_view()
#     fig.canvas.flush_events()

# while True:
#     x_data.append(len(x_data))
#     y_data.append(np.random.rand())
    
#     if len(x_data) > 10:  # Limit the number of data points to display
#         x_data.pop(0)
#         y_data.pop(0)
    
#     update_plot(x_data, y_data)
#     time.sleep(1)  # Sleep for 1 second to control the update rate

plt.ion()
fig, ax = plt.subplots()
x_data = [0]
y_data = [0]
line, = ax.plot(x_data, y_data)

while True:
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.flush_events()
    x_data.append(x_data[-1]+1)
    y_data.append(np.random.rand())

    if len(x_data) > 20:  # Limit the number of data points to display
        x_data.pop(0)
        y_data.pop(0)

    time.sleep(.01)  # Sleep for 1 second to control the update rate
    # print(f'x = {x_data}')