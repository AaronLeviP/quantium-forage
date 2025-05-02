import pandas as pd

if __name__ == '__main__':
    # Array for all csvs to open
    csvs = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
    all_data = []

    # open each csv
    for csv in csvs:
        df = pd.read_csv(csv, parse_dates=['date'])

        # df only contains the rows where product is pink morsel
        df = df[df["product"] == 'pink morsel']

        # create a new column sales and make it equal to quantity * price
        # explicitly convert quantity to be of type int, and use a lambda function to convert price into a float by dropping the first character ($)
        df["sales"] = df["quantity"].astype(int) * df["price"].apply(lambda x: float(x[1:]))

        # only take the data we need
        df = df[['date', 'region', 'sales']]
        all_data.append(df)

    # combines all the dfs that we parsed through
    combined_csvs = pd.concat(all_data)

    # sort by the date
    combined_csvs = combined_csvs.sort_values('date')

    # create the new csv file with all the data
    combined_csvs.to_csv('data/combined_data.csv', index=False)












