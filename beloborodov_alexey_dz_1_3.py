percent_declination = [' процент', ' процента', ' процентов']
i = 0
while i < 101:
    if 5 <= i <= 20:
        print(i, percent_declination[2])
    elif (i % 10) == 1:
      print(i, percent_declination[0])
    elif 2 <= (i % 10) <= 4:
       print(i, percent_declination[1])
    else:
        print(i, percent_declination[2])
    i += 1

