import sys
from CVPRHelper import CVPRHelper


if __name__ == '__main__':
    kw = sys.argv[1]    
    helper = CVPRHelper(2021)
    print(f"Searching for \"{kw}\"...")
    helper.download_keyword(kw)
