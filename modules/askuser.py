def askuser():
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

    location_num = int(input('Enter your choice: '))

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
    data_type_num = int(input('Enter your choice: '))

    if data_type_num == 4:
        print("1. Wind speed")
        print("2. Wind speed (Beufort conversion)")
        print("3. Wind gust")
        bonus = int(input('Enter your choice: '))

    elif data_type_num == 9:
        print("1. Wind direction (degrees)")
        print("2. Wind direction (compass)")
        print("3. Wind Gust direction (degrees)")
        print("4. Wind Gust direction (compass)")
        bonus = int(input('Enter your choice: '))
    else:
        bonus = 0

    return location_num, data_type_num, bonus