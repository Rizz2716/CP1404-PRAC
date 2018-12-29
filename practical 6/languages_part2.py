from prac_06.programming_language import programming_lang


def main():
    ruby = programming_lang("Ruby", "Dynamic", True, 1995)
    python = programming_lang("Python", "Dynamic", True, 1991)
    visual_basic = programming_lang("Visual Basic", "Static", False, 1991)
    language_list = []
    language_list.append(ruby)
    language_list.append(python)
    language_list.append(visual_basic)

    print(language_list)


main()