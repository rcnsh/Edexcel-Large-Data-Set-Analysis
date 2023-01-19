def analyse_generated_data(data1, data2, data1name, data2name, date):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    # date formatting

    for i in range(len(date)):
        date[i] = str(date[i])

    for i in range(1, len(data1)):
        data1[i] = float(data1[i])

    for i in range(1, len(data2)):
        data2[i] = float(data2[i])

    for i in range(len(date)):
        date[i] = date[i].replace(', ', '-')
        date[i] = date[i].replace('datetime.datetime(', '')
        date[i] = date[i].replace('0, 0)', '')
        date[i] = date[i].replace(' 00:00:00', '')
        print(date[i])




    print("Choose a type of analysis:")
    print("1. Line graph (separate graphs")
    print("2. Bar chart")
    print("3. Scatter plot")
    print("4. Box plot")
    print("5. Pie chart")
    print("6. Histogram")
    print("7. Exit")
    ask = int(input(""))
    if ask == 1:

        date = pd.to_datetime(date)

        fig, ax1 = plt.subplots()
        ax1.plot_date(date, data1, 'k-')
        plt.gcf().autofmt_xdate()
        plt.title(f'Plot of {data1name} against time.')
        plt.xlabel("Timestamp")
        plt.ylabel(f"{data1name}")
        plt.show()

        fig, ax2 = plt.subplots()
        ax2.plot_date(date, data2, 'k-')
        plt.gcf().autofmt_xdate()
        plt.title(f'Plot of {data2name} against time.')
        plt.xlabel("Timestamp")
        plt.ylabel(f"{data2name}")
        plt.show()
    if ask == 2:

        x = np.arange(len(date))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, data1, width, label=data1name)
        rects2 = ax.bar(x + width / 2, data2, width, label=data2name)

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(f"{data1name} in blue, {data2name}, in orange.")
        ax.set_title(f'Plot of Data1 and Data2 over time')
        ax.set_xticks(x, date)
        ax.legend()

        ax.bar_label(rects1, padding=3,)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()
        plt.gcf().autofmt_xdate()
        plt.show()