import csv


class CSVFeed:

    @staticmethod
    def return_csv_data():
        with open("libs/data/data.csv", "r") as f:
            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)
            tmp = []
            for row in csv_reader:
                tmp.append(row)
            return tmp
