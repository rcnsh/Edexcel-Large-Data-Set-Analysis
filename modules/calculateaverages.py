def calculate_averages(data1, data2, data1name, data2name):
    from rich import print
    from rich import pretty
    pretty.install()
    from statistics import median, mean, stdev, mode, correlation
    data1 = [float(i) for i in data1]
    data2 = [float(i) for i in data2]

    # string formatting
    x = data1name.split()
    data1namepart1 = x[0] + ' ' + x[1] + ' ' + x[2]
    data1namepart2 = x[4] + ' ' + x[5]

    y = data2name.split()
    data2namepart1 = y[0] + ' ' + y[1] + ' ' + y[2]
    data2namepart2 = y[4] + ' ' + y[5]



    print('Calculating averages...')
    print(f'Median of {data1namepart2} at {data1namepart1}: ' + str(median(data1)))
    print(f'Median of {data2namepart2} at {data2namepart1}: ' + str(median(data2)))
    print(f'Mean of {data1namepart2} at {data1namepart1}: ' + str(mean(data1)))
    print(f'Mean of {data2namepart2} at {data2namepart1}: ' + str(mean(data2)))
    print(f'Standard deviation of {data1namepart2} at {data1namepart1}: ' + str(stdev(data1)))
    print(f'Standard deviation of {data2namepart2} at {data2namepart2}: ' + str(stdev(data2)))
    print(f'Mode of {data1namepart2} at {data1namepart1}: ' + str(mode(data1)))
    print(f'Mode of {data2namepart2} at {data2namepart1}: ' + str(mode(data2)))
    print(f'Correlation of data1 and data2: ' + str(correlation(data1, data2)))