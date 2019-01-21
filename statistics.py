import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


class ScoresStatistics:

    def __init__(self, X):
        self.X = X

        ## compute the stats prms
        self.varieteNote = len(np.unique(self.X))

        self.size = self.X.size

        self.min = np.amin(self.X)
        self.max = np.amax(self.X)

        self.median = np.median(self.X)

        self.mu = self.X.mean()
        self.sigma = np.std(self.X)
        self.var = self.sigma * self.sigma

        self.q1 = np.percentile(self.X, 25)
        self.q2 = np.percentile(self.X, 50)
        self.q3 = np.percentile(self.X, 75)

        self.makePlot()

    def makePlot(self):
        ## the histogram of the data

        self.fig, self.axs = plt.subplots(2, 1)

        hist, bin_edges, patches = self.axs[0].hist(self.X, bins=20,
                                                    density=False,
                                                    facecolor='green', edgecolor='black')

        ## add a 'best fit' normal distribution
        y = norm.pdf(bin_edges, self.mu, self.sigma) * self.size
        self.axs[0].plot(bin_edges, y, 'b--', linewidth=1)

        title0 = r"Histogram of scores : $\mu={:.03},\ \sigma={:.03}$".format(self.mu,
                                                                              self.sigma)
        self.axs[0].set_title(title0)
        self.axs[0].set_xlim(0, 20)
        self.axs[0].set_xticks(np.arange(0, 21, step=1))

        ## the cumulative histogram of the data
        self.axs[1].hist(self.X, 20, histtype='step', cumulative=True)

        title1 = r"$total={}\ |\ min={:.03}\ |\ max={:.03}\ |\ median={}\ |\ σ² = {:.03}$".format(self.size,
                                                                                                  self.min,
                                                                                                  self.max,
                                                                                                  self.median,
                                                                                                  self.var)
        self.axs[1].set_title(title1)
        xlabel1 = r"$q1 = {:.03}\ |\ q2 = {:.03}\ |\ q3 = {:.03}$".format(self.q1,
                                                                          self.q2,
                                                                          self.q3)
        self.axs[1].set_xlabel(xlabel1)

        self.axs[1].set_xlim(self.min, self.max)
        self.axs[1].set_xticks(np.arange(self.min, self.max, step=1))

        ## display quartiles
        self.axs[1].plot([self.q1, self.q1], [0, self.size], 'r--',
                         [self.q2, self.q2], [0, self.size], 'r--',
                         [self.q3, self.q3], [0, self.size], 'r--')

        # adjusting
        self.fig.subplots_adjust(hspace=0.4)
        self.fig.tight_layout()

    def showPlot(self):
        plt.show()

    def savePlot(self, path):
        self.fig.savefig(path, dpi=self.fig.dpi, bbox_inches='tight')
        print("Successfully saved" + path)

    def __str__(self):
        return '''
        population   = {}
        min          = {:.03}
        max          = {:.03}
        median       = {:.03}
        μ            = {:.03}
        σ²           = {:.03}
        σ            = {:.03}
        1st quartile = {:.03}
        2nd quartile = {:.03}
        3rd quartile = {:.03}\n'''.format(self.size,
                                          self.min,
                                          self.max,
                                          self.median,
                                          self.mu,
                                          self.var,
                                          self.sigma,
                                          self.q1,
                                          self.q2,
                                          self.q3)
