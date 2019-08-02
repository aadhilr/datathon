
from pathlib import Path
import pandas as pd


def data_read(file_name):
    relative = Path(f"data/{file_name}")
    absolute = relative.absolute()
    data = pd.read_csv(absolute)
    return data


def convert_to_date(x):
    date_str = (x[1]).astype(str)
    return date_str[-2:]


def calculate_customer_count():
    customer_count = data_read('participants_3a_datathon_44days.csv')
    print(f"There are {len(customer_count)} records...")
    customer_count['hour'] = customer_count.apply(convert_to_date, axis=1)
    cell_id_mean = customer_count.groupby(["cell_id", "hour"])["cx_cnt"].mean()
    print(cell_id_mean)


def main():
    calculate_customer_count()


if __name__ == "__main__":
    main()