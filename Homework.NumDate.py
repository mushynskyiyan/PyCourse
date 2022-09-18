sec = int(input("Введите число от 0 до 8639999: "))
if 0 <= sec <= 8639999:
    days = sec // 86400
    hours = sec // 3600 % 24
    minutes = sec // 60 % 60
    seconds = sec % 60
    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)
    lst = ["4", "5", "6", "7", "8", "9"]
    if days == 0 or str(days)[-1] in lst:
        pronoun = "дней"
    elif days == 1 or str(days)[-1] == "1":
        pronoun = "день"
    else:
        pronoun = "дня"
    date = f"{days} {pronoun}, {hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}"
    print(date)
else:
    print("Ошибка 404,в следующий раз введите правильное число")