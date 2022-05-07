import requests
import csv
from datetime import datetime
import time

def main():
    url = input('Enter your url: ')
    field = input('Enter the field you want to export: ')
    number  = int(input('How many times want to hit the API?: '))
    throttle  = float(input('How many miliseconds (ex:0.01) / seconds (ex: 1) time interval between each request?: '))

    i = 0
    data = []
    while i < number :
        response = requests.get(url)
        api_field = response.json()[field]
        data.append([api_field])
        i = i +1
        time.sleep(throttle)

    export_to_csv(data)


def export_to_csv(data):
    folder = 'exports/'
    filename = folder + datetime.now().strftime("%Y_%m_%d__%H-%M-%S") + '.csv'

    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter = ',')
        writer.writerows(data)

main()