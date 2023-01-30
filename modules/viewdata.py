def viewdata(location, type, bonus):
    from modules.support.support import resource_path
    import os
    from pathlib import Path
    cwd = Path.cwd()
    from rich import print
    from rich import pretty
    pretty.install()
    global sheet_ranges
    from modules import vars
    import openpyxl
    wb = openpyxl.load_workbook(filename=os.path.join(cwd, 'large-dataset.xlsx'))

    if location == 1:
        sheet_ranges = wb[vars.CAMBOURNE1987]
    elif location == 2:
        sheet_ranges = wb[vars.HEATHROW1987]
    elif location == 3:
        sheet_ranges = wb[vars.HURN1987]
    elif location == 4:
        sheet_ranges = wb[vars.LEEMING1987]
    elif location == 5:
        sheet_ranges = wb[vars.LEUCHARS1987]
    elif location == 6:
        sheet_ranges = wb[vars.CAMBOURNE2015]
    elif location == 7:
        sheet_ranges = wb[vars.HEATHROW2015]
    elif location == 8:
        sheet_ranges = wb[vars.HURN2015]
    elif location == 9:
        sheet_ranges = wb[vars.LEEMING2015]
    elif location == 10:
        sheet_ranges = wb[vars.LEUCHARS2015]


    if type == 1:
        for i in range(7, 190):
            data = str(sheet_ranges['B' + str(i)].value)
            data = data.replace(' ', '.')
            print(data)
    elif type == 2:
        for i in range(7, 190):
            data = str(sheet_ranges['C' + str(i)].value)
            data = data.replace(' ', '.')
            print(data)
    elif type == 3:
        for i in range(7, 190):
            data = str(sheet_ranges['D' + str(i)].value)
            data = data.replace(' ', '.')
            print(data)
    elif type == 4:

        if bonus == 1:
            for i in range(7, 190):
                data = str(sheet_ranges['E' + str(i)].value)
                data = data.replace(' ', '.')
                print(data)
        elif bonus == 2:
            for i in range(7, 190):
                data = str(sheet_ranges['F' + str(i)].value)
                data = data.replace(' ', '.')
                print(data)
        elif bonus == 3:
            for i in range(7, 190):
                data = str(sheet_ranges['G' + str(i)].value)
                data = data.replace(' ', '.')
                print(data)
    elif type == 5:
        for i in range(7, 190):
            data = str(sheet_ranges['H' + str(i)].value)
            data = data.replace(' ', '.')
            print(data)
    elif type == 6:
        for i in range(7, 190):
            data = str(sheet_ranges['I' + str(i)].value)
            data = data.replace(' ', '.')
            print(data)
    elif type == 7:
        for i in range(7, 190):
            data = str(sheet_ranges['J' + str(i)].value)
            data = data.replace(' ', '.')
            print(data)
    elif type == 8:
        for i in range(7, 190):
            data = str(sheet_ranges['K' + str(i)].value)
            data = data.replace(' ', '.')
            print(data)
    elif type == 9:
        if bonus == 1:
            for i in range(7, 190):
                data = str(sheet_ranges['L' + str(i)].value)
                data = data.replace(' ', '.')
                print(data)
        elif bonus == 2:
            for i in range(7, 190):
                data = str(sheet_ranges['M' + str(i)].value)
                data = data.replace(' ', '.')
                print(data)
        elif bonus == 3:
            for i in range(7, 190):
                data = str(sheet_ranges['N' + str(i)].value)
                data = data.replace(' ', '.')
                print(data)
        elif bonus == 4:
            for i in range(7, 190):
                data = str(sheet_ranges['O' + str(i)].value)
                data = data.replace(' ', '.')
                print(data)
