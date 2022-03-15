class BaseSchema:

    def __init__(self, attributes):
        self.data = {}
        self.temp = []
        self.attributes = attributes

    def populate_data(self, row):
        self.temp = list(row)
        for x in range(len(self.attributes)):
            self.data[f'{self.attributes[x]}'] = self.temp[x]


class Apportionment(BaseSchema):

    def __init__(self, row):
        super().__init__(attributes=['id', 'state', 'pop', 'reps', 'seat_change', 'avg_per_rep', 'year'])
        self.populate_data(row)


class FipCodes(BaseSchema):

    def __init__(self, row):
        super().__init__(attributes=['id', 'full_fips', 'state_fips', 'county_fips', 'county', 'state'])
        self.populate_data(row)


class UnemploymentCounty(BaseSchema):

    def __init__(self, row):
        super().__init__(attributes=['id', 'full_fips', 'state_fips', 'county_fips', 'county_name_state',
                                     'year', 'labor_force', 'employed', 'unemployed', 'rate'])
        self.populate_data(row)


class ItemizedTaxes(BaseSchema):

    def __init__(self, row):
        super().__init__(
            attributes=['id', 'st', 'yr', 'total_taxes', 'property_taxes', 'sales_and_gross_receipts_taxes',
                        'general_sales_and_gross_receipts_taxes', 'selective_sales_and_gross_receipts_taxes',
                        'alcoholic_beverages_sales_tax', 'amusements_sales_tax', 'insurance_premiums_sales_tax',
                        'motor_fuels_sales_tax', 'pari_mutuels_sales_tax', 'public_utilities_sales_tax',
                        'tobacco_products_sales_tax', 'other_selective_sales_and_gross_receipts_taxes', 'license_taxes',
                        'alcoholic_beverages_license', 'amusements_license', 'corporations_in_general_license',
                        'hunting_and_fishing_license', 'motor_vehicle_license', 'motor_vehicle_operators_license',
                        'public_utilities_license', 'occupation_and_business_license_nec', 'other_license_taxes',
                        'income_taxes', 'individual_income_taxes', 'corporations_net_income_taxes', 'other_taxes',
                        'death_and_gift_taxes', 'documentarty_and_stock_transfer_taxes', 'severance_taxes',
                        'taxes_nec'])
        self.populate_data(row)
