# Dice simulation
from plotly.graph_objs import Bar, Layout
from plotly import offline
from os import path

from die import Die

def main():
    # Set the dice up
    numSides = 20
    die1 = Die(numSides)
    die2 = Die(numSides)

    numRolls = 100000

    # Roll the die numRoll times and store the sum of the two.
    results = []

    for roll in range(numRolls):
        result = die1.roll() + die2.roll()
        results.append(result)

    # Anaylizing the results from above.
    frequencies = []

    maxResult = die1.numSides + die2.numSides
    for value in range(2, maxResult+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # Create a graph from the results.
    x_values = list(range(2, maxResult+1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick':1}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title=f'Results of rolling two D{numSides} dice {numRolls} times', xaxis=x_axis_config, yaxis=y_axis_config)
    # Get the script directory and add the file name to it.
    filePath = f'{path.dirname(__file__)}/d{numSides}_dice_simulation.html'
    offline.plot({'data': data, 'layout': my_layout},filename=filePath)

if __name__ == '__main__':
    main()