### Week 4 lectures ### this part is in
""" yf_example2.py
Example of a function to download stock prices from Yahoo Finance.
"""
import yfinance as yf
def yf_prc_to_csv(tic, pth, start=None, end=None):
     """ Downloads stock prices from Yahoo Finance and saves the
     information in a CSV file
     Parameters
     ----------
     tic : str
        Ticker
     pth : str
        Location of the output CSV file
     start: str, optional
        Download start date string (YYYY-MM-DD)
         If None (the default), start is set to '1900-01-01'
     end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
     """
     df = yf.download(tic, start=start, end=end, ignore_tz=True)
     df.to_csv(pth)

# Example
tic = 'QAN.AX'
pth = 'qan_stk_prc.csv'
yf_prc_to_csv(tic, pth)

# REMEMBER TO DELETE THIS!!!
# This will print the value of __name__
#print(f"The value of __name__ is: '{__name__}'")

#to save stock prices to our new folder
if __name__ == "__main__":
     tic = 'QAN.AX'
     datadir = "D:\Toolkit\Toolkit\data"
     pth = fr'{datadir}\qan_stk_prc.csv'
     yf_prc_to_csv(tic, pth)


# ues os to have the same result as code above
"""
import os
pth = os.path.join(datadir, 'qan_stk_prc.csv')
"""
"""
if __name__ == "__main__":
     import os
     tic = 'QAN.AX'
     datadir = 'D:\Toolkit\Toolkit\data'
     pth = os.path.join(datadir, 'qan_stk_prc.csv')
     yf_prc_to_csv(tic, pth)
"""
# after create the module named "toolkit_config"
# we will change code above into thsi one , this is an improvement and more useful

if __name__ == "__main__":
     import os
     import toolkit_config as cfg
     tic = 'QAN.AX'
     pth = os.path.join(cfg.DATADIR, 'qan_stk_prc.csv')
     yf_prc_to_csv(tic, pth)

