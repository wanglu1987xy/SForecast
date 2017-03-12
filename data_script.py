import numpy as np
import sys, os
import pandas as pd

if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]

    f = open(infile, 'r')
    fcontent = f.readlines()
    f.close()
    data_list = []

    for line in fcontent:
        col_content = line.split(' ')
        if len(col_content) > 2:
            if col_content[3]=='INFO':
                price = float(col_content[5])
                volume = float(col_content[6])
                turnover_ratio = float(col_content[7])
                if volume==0.0 or np.isnan(volume) or turnover_ratio==0.0 or np.isnan(turnover_ratio):
                    continue
                else:
                    data = {'Time':col_content[0], 'Price':price, 'Volume':volume, 'Turnover_ratio':turnover_ratio}
                    data_list.append(data)
                    print col_content[0] + ',' + col_content[1] + ',' + str(price) + ',' + str(volume) + ',' + str(turnover_ratio)

    s = pd.Series(data_list)
    s.to_csv(outfile)
    print s[0]
