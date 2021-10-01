import matplotlib.pyplot as plt
import matplotlib.patches as patches


"""
For the first attempt, this will show two shades,
and have someone pick the brightest.
Future version will show three colors, two of which are identical,
 and have someone pick the one htat's different.
"""
class ColorMapper:

    def __init__(self):
        self.measurments = []
    
    def show_colors(self, c1, c2):

        fig, ax = plt.subplots(figsize=(10, 5))
        rect1 = patches.Rectangle((0, 0), 1, 1,
                                  linewidth=1,
                                  edgecolor='none',
                                  facecolor=c1)
        rect2 = patches.Rectangle((1, 0), 1, 1,
                                  linewidth=1,
                                  edgecolor='none',
                                  facecolor=c2)
        ax.add_patch(rect1)
        ax.add_patch(rect2)

        ax.set_xlim(0, 2)
        ax.set_ylim(0, 1)
        ax.axis('off')
        plt.show()



if __name__ == "__main__":
    cm = ColorMapper()
    cm.show_colors((.14, .14, .14),
                   (.15, .15, .15))

