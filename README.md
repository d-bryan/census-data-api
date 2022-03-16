# Census Bureau Data REST API

## Description

The Census Bureau Data REST API is used for retrieving data that has been gathered from the Census.
Various types of information about the United States, Apportionment about state population over time,
FIP Codes are the state and county designated FIP codes, Itemized Taxes are collected taxes over time,
and Unemployment County is unemployment rate by state and county in the United States.

[Live Demo of the API](https://census-bureau-data.herokuapp.com/)

## Routes

### Root Route

Returns to the documentation page, as there is no retrievable data on the root route. Helping the user to learn how
the application works.

For all routes below substitute `census-bureau-data.herokuapp.com` with the host you are running the application on
or `localhost:8000` or `127.0.0.1:8000`

### Apportionment

```http request
https://census-bureau-data.herokuapp.com/apportionment/

https://census-bureau-data.herokuapp.com/apportionment/state/

https://census-bureau-data.herokuapp.com/apportionment/year/

https://census-bureau-data.herokuapp.com/apportionment/pop-greater/

https://census-bureau-data.herokuapp.com/apportionment/pop-less/

https://census-bureau-data.herokuapp.com/apportionment/reps-greater/

https://census-bureau-data.herokuapp.com/apportionment/reps-less/
```

#### Example Queries

```http request
https://census-bureau-data.herokuapp.com/apportionment/state/?state=maryland

https://census-bureau-data.herokuapp.com/apportionment/year/?year=1950

https://census-bureau-data.herokuapp.com/apportionment/pop-greater/?pop=5346279

https://census-bureau-data.herokuapp.com/apportionment/pop-less/?pop=5346279

https://census-bureau-data.herokuapp.com/apportionment/reps-greater/?reps=25

https://census-bureau-data.herokuapp.com/apportionment/reps-less/?reps=25
```

### Itemized Taxes

```http request
https://census-bureau-data.herokuapp.com/itemized-taxes/

https://census-bureau-data.herokuapp.com/itemized-taxes/year/

https://census-bureau-data.herokuapp.com/itemized-taxes/state/

https://census-bureau-data.herokuapp.com/itemized-taxes/total-taxes-greater/

https://census-bureau-data.herokuapp.com/itemized-taxes/total-taxes-less/
```

#### Example Queries

```http request
https://census-bureau-data.herokuapp.com/itemized-taxes/year/?year=2020

https://census-bureau-data.herokuapp.com/itemized-taxes/state/?state=maryland

https://census-bureau-data.herokuapp.com/itemized-taxes/total-taxes-greater/?taxes=13181560

https://census-bureau-data.herokuapp.com/itemized-taxes/total-taxes-less/?taxes=13181560
```

### Unemployment County

```http request
https://census-bureau-data.herokuapp.com/unemployment-county/

https://census-bureau-data.herokuapp.com/unemployment-county/fip/

https://census-bureau-data.herokuapp.com/unemployment-county/total-fip/
```

#### Example Queries 

```http request
https://census-bureau-data.herokuapp.com/unemployment-county/fip/?fip=10005
```

## Database

There are four tables in the database as described below:

### apportionment

| id  | st  | pop | num_reps | seat_change | avg_per_rep | yr  |
|-----|-----|-----|----------|-------------|-------------|-----|


### fip_codes

| id  | full_fips | state_fips | county_fips | county | st  |
|-----|-----------|------------|-------------|--------|-----|


### itemized_taxes

| id  | st  | yr  | total_taxes  | property_taxes  | sales_and_gross_receipts_taxes  | general_sales_and_gross_receipts_taxes  | selective_sales_and_gross_receipts_taxes  | alcoholic_beverages_sales_tax  | amusements_sales_tax  | insurance_premiums_sales_tax  | motor_fuels_sales_tax  | pari_mutuels_sales_tax  | public_utilities_sales_tax  | tobacco_products_sales_tax  | other_selective_sales_and_gross_receipts_taxes  | license_taxes  | alcoholic_beverages_license  | amusements_license  | corporations_in_general_license  | hunting_and_fishing_license  | motor_vehicle_license  | motor_vehicle_operators_license  | public_utilities_license  | occupation_and_business_license_nec  | other_license_taxes  | income_taxes  | individual_income_taxes  | corporations_net_income_taxes  | other_taxes | death_and_gift_taxes | documentarty_and_stock_transfer_taxes | severance_taxes | taxes_nec |
|-----|-----|-----|--------------|-----------------|---------------------------------|-----------------------------------------|-------------------------------------------|--------------------------------|-----------------------|-------------------------------|------------------------|-------------------------|-----------------------------|-----------------------------|-------------------------------------------------|----------------|------------------------------|---------------------|----------------------------------|------------------------------|------------------------|----------------------------------|---------------------------|--------------------------------------|----------------------|---------------|--------------------------|--------------------------------|-------------|----------------------|---------------------------------------|-----------------|-----------|

### unemployment_county

| id  | full_fips | state_fips | county_fips | county_name_state | yr  | labor_force | employed | unemployed | rate |
|-----|-----------|------------|-------------|-------------------|-----|-------------|----------|------------|------|


## Environment Variables

You will need to set the following environment variables in your `.env` file for the application to work

```text
ALLOWED_ORIGINS="EXAMPLE ORIGINS FOR CORS"
```

