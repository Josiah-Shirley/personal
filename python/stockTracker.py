def increaseByTwoPercent(base, rate) -> float:
    base = base + (base*rate)
    return base

def findValueAfterNDays(days, principal, rate) -> float:
    for _ in range(days):
        principal = increaseByTwoPercent(principal, rate)
    return round(principal, 2)

def printValue():
    days = int(input("How many days are wanting to keep the principal invested for? > "))
    principal = float(input("How much is your principal investment? > "))
    rate = float(input("What is the expected daily rate of return [As a decimal]? > "))
    endValue = findValueAfterNDays(days, principal, rate)
    percent = str(rate*100) + "%"
    print("After", days, "days, at an increase of", percent ,"per day, your principal will be worth $" + str(endValue))

printValue()

