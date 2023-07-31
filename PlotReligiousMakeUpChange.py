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
        hredev = get_data(t, 'Total HRE Development')
        catholicshare = get_data(t, 'Catholic States Share of HRE Dev')
        sunnishare = get_data(t, 'Sunni States Share of HRE Dev')
        orthodoxshare = get_data(t, 'Orthodox States Share of HRE Dev')
        itr = range(1, len(hremembers) + 1)

        #plt.plot(itr, hremembers, label="Amount of HRE Members")
        #plt.plot(itr, hredev, label="Total HRE Development")
        plt.plot(itr, catholicshare, label="Catholic States Share of HRE Dev")
        plt.plot(itr, sunnishare, label="Sunni States Share of HRE Dev")
        plt.plot(itr, orthodoxshare, label="Orthodox States Share of HRE Dev")

        plt.legend(loc=2, ncol=2)

        plt.show()
