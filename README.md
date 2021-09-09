# CVFPaperHelper
Automatically download multiple papers by keywords in CVPR

## Install
```bash
mkdir PapersToRead
cd PaperToRead
pip install requests tqdm
git clone https://github.com/JamesQFreeman/CVFPaperHelper.git
```

## Usage
In the bash you can:

![download](/example.gif)

## Or use it as a class
```python
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
```
such as build word cloud

![wordcloud](/wordcloud.jpg)

## Have a good time!
