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
        plt.show(block=False)
    
    def query_colors(self, c1, c2):
        self.show_colors(c1, c2)
        answer = input("Which is darker? (1 or 2) ")
        while answer not in ('1', '2'):
            answer = input("Please enter 1 or 2: ")
        return int(answer)
    
    def choose_colors(self):
        """Choose two colors based on current data"""

    def run_trial(self, n):
        for i in range(n):
            c1, c2 = self.choose_colors()
            answer = self.query_colors(c1, c2)
            # add colors to dataset
        
        # save data to file
        







if __name__ == "__main__":
    cm = ColorMapper()
    cm.show_colors((.14, .14, .14),
                   (.15, .15, .15))

