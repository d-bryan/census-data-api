# import sqlite3
# import os
# import pandas as pd
# from dotenv import load_dotenv
# from sqlite3 import Error
# # load environment variables
# load_dotenv()
# # ensure absolute paths are used from content root
# db_name = os.getenv("DB_NAME")
# working_directory = os.getcwd()
# db_full_path = f'{working_directory}/{db_name}'
# # create dictionaries for later use
# apportionment_data = pd.read_csv(f'{os.getcwd()}/{os.getenv("APPORTIONMENT_CSV")}')
# fips_data = pd.read_csv(f'{os.getcwd()}/{os.getenv("FIPS_CODES_CSV")}')
# unemployment_data = pd.read_csv(f'{os.getcwd()}/{os.getenv("COUNTY_UNEMPLOYMENT_RATE_CSV")}')
# itemized_taxes_data = pd.read_csv(f'{os.getcwd()}/{os.getenv("ITEMIZED_STATE_TAXES_CSV")}')
# apportionment_dict = {
#     'data': apportionment_data,
#     'sql': """INSERT INTO apportionment (st,pop,num_reps,seat_change,avg_per_rep,yr)
#     VALUES(?,?,?,?,?,?)""",
#     'table_size': 500,
#     'name': 'apportionment'
# }
# fips_dict = {
#     'data': fips_data,
#     'sql': """INSERT INTO fip_codes (full_fips,state_fips,county_fips,county,st)
#     VALUES(?,?,?,?,?)""",
#     'table_size': 3142,
#     'name': 'fip_codes'
# }
# unemployment_dict = {
#     'data': unemployment_data,
#     'sql': """INSERT INTO unemployment_county (full_fips,state_fips,county_fips,county_name_state,yr,
#     labor_force,employed,unemployed,rate)
#     VALUES(?,?,?,?,?,?,?,?,?)""",
#     'table_size': 3141,
#     'name': 'unemployment_county'
# }
# itemized_taxes_dict = {
#     'data': itemized_taxes_data,
#     'sql': """INSERT INTO itemized_taxes (st,yr,total_taxes,property_taxes,sales_and_gross_receipts_taxes,
#     general_sales_and_gross_receipts_taxes,selective_sales_and_gross_receipts_taxes,alcoholic_beverages_sales_tax,
#     amusements_sales_tax,insurance_premiums_sales_tax,motor_fuels_sales_tax,pari_mutuels_sales_tax,
#     public_utilities_sales_tax,tobacco_products_sales_tax,other_selective_sales_and_gross_receipts_taxes,
#     license_taxes,alcoholic_beverages_license,amusements_license,corporations_in_general_license,
#     hunting_and_fishing_license,motor_vehicle_license,motor_vehicle_operators_license,public_utilities_license,
#     occupation_and_business_license_nec,other_license_taxes,income_taxes,individual_income_taxes,
#     corporations_net_income_taxes,other_taxes,death_and_gift_taxes,documentarty_and_stock_transfer_taxes,
#     severance_taxes,taxes_nec)
#     VALUES(?,?,?,?,?,?,?,?,?,?,
#     ?,?,?,?,?,?,?,?,?,?,
#     ?,?,?,?,?,?,?,?,?,?,
#     ?,?,?)""",
#     'table_size': 104,
#     'name': 'itemized_taxes'
# }
#
#
# def connect_database(database):
#     """
#     Create the database if it does not exist
#     and establish a connection to it
#     :param database: path to the database
#     :return: Database connection object or none
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(database)
#         return conn
#     except Error as e:
#         print(e)
#
#     return conn
#
#
# def create_table(conn, create_table_sql):
#     """
#     Creates a table for the specific database connection
#     with the associated SQL statement
#     :param conn: Database connection
#     :param create_table_sql: SQL statement
#     """
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)
#
#
# def create_tables():
#     """
#     Create the tables for the database
#     """
#     sql_create_apportionment_table = """CREATE TABLE IF NOT EXISTS apportionment (
#         id INTEGER PRIMARY KEY,
#         st VARCHAR(100) NOT NULL,
#         pop INTEGER NOT NULL,
#         num_reps INTEGER NOT NULL,
#         seat_change INTEGER NOT NULL,
#         avg_per_rep INTEGER NOT NULL,
#         yr INTEGER NOT NULL);"""
#
#     sql_create_fips_codes_table = """CREATE TABLE IF NOT EXISTS fip_codes (
#         id INTEGER PRIMARY KEY,
#         full_fips INTEGER NOT NULL,
#         state_fips INTEGER NOT NULL,
#         county_fips INTEGER NOT NULL,
#         county VARCHAR(75) NOT NULL,
#         st VARCHAR(3) NOT NULL);"""
#
#     sql_create_county_unemployment_rate_table = """CREATE TABLE IF NOT EXISTS unemployment_county (
#         id INTEGER PRIMARY KEY,
#         full_fips INTEGER NOT NULL,
#         state_fips INTEGER NOT NULL,
#         county_fips INTEGER NOT NULL,
#         county_name_state VARCHAR(100) NOT NULL,
#         yr INTEGER NOT NULL,
#         labor_force INTEGER NOT NULL,
#         employed INTEGER NOT NULL,
#         unemployed INTEGER NOT NULL,
#         rate DOUBLE NOT NULL);"""
#
#     sql_create_itemized_state_taxes_table = """CREATE TABLE IF NOT EXISTS itemized_taxes (
#         id INTEGER PRIMARY KEY,
#         st VARCHAR (100) NOT NULL,
#         yr INTEGER NOT NULL,
#         total_taxes INTEGER NOT NULL,
#         property_taxes INTEGER NOT NULL,
#         sales_and_gross_receipts_taxes INTEGER NOT NULL,
#         general_sales_and_gross_receipts_taxes INTEGER NOT NULL,
#         selective_sales_and_gross_receipts_taxes INTEGER NOT NULL,
#         alcoholic_beverages_sales_tax INTEGER NOT NULL,
#         amusements_sales_tax INTEGER NOT NULL,
#         insurance_premiums_sales_tax INTEGER NOT NULL,
#         motor_fuels_sales_tax INTEGER NOT NULL,
#         pari_mutuels_sales_tax INTEGER NOT NULL,
#         public_utilities_sales_tax INTEGER NOT NULL,
#         tobacco_products_sales_tax INTEGER NOT NULL,
#         other_selective_sales_and_gross_receipts_taxes INTEGER NOT NULL,
#         license_taxes INTEGER NOT NULL,
#         alcoholic_beverages_license INTEGER NOT NULL,
#         amusements_license INTEGER NOT NULL,
#         corporations_in_general_license INTEGER NOT NULL,
#         hunting_and_fishing_license INTEGER NOT NULL,
#         motor_vehicle_license INTEGER NOT NULL,
#         motor_vehicle_operators_license INTEGER NOT NULL,
#         public_utilities_license INTEGER NOT NULL,
#         occupation_and_business_license_nec INTEGER NOT NULL,
#         other_license_taxes INTEGER NOT NULL,
#         income_taxes INTEGER NOT NULL,
#         individual_income_taxes INTEGER NOT NULL,
#         corporations_net_income_taxes INTEGER NOT NULL,
#         other_taxes INTEGER NOT NULL,
#         death_and_gift_taxes INTEGER NOT NULL,
#         documentarty_and_stock_transfer_taxes INTEGER NOT NULL,
#         severance_taxes INTEGER NOT NULL,
#         taxes_nec INTEGER NOT NULL);"""
#
#     # create connection
#     conn = connect_database(db_full_path)
#     if conn is not None:
#         # create
#         create_table(conn, sql_create_apportionment_table)
#         print("apportionment table successfully created")
#         create_table(conn, sql_create_fips_codes_table)
#         print("fips code table successfully created")
#         create_table(conn, sql_create_county_unemployment_rate_table)
#         print("county unemployment table successfully created")
#         create_table(conn, sql_create_itemized_state_taxes_table)
#         print("itemized taxes table successfully created")
#         conn.close()
#     else:
#         print("Error: Cannot connect to the database")
#
#
# def insert_item(conn, sql, item):
#     """
#     Insert a row into specific table
#     :param conn: Database connection
#     :param sql: INSERT STATEMENT SQL
#     :param item: Row of data to insert
#     :return: last row id
#     """
#     cur = conn.cursor()
#     cur.execute(sql, item)
#     conn.commit()
#     return cur.lastrowid
#
#
# def populate_tables():
#     """
#     Populate all the tables
#     :return:
#     """
#     create_tables()
#     insert_data(data=apportionment_dict)
#     insert_data(data=fips_dict)
#     insert_data(data=unemployment_dict)
#     insert_data(data=itemized_taxes_dict)
#
#
# def insert_data(**kwargs):
#     current_data = kwargs['data']
#     conn = connect_database(db_full_path)
#     # check for already populated data
#     cur = conn.cursor()
#     cur.execute(f"SELECT COUNT(*) FROM {current_data['name']}")
#     result = cur.fetchone()
#     if result[0] == current_data['table_size']:
#         print("table already populated...")
#         conn.close()
#         return
#     else:
#         with conn:
#             loop_data(name=current_data['name'], df=current_data['data'], conn=conn, sql=current_data['sql'])
#         conn.close()
#
#
# def loop_data(**kwargs):
#     for index, row in kwargs['df'].iterrows():
#         if kwargs['name'] == 'apportionment':
#             data = (row['state'], row['population'], row['num_reps'],
#                     row['seat_change'], row['avg_per_rep'], row['year'])
#         elif kwargs['name'] == 'fip_codes':
#             data = (row['full_fips'], row['state_fips'], row['county_fips'],
#                     row['county'], row['state'])
#         elif kwargs['name'] == 'unemployment_county':
#             data = (row['full_fips'], row['state_fips'], row['county_fips'],
#                     row['county_name_state'], row['year'], row['labor_force'],
#                     row['employed'], row['unemployed'], row['rate'])
#         elif kwargs['name'] == 'itemized_taxes':
#             data = (row['name'], row['year'], row['total_taxes'], row['property_taxes'],
#                     row['sales_and_gross_receipts_taxes'], row['general_sales_and_gross_receipts_taxes'],
#                     row['selective_sales_and_gross_receipts_taxes'], row['alcoholic_beverages_sales_tax'],
#                     row['amusements_sales_tax'], row['insurance_premiums_sales_tax'], row['motor_fuels_sales_tax'],
#                     row['pari_mutuels_sales_tax'], row['public_utilities_sales_tax'], row['tobacco_products_sales_tax'],
#                     row['other_selective_sales_and_gross_receipts_taxes'], row['license_taxes'],
#                     row['alcoholic_beverages_license'], row['amusements_license'],
#                     row['corporations_in_general_license'], row['hunting_and_fishing_license'],
#                     row['motor_vehicle_license'], row['motor_vehicle_operators_license'],
#                     row['public_utilities_license'], row['occupation_and_business_license_nec'],
#                     row['other_license_taxes'], row['income_taxes'], row['individual_income_taxes'],
#                     row['corporations_net_income_taxes'], row['other_taxes'], row['death_and_gift_taxes'],
#                     row['documentarty_and_stock_transfer_taxes'], row['severance_taxes'], row['taxes_nec'])
#         insert_item(kwargs['conn'], kwargs['sql'], data)
#     print(f"{kwargs['name']} data successfully added")
#
