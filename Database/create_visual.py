from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from matplotlib.pyplot import subplots, show

from database import Day

def main():
    # Getting Static Data
    engine = create_engine("sqlite:///data.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(Day).all()
 
    highs = list()
    lows = list()
    dates = list()
        
    for day in data:
        # Highs are in column 5
        high = day.tmax
        highs.append(high)

        # Lows are in column 6
        low = day.tmin
        lows.append(low)

        # Matplotlib.pyplot needs dates in a specific format
        date = day.date
        dates.append(date)

    # Setting up Graph
    graph = subplots()
    graph_figure = graph[0]
    graph_parts = graph[1]

    # Will plot 2 lines
    graph_parts.plot(dates, highs, c="red")
    graph_parts.plot(dates, lows, c="blue")

    # Labeling Graph
    graph_parts.set_title("North Little Rock Daily Temps, 2022", fontsize=26)
    graph_parts.set_xlabel("Date", fontsize=18)
    graph_parts.set_ylabel("Temperature (\u00b0F)", fontsize=18)
    
    graph_figure.autofmt_xdate()

    # Show the graph
    show()
    
    # Save file
    # graph_figure.savefig("graph.png")


if __name__ == '__main__':
    main()