def generatedata(data1, data2):
    global sheet_ranges
    from modules import vars
    import openpyxl
    wb = openpyxl.load_workbook(filename='data/large-dataset.xlsx')
    dataquantity = int(input('Enter the number of data points to generate: '))
    offset = (183 // dataquantity) - 1
    for i in range(0, 2):
        print(i)
        if i == 0:
            print('Generating data set 1...')
        elif i == 1:
            print('Generating data set 2...')
        else:
            print('Maximum data sets reached')
            print('Clearing data sets...')
            print('Generating data set 1...')
            i = 0
            data1.clear()
            data2.clear()
            return

        print('Choose a location from the options below: ')
        print('1. Cambourne, United Kingdom (1987)')
        print('2. Heathrow, United Kingdom (1987)')
        print('3. Hurn, United Kingdom (1987)')
        print('4. Leeming, United Kingdom (1987)')
        print('5. Leuchars, United Kingdom (1987)')
        print('6. Cambourne, United Kingdom (2015)')
        print('7. Heathrow, United Kingdom (2015)')
        print('8. Hurn, United Kingdom (2015)')
        print('9. Leeming, United Kingdom (2015)')
        print('10. Leuchars, United Kingdom (2015)')

        choice = int(input('Enter your choice: '))
        if choice == 1:
            sheet_ranges = wb[vars.CAMBOURNE1987]
        elif choice == 2:
            sheet_ranges = wb[vars.HEATHROW1987]
        elif choice == 3:
            sheet_ranges = wb[vars.HURN1987]
        elif choice == 4:
            sheet_ranges = wb[vars.LEEMING1987]
        elif choice == 5:
            sheet_ranges = wb[vars.LEUCHARS1987]
        elif choice == 6:
            sheet_ranges = wb[vars.CAMBOURNE2015]
        elif choice == 7:
            sheet_ranges = wb[vars.HEATHROW2015]
        elif choice == 8:
            sheet_ranges = wb[vars.HURN2015]
        elif choice == 9:
            sheet_ranges = wb[vars.LEEMING2015]
        elif choice == 10:
            sheet_ranges = wb[vars.LEUCHARS2015]

        print('Choose a parameter from the options below: ')
        print('1. Mean temperature')
        print('2. Total rainfall')
        print('3. Total sunshine')
        print('4. Mean wind speed')
        print('5. Relative humidity')
        print('6. Mean cloud cover')
        print('7. Mean visibility')
        print('8. Mean pressure')
        print('9. Wind direction')

        choice2 = int(input('Enter your choice: '))
        if choice2 == 1:
            for j in range(7, 190, offset):
                data = str(sheet_ranges['B' + str(j)].value)
                if data == 'n/a':
                    print("WARNING: n/a value found. This may mess up your data.")
                    continue
                data = data.replace(' ', '.')
                print(data)
                if i == 0:
                    data1.append(data)
                elif i == 1:
                    data2.append(data)
        elif choice2 == 2:
            for j in range(7, 190, offset):
                data = str(sheet_ranges['C' + str(j)].value)
                if data == 'n/a':
                    print("WARNING: n/a value found. This may mess up your data.")
                    continue
                data = data.replace(' ', '.')
                print(data)
                if i == 0:
                    data1.append(data)
                elif i == 1:
                    data2.append(data)
        elif choice2 == 3:
            for j in range(7, 190, offset):
                data = str(sheet_ranges['D' + str(j)].value)
                if data == 'n/a':
                    print("WARNING: n/a value found. This may mess up your data.")
                    continue
                data = data.replace(' ', '.')
                print(data)
                if i == 0:
                    data1.append(data)
                elif i == 1:
                    data2.append(data)
        elif choice2 == 4:
            print("1. Wind speed")
            print("2. Wind speed (Beufort conversion)")
            print("3. Wind gust")
            choice3 = int(input('Enter your choice: '))
            if choice3 == 1:
                for j in range(7, 190, offset):
                    data = str(sheet_ranges['E' + str(j)].value)
                    if data == 'n/a':
                        print("WARNING: n/a value found. This may mess up your data.")
                        continue
                    data = data.replace(' ', '.')
                    print(data)
                    if i == 0:
                        data1.append(data)
                    elif i == 1:
                        data2.append(data)
            elif choice3 == 2:
                for j in range(7, 190, offset):
                    data = str(sheet_ranges['F' + str(j)].value)
                    if data == 'n/a':
                        print("WARNING: n/a value found. This may mess up your data.")
                        continue
                    data = data.replace(' ', '.')
                    print(data)
                    if i == 0:
                        data1.append(data)
                    elif i == 1:
                        data2.append(data)
            elif choice3 == 3:
                for j in range(7, 190, offset):
                    data = str(sheet_ranges['G' + str(j)].value)
                    if data == 'n/a':
                        print("WARNING: n/a value found. This may mess up your data.")
                        continue
                    data = data.replace(' ', '.')
                    print(data)
                    if i == 0:
                        data1.append(data)
                    elif i == 1:
                        data2.append(data)
        elif choice2 == 5:
            for j in range(7, 190, offset):
                data = str(sheet_ranges['H' + str(j)].value)
                if data == 'n/a':
                    print("WARNING: n/a value found. This may mess up your data.")
                    continue
                data = data.replace(' ', '.')
                print(data)
                if i == 0:
                    data1.append(data)
                elif i == 1:
                    data2.append(data)
        elif choice2 == 6:
            for j in range(7, 190, offset):
                data = str(sheet_ranges['I' + str(j)].value)
                if data == 'n/a':
                    print("WARNING: n/a value found. This may mess up your data.")
                    continue
                data = data.replace(' ', '.')
                print(data)
                if i == 0:
                    data1.append(data)
                elif i == 1:
                    data2.append(data)
        elif choice2 == 7:
            for j in range(7, 190, offset):
                data = str(sheet_ranges['J' + str(j)].value)
                if data == 'n/a':
                    print("WARNING: n/a value found. This may mess up your data.")
                    continue
                data = data.replace(' ', '.')
                print(data)
                if i == 0:
                    data1.append(data)
                elif i == 1:
                    data2.append(data)
        elif choice2 == 8:
            for j in range(7, 190, offset):
                data = str(sheet_ranges['K' + str(j)].value)
                if data == 'n/a':
                    print("WARNING: n/a value found. This may mess up your data.")
                    continue
                data = data.replace(' ', '.')
                print(data)
                if i == 0:
                    data1.append(data)
                elif i == 1:
                    data2.append(data)
        elif choice2 == 9:
            print("1. Wind direction (degrees)")
            print("2. Wind direction (compass)")
            print("3. Wind Gust direction (degrees)")
            print("4. Wind Gust direction (compass)")
            choice4 = int(input('Enter your choice: '))
            if choice4 == 1:
                for j in range(7, 190, offset):
                    data = str(sheet_ranges['L' + str(j)].value)
                    if data == 'n/a':
                        print("WARNING: n/a value found. This may mess up your data.")
                        continue
                    data = data.replace(' ', '.')
                    print(data)
                    if i == 0:
                        data1.append(data)
                    elif i == 1:
                        data2.append(data)
            elif choice4 == 2:
                for j in range(7, 190, offset):
                    data = str(sheet_ranges['M' + str(j)].value)
                    if data == 'n/a':
                        print("WARNING: n/a value found. This may mess up your data.")
                        continue
                    data = data.replace(' ', '.')
                    print(data)
                    if i == 0:
                        data1.append(data)
                    elif i == 1:
                        data2.append(data)
            elif choice4 == 3:
                for j in range(7, 190, offset):
                    data = str(sheet_ranges['N' + str(j)].value)
                    if data == 'n/a':
                        print("WARNING: n/a value found. This may mess up your data.")
                        continue
                    data = data.replace(' ', '.')
                    print(data)
                    if i == 0:
                        data1.append(data)
                    elif i == 1:
                        data2.append(data)
            elif choice4 == 4:
                for j in range(7, 190, offset):
                    data = str(sheet_ranges['O' + str(j)].value)
                    if data == 'n/a':
                        print("WARNING: n/a value found. This may mess up your data.")
                        continue
                    data = data.replace(' ', '.')
                    print(data)
                    if i == 0:
                        data1.append(data)
                    elif i == 1:
                        data2.append(data)

        if i == 0:
            i += 1
        elif i == 1:
            i += 1
    print('Data1: ' + str(data1))
    print('Data2: ' + str(data2))
    return data1, data2
