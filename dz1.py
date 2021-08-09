# Задача 1

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    text = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
    for i in text:
        print(i)


# Задача 3


from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby_1.csv", "r", encoding="utf-8") as hobby:

        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open("dict_n_h.json", "w", encoding="utf8") as f:
                all_list = zip_longest((" ".join(us.split(",")) for us in users), hobby, fillvalue=None)
                my_dict = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}

                dump(my_dict, f, ensure_ascii=False, indent=4)
            print(my_dict)
        else:
            exit(1)


# Задача 6

from sys import argv

with open("bakery.csv", "a", encoding="utf-8") as donut_a:
    with open("bakery.cvs", "r", encoding="utf-8")as donut_r:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace(".", "").isdigit()]:
            if len(argv) == 3:
                start, finish = map(int, argv[1:])
                print(*(v for i, v in enumerate(donut_r) if start - 1 <= i < finish), sep="")
            if "," in argv[1] or "." in argv[1]:
                if round(float(argv[1].replace(",", ".")), 3) <= 99999.999:
                    print(f'{round(float(argv[1].replace(",", ".")), 3):>010}', file=donut_a)
                else:
                    print("Number must be less than 99 999,999")
            else:
                print(*(v for i, v in enumerate(donut_r) if i >= int(argv[1]) - 1))
        else:
            print(donut_r.read())
