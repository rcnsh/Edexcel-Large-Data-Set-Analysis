def analyse_generated_data(data1, data2, data1name, data2name, date1, date2):
    from rich import print
    from rich import pretty
    pretty.install()
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import click
    # date formatting
    click.clear()
    print("Reformatting dates and data")
    print("This may take a while...")

    for i in range(len(date1)):
        date1[i] = str(date1[i])

    for i in range(1, len(data1)):
        data1[i] = float(data1[i])

    for i in range(1, len(data2)):
        data2[i] = float(data2[i])

    for i in range(len(date1)):
        date1[i] = date1[i].replace(', ', '-')
        date1[i] = date1[i].replace('datetime.datetime(', '')
        date1[i] = date1[i].replace('0, 0)', '')
        date1[i] = date1[i].replace(' 00:00:00', '')

    for i in range(len(date2)):
        date2[i] = str(date2[i])

    for i in range(len(date2)):
        date2[i] = date2[i].replace(', ', '-')
        date2[i] = date2[i].replace('datetime.datetime(', '')
        date2[i] = date2[i].replace('0, 0)', '')
        date2[i] = date2[i].replace(' 00:00:00', '')
    click.clear()
    print("Choose a type of analysis:")
    print("1. Line graph (separate graphs")
    print("2. Bar chart")
    print("3. Exit")
    ask = int(input(""))
    if ask == 1:

        date1 = pd.to_datetime(date1)
        date2 = pd.to_datetime(date2)

        fig, ax1 = plt.subplots()
        ax1.plot(date1, data1)
        plt.gcf().autofmt_xdate()
        plt.title(f'Plot of {data1name} against time.')
        plt.xlabel("Timestamp")
        plt.ylabel(f"{data1name}")
        fig.canvas.manager.set_window_title(f'Plot of {data1name} against time.')

        fig, ax2 = plt.subplots()
        ax2.plot_date(date2, data2, 'k-')
        plt.gcf().autofmt_xdate()
        plt.title(f'Plot of {data2name} against time.')
        plt.xlabel("Timestamp")
        plt.ylabel(f"{data2name}")
        fig.canvas.manager.set_window_title(f'Plot of {data2name} against time.')
        plt.show()
    if ask == 2:

        x = np.arange(len(date1))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, data1, width, label=data1name)
        rects2 = ax.bar(x + width / 2, data2, width, label=data2name)

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(f"{data1name} in blue, {data2name}, in orange.")
        ax.set_title(f'Plot of Data1 and Data2 over time')
        ax.set_xticks(x, date1)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()
        plt.gcf().autofmt_xdate()
        plt.show()

    if ask == 3:
        click.clear()
        return 0