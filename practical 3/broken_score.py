def main():
    score = float(input("Enter score: "))
    result = check_score(score)

    print(result)
    print("Thanks")


def check_score(score):
    if score < 0 or score > 100:
        result = ("invalid score")
    else:
        if score >= 90:
            result = ("Excellent")
        elif score >= 50:
            result = ("Passable")
        else:
            result = ("Bad")
    return result


main()