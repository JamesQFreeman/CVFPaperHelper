from CVPRHelper import CVPRHelper
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def download():
    helper = CVPRHelper(2021)
    helper.download_keyword('generative')


def search():
    helper = CVPRHelper(2021)
    for id in helper.search_keyword('generative'):
        print(helper.titles[id])


def fancy_word_cloud():
    helper = CVPRHelper(2021)
    text = ' '.join(helper.titles)
    wc = WordCloud(background_color="white", height=800, width=1600)
    wc.generate(text)
    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    plt.show()
    # plt.savefig('wordcloud.jpg', dpi=500)


fancy_word_cloud()
