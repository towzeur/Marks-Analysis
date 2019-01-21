import numpy as np

from get_scores import getScoresFromFile
from statistics import ScoresStatistics


def main(srcPath, dstPath):
    scoresList = getScoresFromFile(srcPath)
    scores = np.array(scoresList)

    # getting the stc
    stc = ScoresStatistics(scores)
    print(stc)

    # display the figure
    stc.showPlot()

    # save fig
    stc.savePlot(dstPath)


if __name__ == '__main__':
    scoresPath = "notes.txt"
    figPath = "notes_proba_1a.png"

    main(scoresPath, figPath)
