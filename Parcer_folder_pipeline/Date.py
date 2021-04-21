import datetime


def parser():
    i = datetime.date.today()
    j = i.strftime('%m/%d/20%y')
    return j


if __name__ == "__main__":
    parser()
