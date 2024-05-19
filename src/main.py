import pandas as pd


def read_data():
    df = pd.read_csv("../data/goodreads_library_export.csv")
    # df = df[df["Read Count"] > 0]
    return df


def main():
    df = read_data()

    print(df.head())


main()
