import random


class Country():

    def __init__(self, name, continent, language, head):
        self.name = name

        self.continent = continent
        self.language = language
        self.head = head


def search():
    nor_am = "North"
    s_am = "South America"
    eur = "Europe"
    asia = "Asia"
    afr = "Africa"

    eng = "English"
    spain = "Spain"
    port = "Portugal"
    greece = "Greece"
    itl = "Italian"
    ukr = "Ukranian"
    jpn = "Japanese"
    chn = "Chinese"
    arab = "Arabian"
    fr = "French"
    sm = "Somalian"

    pr = "President"
    pr_m = "Prime-Minister"
    pope = "Pope"
    gen_sec = "General Secretary"

    cont_arr = [nor_am, s_am, eur, asia, afr]
    lang_arr = [eng, spain, port, greece, itl, ukr, jpn, chn, arab, fr, sm]
    head_arr = [pr, pr_m, pope, gen_sec]

    country_arr = [Country("USA", nor_am, eng, pr),
                   Country("Canada", nor_am, eng, pr_m),
                   Country("Mexico", nor_am, spain, pr),
                   Country("Brazil", s_am, port, pr),
                   Country("Argentina", s_am, spain, pr),
                   Country("England", eur, eng, pr_m),
                   Country("Italy", eur, itl, pr_m),
                   Country("Spain", eur, itl, pope),
                   Country("Ukraine", eur, ukr, pr),
                   Country("China", asia, chn, gen_sec),
                   Country("Japan", asia, jpn, pr_m),
                   Country("Egypt", afr, arab, pr),
                   Country("N-country", afr, fr, pr),
                   Country("Somali", afr, sm, pr)]

    check_cont = True
    check_lang = True
    check_head = True

    while len(country_arr) != 1:
        size_coun_array = len(country_arr)
        rand_cont = random.randint(0, len(cont_arr) - 1)
        rand_lang = random.randint(0, len(lang_arr) - 1)
        rand_head = random.randint(0, len(head_arr) - 1)

        cont = cont_arr[rand_cont]
        lang_quest = lang_arr[rand_lang]
        head_quest = head_arr[rand_head]

        if check_cont:
            print("Your country located in", cont, "?")
            answer = input()

            if answer.lower() == "yes":
                country_arr = [elem for elem in country_arr if elem.continent == cont]
                check_cont = False
            else:
                country_arr = [elem for elem in country_arr if elem.continent != cont]

        if check_lang:
            print("Your country language is", lang_quest, "?")
            answer = input()

            if answer.lower() == "yes":
                country_arr = [elem for elem in country_arr if elem.language == lang_quest]
                check_lang = False
            else:
                country_arr = [elem for elem in country_arr if elem.language != lang_quest]

        if check_head:
            print("Your country head is", head_quest, "?")
            answer = input()

            if answer.lower() == "yes":
                country_arr = [elem for elem in country_arr if elem.head == head_quest]
                check_head = False
            else:
                country_arr = [elem for elem in country_arr if elem.head != head_quest]

        cont_arr.pop(rand_cont)
        lang_arr.pop(rand_lang)
        head_arr.pop(rand_head)

    print(country_arr[0].name)


search()
