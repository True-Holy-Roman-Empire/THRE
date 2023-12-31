from matplotlib import pyplot as plt
import pandas as pd

def get_data(t, i):
    lst = []
    loc = 0

    while True:
        loc = t.find(i, loc)

        if loc != -1:
            end = t.find('\n', loc)
            lst.append(float(t[loc:end].strip().split(':')[1].strip()))
            loc = end
        else:
            break

    return lst

if __name__ == '__main__':
    with open('game.log') as f:
        t = f.read()
        
        hremembers = get_data(t, 'Amount of HRE Members')
        nonabrahamic = get_data(t, 'Nations that are not Abrahamic share of HRE Dev')
        catholicshare = get_data(t, 'Catholic (ABR) States Share of HRE Dev')
        sunnishare = get_data(t, 'Sunni (ABR) States Share of HRE Dev')
        orthodoxshare = get_data(t, 'Orthodox (ABR) States Share of HRE Dev')
        abreformdesire = get_data(t, 'Abrahamic Reform Desire')
        itr = range(1, len(hremembers) + 1)

        plt.plot(itr, hremembers, label="Amount of HRE Members")
        plt.plot(itr, nonabrahamic, label="Nations that are not Abrahamic share of HRE Dev in %")
        plt.plot(itr, catholicshare, label="Catholic States Share of HRE Dev in %")
        plt.plot(itr, sunnishare, label="Sunni States Share of HRE Dev in %")
        plt.plot(itr, orthodoxshare, label="Orthodox States Share of HRE Dev in %")
        plt.plot(itr, abreformdesire, label="Abrahamic Reform Desire")

        plt.legend(loc=2, ncol=2)

        plt.show()
