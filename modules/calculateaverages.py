def calculate_averages(data1, data2):
    from statistics import median, mean, stdev, mode, correlation
    data1 = [float(i) for i in data1]
    data2 = [float(i) for i in data2]

    print('Calculating averages...')
    print('Median of data1: ' + str(median(data1)))
    print('Median of data2: ' + str(median(data2)))
    print('Mean of data1: ' + str(mean(data1)))
    print('Mean of data2: ' + str(mean(data2)))
    print('Standard deviation of data1: ' + str(stdev(data1)))
    print('Standard deviation of data2: ' + str(stdev(data2)))
    print('Mode of data1: ' + str(mode(data1)))
    print('Mode of data2: ' + str(mode(data2)))
    print('Correlation of data1 and data2: ' + str(correlation(data1, data2)))