"""fy_example3.py
this module is used to follow the quiz in week 4
thanks for tutor's work
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    year = int(year)
    tic = "QAN.AX"
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    yf_example2.yf_prc_to_csv(tic, pth, start=start, end=end)


if __name__ == "__main__":
    qan_prc_to_csv(2020) # test case