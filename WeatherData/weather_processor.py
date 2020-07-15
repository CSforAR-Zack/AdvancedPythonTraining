from matplotlib.pyplot import style, subplots, show
from datetime import datetime
from csv import reader
from os import path, chdir

def main():
    dirPath = path.dirname(path.realpath(__file__))
    chdir(dirPath)

    fileName = 'Little_Rock_Weather_2019.csv'

    with open(fileName) as f:
        r = reader(f)
        headerRow = next(r)

        highs = []
        lows = []
        dates = []

        for row in r:
            if row[0] == 'USW00003952':
                high = int(row[5])
                highs.append(high)

                low = int(row[6])
                lows.append(low)

                date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(date)

    fig, ax = subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)

    ax.set_title('Little Rock Daily Temperatures, 2019', fontsize=26)

    ax.set_xlabel('Dates', fontsize=18)
    fig.autofmt_xdate()

    ax.set_ylabel('Temperatures (\u00b0F)', fontsize=18)

    show()


if __name__ == '__main__':
    main()