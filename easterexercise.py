def easter(year):
    specialyears = [1954, 1981, 2049, 2076]
    if year >= 1900 and year < 2100:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        dateofeaster = 22 + d + e
        if year in specialyears:
            dateofeaster -= 7
        return dateofeaster
    else:
        return -1

month = "March"
year = int(input("Please enter the year you would like to calculate Easter for"))
day = easter(year)
if day != -1:
    if day > 31:
        month = "April"
        day = day % 31
        print("Easter day in",year,"is",day,month)
else:
    print("Invalid year entered, year must be between 1900 and 2099")

