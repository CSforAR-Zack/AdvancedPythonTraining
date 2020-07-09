from matplotlib.pyplot import style, subplots, show
from datetime import datetime
from csv import reader
from os import path

filepath = f'{path.dirname(__file__)}/Little_Rock_Weather_2019.csv'

with open(filepath) as f:
    reader = reader(f)
    header_row = next(reader)
    
    # Get high and low temperatures
    highs = []
    lows = []
    dates = []
    for row in reader:
        # Look for LR Airport Station Data
        if row[0] == 'USW00003952':
            high = int(row[5])
            highs.append(high)

            low = int(row[6])
            lows.append(low)

            # Get the date and create a datetime object out of it
            date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(date)
    
# Plot the high temperatures
style.use('seaborn')
fig, ax = subplots()
ax.plot(dates, highs, c='red', alpha=0.5) # Plot highs in red line
ax.plot(dates, lows, c='blue', alpha=0.5) # Plot lows in blue line
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # Shade inbetween lines blue

# Format plot
ax.set_title('Little Rock Daily Temperatures, 2019', fontsize=26)

# X Axis
ax.set_xlabel('', fontsize=18)
fig.autofmt_xdate() # Tilt the dates to fit better

# Y Axis
ax.set_ylabel('Temperature (\u00b0F)', fontsize=18)

ax.tick_params(axis='both', which='major', labelsize=12) # Axis value font size

show() # Display the graph