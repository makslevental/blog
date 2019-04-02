import matplotlib.pyplot as plt
import numpy as np

# A = 5
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')
# plt.stem(
#     [0]+[A/(n*np.pi) for n in range(1,20)],
# )
# plt.xlabel("$n$", fontsize=18)
# plt.ylabel(r"$b_n$", fontsize=24)
# plt.savefig("/home/maksim/dev_projects/makslevental.github.io/images/sawtooth_freq_plot.png")

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
A = 2/np.pi
plt.stem([0,1,2,3,4,5], [0,A,-A/2,A/3,-A/4,A/5])
plt.step([0,1,2,3,4], [0,1,1,0,0], where='post', color='red')
plt.fill_between([1,2,3], 0, 1, facecolor='red', alpha=0.3)

plt.xlabel("$n$", fontsize=18)
plt.ylabel(r"$b_n$", fontsize=24)
# plt.show()
plt.savefig("/home/maksim/dev_projects/makslevental.github.io/images/sawtooth_filter_freq_plot.png")
# # Example data
# t = np.arange(0.0, 1.0 + 0.01, 0.01)
# s = np.cos(4 * np.pi * t) + 2
#
# plt.rc('text', usetex=True)
# plt.plot(t, s)
#
# plt.xlabel(r'\textbf{time} (s)')
# plt.ylabel(r'\textit{voltage} (mV)',fontsize=16)
# plt.title(r"\TeX\ is Number "
#           r"$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
#           fontsize=16, color='gray')
# # Make room for the ridiculously large title.
# plt.subplots_adjust(top=0.8)
#
# plt.savefig('tex_demo')
# plt.show()