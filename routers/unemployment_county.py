from fastapi import APIRouter, Query
from data_seed import crud

router = APIRouter(
    prefix='/unemployment-county',
    tags=['unemployment-county'],
    responses={404: {"msg": "data not found"}}
)


@router.get('/')
async def total():
    """
    Retrieve unemployment data in full

    :return: List of dictionaries
    """
    return crud.get_unemployment_full()


@router.get('/total-fip/')
async def total_fip():
    """
    Retrieve fip codes by in full

    :return: List of dictionaries
    """
    return crud.get_full_fip()


@router.get('/fip/')
async def by_fip(
        fip: int = Query(
            ...,
            title="FIP Value",
            description="Query the database for the unemployment data in question by fip code | "
                        "min=1001 max=13235",
            ge=1001,
            le=56045,
            example="10005"
        )
):
    """
    Retrieve unemployment data by fip code

    :param fip: FIP code
    :return: List of dictionaries
    """
    return crud.get_unemployment_by_fip(fip)
