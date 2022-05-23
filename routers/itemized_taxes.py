from fastapi import APIRouter, Query
from data_seed import crud, schema

router = APIRouter(
    prefix='/itemized-taxes',
    tags=['itemized-taxes'],
    responses={404: {"msg": "data not found"}}
)


@router.get('/')
async def total():
    """
    Retrieve itemized taxes in full

    :return: List of dictionaries
    """
    return crud.get_all_items(select=f"SELECT * FROM itemized_taxes",
                              schema_type=schema.ItemizedTaxes)


@router.get('/state/')
async def by_state(
        state: str = Query(
            ...,
            title="State Value",
            description="Query the database for the state in question",
            min_length=2,
            max_length=20,
            example="maryland"
        )
):
    """
    Retrieve itemized taxes by state

    :param state: state
    :return: List of dictionaries
    """
    return crud.get_all_items(select=f"SELECT * FROM itemized_taxes WHERE st = '{state.lower()}'",
                              schema_type=schema.ItemizedTaxes)


@router.get('/year/')
async def by_year(
        year: int = Query(
            ...,
            title="Year Value",
            description="Query the database for the year in question, must be either 2019 or 2020",
            ge=2019,
            le=2020,
            example="2020"
        )
):
    """
    Retrieve itemized taxes by year

    :param year: year
    :return: List of dictionaries
    """
    return crud.get_all_items(select=f"SELECT * FROM itemized_taxes WHERE yr = {year}",
                              schema_type=schema.ItemizedTaxes)


@router.get('/total-taxes-greater/')
async def by_total_taxes_greater(
        taxes: int = Query(
            ...,
            title="Total Taxes Value",
            description="Query the database for the total taxes greater than specific "
                        "value in question | min=1318156 max=1093374302",
            ge=1318156,
            le=1093374302,
            example="13181560"
        )
):
    """
    Retrieve itemized taxes by total taxes - must be greater than

    :param taxes: taxes
    :return: List of dictionaries
    """
    return crud.get_all_items(select=f"SELECT * FROM itemized_taxes WHERE total_taxes >= {taxes}",
                              schema_type=schema.ItemizedTaxes)


@router.get('/total-taxes-less/')
async def by_total_taxes_less(
        taxes: int = Query(
            ...,
            title="Total Taxes Value",
            description="Query the database for the total taxes less than specific "
                        "value in question | min=1318156 max=1093374302",
            ge=1318156,
            le=1093374302,
            example="13181560"
        )
):
    """
    Retrieve itemized taxes by total taxes - must be less than

    :param taxes: taxes
    :return: List of dictionaries
    """
    return crud.get_all_items(select=f"SELECT * FROM itemized_taxes WHERE total_taxes <= {taxes}",
                              schema_type=schema.ItemizedTaxes)
