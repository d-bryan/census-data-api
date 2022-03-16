from data_seed.populate_data import connect_database, db_full_path
from . import schema

conn = connect_database(db_full_path)


def base_function(select: str):
    """
    Fetch the data from database based on SQL selection
    :param select: STRING SQL
    :return: Rows from database
    """
    cur = conn.cursor()
    cur.execute(select)
    rows = cur.fetchall()
    return rows


def add_items(**kwargs):
    """
    Add items to a list depending on selection parameters
    :param kwargs: kwargs
    :return: LIST of DICT
    """
    rows = base_function(kwargs['select'])
    result = []
    for row in rows:
        current_item = kwargs['schema_type'](row)
        result.append(current_item.data)
    return result


# APPORTIONMENT START
def get_apportionment_total():
    """
    Retrieve total rows from apportionment table
    :return: List
    """
    return add_items(select='SELECT * FROM apportionment',
                     schema_type=schema.Apportionment)


def get_apportionment_by_state(state: str):
    """
    Retrieve apportionment data by state
    :param state: STRING state
    :return: List
    """
    return add_items(select=f"SELECT * FROM apportionment WHERE st = '{state}'",
                     schema_type=schema.Apportionment)


def get_apportionment_by_population_greater(pop: int):
    """
    Retrieve apportionment data by population - must be greater than
    :param pop: population size
    :return: List
    """
    return add_items(select=f"SELECT * FROM apportionment WHERE pop >= {pop}",
                     schema_type=schema.Apportionment)


def get_apportionment_by_population_less(pop: int):
    """
    Retrieve apportionment data by population - must be less than
    :param pop: population size
    :return: List
    """
    return add_items(select=f"SELECT * FROM apportionment WHERE pop <= {pop}",
                     schema_type=schema.Apportionment)


def get_apportionment_by_num_reps_greater(reps: int):
    """
    Retrieve apportionment data by number of reps - must be greater than
    :param reps: number of reps
    :return: List
    """
    return add_items(select=f"SELECT * FROM apportionment WHERE num_reps >= {reps}",
                     schema_type=schema.Apportionment)


def get_apportionment_by_num_reps_less(reps: int):
    """
    Retrieve apportionment data by number of reps - must be less than
    :param reps: number of reps
    :return: List
    """
    return add_items(select=f"SELECT * FROM apportionment WHERE num_reps <= {reps}",
                     schema_type=schema.Apportionment)


def get_apportionment_by_year(year: int):
    """
    Retrieve apportionment data by year
    :param year: year
    :return: List
    """
    return add_items(select=f"SELECT * FROM apportionment WHERE yr = {year}",
                     schema_type=schema.Apportionment)


# FIP CODES START
def get_full_fip():
    """
    Retrieve fip codes by in full
    :return: List
    """
    return add_items(select=f"SELECT * FROM fip_codes",
                     schema_type=schema.FipCodes)


def get_fip_by_state(state: str):
    """
    Retrieve fip codes by state
    :param state: STRING state
    :return: List
    """
    return add_items(select=f"SELECT * FROM fip_codes WHERE st = '{state}'",
                     schema_type=schema.FipCodes)


def get_fip_by_county(county: str):
    """
    Retrieve fip codes by county
    :param county: STRING county
    :return: List
    """
    return add_items(select=f"SELECT * FROM fip_codes WHERE county = '{county}'",
                     schema_type=schema.FipCodes)


# UNEMPLOYMENT START
def get_unemployment_full():
    """
    Retrieve unemployment data in full
    :return: List
    """
    return add_items(select=f"SELECT * FROM unemployment_county",
                     schema_type=schema.UnemploymentCounty)


def get_unemployment_by_fip(fip: int):
    """
    Retrieve unemployment data by fip code
    :param fip: FIP code
    :return: List
    """
    return add_items(select=f"SELECT * FROM unemployment_county WHERE full_fips = {fip}",
                     schema_type=schema.UnemploymentCounty)


# ITEMIZED TAXES START
def get_itemized_taxes_full():
    """
    Retrieve itemized taxes in full
    :return: List
    """
    return add_items(select=f"SELECT * FROM itemized_taxes",
                     schema_type=schema.ItemizedTaxes)


def get_itemized_taxes_by_state(state: str):
    """
    Retrieve itemized taxes by state
    :param state: STRING state
    :return: List
    """
    return add_items(select=f"SELECT * FROM itemized_taxes WHERE st = '{state}'",
                     schema_type=schema.ItemizedTaxes)


def get_itemized_taxes_by_year(year: int):
    """
    Retrieve itemized taxes by year
    :param year: INTEGER year
    :return: List
    """
    return add_items(select=f"SELECT * FROM itemized_taxes WHERE yr = {year}",
                     schema_type=schema.ItemizedTaxes)


def get_itemized_taxes_by_total_taxes_greater(total: int):
    """
    Retrieve itemized taxes by total taxes - must be greater than
    :param total: INTEGER total taxes
    :return: List
    """
    return add_items(select=f"SELECT * FROM itemized_taxes WHERE total_taxes >= {total}",
                     schema_type=schema.ItemizedTaxes)


def get_itemized_taxes_by_total_taxes_less(total: int):
    """
    Retrieve itemized taxes by total taxes - must be less than
    :param total: INTEGER total taxes
    :return: List
    """
    return add_items(select=f"SELECT * FROM itemized_taxes WHERE total_taxes <= {total}",
                     schema_type=schema.ItemizedTaxes)
