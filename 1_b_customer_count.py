
from pathlib import Path
import pandas as pd


def data_read(file_name):
    relative = Path(f"data/{file_name}")
    absolute = relative.absolute()
    data = pd.read_csv(absolute)
    return data


def convert_to_date(x):
    date_str = (x[1]).astype(str)
    return date_str[0:8]


def convert_to_month(x):
    date_str = (x["hh"]).astype(str)
    return date_str[0:6]


def calculate_customer_avg():

    customer_count = data_read("participants_3a_datathon_44days.csv")
    print(f"1 There are {len(customer_count)} records...")

    customer_count["date"] = customer_count.apply(convert_to_date, axis=1)
    print(f" 2 {customer_count}")

    cell_id_mean = customer_count.groupby(["cell_id", "date"]).agg({'cx_cnt': 'sum'})
    customer_count.reset_index(level=0, inplace=True)
    print(f"{cell_id_mean}")

    site_info = data_read("datathon.cell.details.csv")
    cell_site_info = pd.merge(site_info, cell_id_mean, how="inner", on=["cell_id"])
    print(cell_site_info)

    site_mean = cell_site_info.groupby(["site_id"])["cx_cnt"].sum().to_frame()
    print(f"{site_mean}")

    site_mean = site_mean.loc[site_mean["cx_cnt"] >= 100]
    site_mean.reset_index(level=0, inplace=True)
    print(site_mean)

    print(f"######################")
    site_mean = site_mean.rename(columns={"site_id": "SITE_ID", "cx_cnt": "AVG(TOTAL_COUNT)"})
    print(site_mean)
    site_mean.to_csv("question_1_b_team_5.csv", index=False)


def main():
    calculate_customer_avg()


if __name__ == "__main__":
    main()

