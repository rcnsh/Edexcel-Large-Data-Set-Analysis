def analyse_generated_data(data1, data2, data1name, data2name, date):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    # date formatting

    for i in range(len(date)):
        date[i] = str(date[i])

    for i in range(len(date)):
        date[i] = date[i].replace(', ', '-')
        date[i] = date[i].replace('datetime.datetime(', '')
        date[i] = date[i].replace('0, 0)', '')
        date[i] = date[i].replace(' 00:00:00', '')
        print(date[i])




    print("Choose a type of analysis:")
    print("1. Line graph (sorted)")
    print("2. Histogram")
    print("3. Scatter plot")
    print("4. Box plot")
    print("5. Pie chart")
    print("6. Bar chart")
    print("7. Exit")
    ask = int(input(""))
    if ask == 1:

        date = pd.to_datetime(date)
        DF=pd.DataFrame({'x_values': date, 'y1_values': data1, 'y2_values': data2})
        DF = DF.set_index(date)
        plt.plot( 'x_values', 'y1_values', data=DF, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)


        plt.plot('x_values', 'y2_values', data=DF, marker='', color='olive', linewidth=2)
        plt.legend()
        plt.gcf().autofmt_xdate()

        plt.title(f'Plot of {data1name} and {data2name}')
        plt.xlabel("Timestamp")
        plt.ylabel(data2name)
        plt.show()