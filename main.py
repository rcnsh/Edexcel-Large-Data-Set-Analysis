from modules.viewdata import viewdata
from modules.generatedata import generatedata
from modules.askuser import askuser
from modules.calculateaverages import calculate_averages
from modules.analysegenerateddata import analyse_generated_data
from rich import print
from rich import pretty
pretty.install()

data1 = []
data2 = []

while True:
    print('1. View data')
    print('2. Generate random data and save in memory')
    print('3. Calculate averages')
    print('4. Analyse generated data')
    print('5. Read analysis')
    print('6. Exit\n')

    choice = input('Enter your choice: ')
    if choice == '1':
        userResponse = askuser()
        viewdata(userResponse[0], userResponse[1], userResponse[2])
    elif choice == '2':
        got_data = generatedata(data1, data2)
        data1 = got_data[0]
        data2 = got_data[1]
        data1name = got_data[2]
        data2name = got_data[3]
        date1 = got_data[4]
        date2 = got_data[5]
    elif choice == '3':
        if len(data1) == 0 or len(data2) == 0:
            print('You need to generate data first')
        else:
            calculate_averages(data1, data2, data1name, data2name)
    elif choice == '4':
        if len(data1) == 0 or len(data2) == 0:
            print('You need to generate data first')
        else:
            analyse_generated_data(data1, data2, data1name, data2name, date1, date2)
    elif choice == '5':
        read_analysis()
    elif choice == '6':
        break
