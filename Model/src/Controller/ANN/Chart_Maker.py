import random

import pandas as pandas
from matplotlib import pyplot as plt

from settings import CHART_SAVE_PATH
import logging
import numpy

logger = logging.getLogger(__name__)


class ChartMaker:

    def __init__(self):
        self.path = CHART_SAVE_PATH

    def df_to_line_chart(self, df: pandas.DataFrame, filename):
        """
        이상하게 빈 화면으로 보임
        :param filename:
        :param df:
        :return:
        """

        # 그래프
        logger.info(f"df_to_line_chart({type(df)}): \n {df}")
        color_list = []
        print(f"len ???: {len(df)} \n"
              f"{df}")
        for i in range(len(df.columns)):
            color_list.append(numpy.random.rand(3))
        color_list = [numpy.random.rand(3), 'c']
        print(f"color_list : {color_list}")
        fig = df.plot(kind='line', color=color_list).get_figure()
        print(f"fig : {type(fig)}\n"
              f"{fig}")
        fig.savefig(f'{self.path}/{filename}.png', dpi=300)

    def df_to_scatter_chart(self, df: pandas.DataFrame, x_name, y_name, filename):
        """
        이상하게 빈 화면으로 보임
        :param y_name:
        :param x_name:
        :param filename:
        :param df:
        :return:
        """

        # 그래프
        fig = df.plot(kind='scatter', x=x_name, y=y_name, s=1).get_figure()
        fig.savefig(f'{self.path}/{filename}.png', dpi=1000)

    def scatter_chart(self, y_predict, y_data, filename):
        # 그래프
        plt.scatter(y_predict, y_data, alpha=0.4)
        plt.xlabel("Actual")
        plt.ylabel("Predicted")
        plt.title("test code")
        plt.show()
        plt.savefig(f'{self.path}/{filename}.png', dpi=300)

    def multi_line_chart(self, data_list, filename):
        for data in data_list:
            print(data.ymdms)
            print(type(data.ymdms))
            # 내가 사용한 돈을 그래프로 그립니다
            plt.plot(data.ymdms, data.atv_power, color=numpy.random.rand(3))

        print(f"multi_line_chart: data len {len(data_list)}")
        plt.title('Line Graph w/ different markers and colors', fontsize=20)
        plt.ylabel('Cummulative Num', fontsize=14)
        plt.xlabel('Date', fontsize=14)
        plt.legend(fontsize=12, loc='best')
        # 그래프를 저장
        plt.savefig(f'{self.path}/{filename}.png', dpi=300)
