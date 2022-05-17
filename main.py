import pandas as pd
import numpy as np

def openFile(file, fields):
    df = pd.read_csv(file, usecols=fields)
    return df

def task1(dataset, test_file):
    fields = ["longitude", "latitude"]
    df = openFile(dataset, fields)
    df = df.values

    file = open(test_file, "r")
    lines = file.readlines()

    for line in lines:
        line = line.replace("(", "").replace(")", "")
        line = line.split(" ")
        k = int(line[-1])
        coordinate = np.array([line[0], line[1]]).astype(float)

        distances = []
        for vector in df:
            distances.append(np.linalg.norm(coordinate - vector))

        vals = np.array(distances)
        sort_index = np.argsort(vals)[:k]
        filename = 'task1_result.txt'
        for index in sort_index:
            saveToFile(filename, index)

    file.close()


def task2(dataset, test_file):
    fields = ["longitude", "latitude", "date", "time"]
    df = openFile(dataset, fields)

    file = open(test_file, "r")
    lines = file.readlines()

    for line in lines:
        line = line.replace("(", "").replace(")", "").replace('"', "")
        line = line.strip()
        line = line.split(" ")

        k = int(line[2])
        coordinate = np.array([line[0], line[1]]).astype(float)
        start_date = line[3] + ' ' + line[4]
        end_date = line[5] + ' ' + line[6]

        df["date"] = pd.to_datetime(df['date'])
        df["period"] = df["date"].astype(str) + " " + df["time"].astype(str)
        df["period"] = pd.to_datetime(df["period"])

        period_range = (df['period'] > start_date) & (df['period'] <= end_date)
        df1 = df.loc[period_range]
        df1 = df1[["longitude", "latitude"]]
        df1 = df1.to_numpy()

        distances = []
        for vector in df1:
            distances.append(np.linalg.norm(coordinate - vector))

        vals = np.array(distances)
        sort_index = np.argsort(vals)[:k]
        filename = 'task2_result.txt'
        for index in sort_index:
            saveToFile(filename, index)

    file.close()


def task3(dataset, test_file):
    fields = ["longitude", "latitude"]
    df = openFile(dataset, fields)
    df1 = df
    df = df.to_numpy()

    df = np.absolute(df)

    lower_lim = np.absolute(np.array([149, -17]))
    upper_lim = np.absolute(np.array([151, -24]))

    in_range = np.all(np.logical_and(lower_lim <= df, df <= upper_lim), axis=1)
    df2 = df1.loc[in_range]

    vals = np.array(df2.index)
    filename = 'task3_result.txt'
    for index in vals:
        saveToFile(filename, index)


def task4(dataset, test_file):
    start_date = "2021-06-22 00:00:00"
    end_date = "2021-06-26 23:59:59"

    fields = ["longitude", "latitude", "date", "time"]
    df = openFile(dataset, fields)

    df["date"] = pd.to_datetime(df['date'])
    df["period"] = df["date"].astype(str) + " " + df["time"].astype(str)
    df["period"] = pd.to_datetime(df["period"])

    period_range = (df['period'] > start_date) & (df['period'] <= end_date)
    df1 = df.loc[period_range]
    df1 = df1[["longitude", "latitude"]]

    df2 = df1
    df1 = df1.to_numpy()

    df1 = np.absolute(df1)

    lower_lim = np.absolute(np.array([145, -17]))
    upper_lim = np.absolute(np.array([155, -24]))

    in_range = np.all(np.logical_and(lower_lim <= df1, df1 <= upper_lim), axis=1)
    df3 = df2.loc[in_range]

    vals = np.array(df3.index)
    filename = 'task4_result.txt'
    for index in vals:
        saveToFile(filename, index)


def saveToFile(output_file, data):
    with open(output_file, 'a') as file:
        file.writelines(str(data) + "\n")


def main():
    dataset = input("Dataset file: ")
    task = int(input("Enter the task numner i.e: 1,2,3,4: "))

    if task == 1:
        test_file = input("Filename: ")
        task1(dataset, test_file)
    elif task == 2:
        test_file = input("Filename: ")
        task2(dataset, test_file)
    elif task == 3:
        test_file = input("Filename: ")
        task3(dataset, test_file)
    elif task == 4:
        test_file = input("Filename: ")
        task4(dataset, test_file)
    else:
        print("invalid input")

if __name__ == "__main__":
    main()
    #test_file = "task2.txt"



