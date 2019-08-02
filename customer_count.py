
from pathlib import Path
import pandas as pd


def data_read(file_name):
    relative = Path(f"data/{file_name}")
    absolute = relative.absolute()
    data = pd.read_csv(absolute)
    return data


def convert_to_date(x):
    date_str = (x[1]).astype(str)
    return date_str[0:6]


def calculate_customer_avg():

    customer_count = data_read("participants_3a_datathon_44days.csv")
    print(f"There are {len(customer_count)} records...")

    customer_count['hour'] = customer_count.apply(convert_to_date, axis=1)
    print(customer_count)

    customer_count = customer_count.loc[customer_count["hour"] == "201905"]
    print(customer_count)

    cell_id_mean = customer_count.groupby(["cell_id"])["cx_cnt"].mean().to_frame()
    print(f"Cell mean {cell_id_mean}")

    site_info = data_read("datathon.cell.details.csv")
    cell_site_info = pd.merge(site_info, cell_id_mean, how="inner", on=["cell_id"])
    print(cell_site_info)

    site_mean = cell_site_info.groupby(["site_id"])["cx_cnt"].mean().to_frame()
    print(f"{site_mean}")

    print(f"######################")
    site_mean.reset_index(level=0, inplace=True)
    site_mean = site_mean.rename(columns={"site_id": "SITE_ID", "cx_cnt": "AVG(TOTAL_COUNT)"})
    print(site_mean)
    site_mean.to_csv("question_1_a_team_5.csv", index=False)


def main():
    calculate_customer_avg()


if __name__ == "__main__":
    main()

