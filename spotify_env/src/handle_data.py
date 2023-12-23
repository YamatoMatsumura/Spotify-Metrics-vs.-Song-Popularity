import csv
import matplotlib.pyplot as plt


def parse_data(fileName, index):
    data = []
    lineCount = 0

    # loop through and assign data to correct category
    with open(fileName, encoding="utf8") as file:
        file = csv.reader(file)
        # create categories based on header
        header = next(file)
        for thing in header:
            thing = []
            # append each header as a list to data
            data.append(thing)
        for line in file:
            lineCount += 1
            try:
                # loop through and get data from each header
                for i in range(len(header)):
                    # if not a valid data point, make it 0, filtered out later
                    if len(line[i]) == 0 or line[i] == '1.4.2' or (line[i].startswith('-') and line[i][1:].isdigit()) \
                            or line[i] == '?':
                        data[i].append(0)
                    elif isinstance(line[i], (int, float)) and line[i] >= 0:
                        data[i].append(float(line[i]))
                    # checks if data is a number
                    elif isinstance(line[i], str) and line[i].replace('.', '').isdigit():
                        data[i].append(float(line[i]))
                    else:
                        # if its text, append normally
                        data[i].append(line[i])
            except IndexError:
                continue

        # find all data values with 0 and delete from data
        delColumn = []
        for value in index.values():
            for j in range(lineCount):
                if data[value][j] == 0:
                    delColumn.append(j)
        delColumn = sorted(set(delColumn), reverse=True)

        for num in delColumn:
            for i in range(len(data) - 1):
                del data[i][num]

    return data


def plot_data(xValues, yValues, xLabel, yLabel):

    plt.scatter(xValues, yValues, s=0.8)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(f'{xLabel} vs {yLabel}')
    plt.savefig(f'output_graphs/{yLabel}.png')

    plt.clf()
