import pandas as pandas
from matplotlib import pyplot as plt

from settings import ANN_MODEL_SAVE_PATH


class ChartMaker:

    def __init__(self):
        self.path = ANN_MODEL_SAVE_PATH

    def df_to_line_chart(self, df: pandas.DataFrame, filename):
        """
        이상하게 빈 화면으로 보임
        :param filename:
        :param df:
        :return:
        """

        # 그래프
        fig = df.plot(kind='line').get_figure()
        fig.savefig(f'{self.path}/{filename}.png', dpi=300)

    def scatter_chart(self, y_predict, y_data, filename):

        # 그래프
        plt.scatter(y_predict, y_data, alpha=0.4)
        plt.xlabel("Actual")
        plt.ylabel("Predicted")
        plt.title("test code")
        plt.show()
        plt.savefig(f'{self.path}/{filename}.png', dpi=300)

    pass
