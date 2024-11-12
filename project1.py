total_rain = 0
total_wind = 0
days_count = 0

while True:
    information = input("Enter rain in inches, enter wind speed in mph, or -1.0 to finis\n")
    if information == "-1.0":
        break
    else:
        rain, wind = map(float, information.split())


        total_rain += rain
        total_wind += wind
        days_count += 1

if days_count > 0:
    rain_avarage = total_rain / days_count
    wind_avarage = total_wind / days_count
    weather = (rain_avarage * 10) + wind_avarage

    print(f"The avarage rain is {rain_avarage:.1f} inches")
    print(f"The avarage wind is {wind_avarage:.1f} mhp")
    print(f"The weather severity for these {days_count} readings is: {weather:.1f}")
else:
    print("No data entered.")