# Dice simulation
from pygal import Bar
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
    graph = Bar()

    graph.title = f'Results of rolling two D{numSides} die {numRolls} times.'

    # Create the x labels
    graph.x_labels = []
    for x in range(2, maxResult+1):
        graph.x_labels.append(f'{x}')

    # Add axii titles.
    graph.x_title = 'Result'
    graph.y_title = 'Frequency of Result'

    graph.add(f'D{numSides} + D{numSides}', frequencies) # Add teh frequencies to the graph

    # Get the script directory and add the file name to it.
    filePath = f'{path.dirname(__file__)}/d{numSides}_dice_simulation.svg'
    graph.render_to_file(filePath) # Create the visual file.

if __name__ == '__main__':
    main()