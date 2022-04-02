from fastapi import APIRouter, Query, HTTPException
from typing import List
from data_seed import crud, schema

router = APIRouter(
    prefix='/unemployment-county',
    tags=['unemployment-county'],
    responses={
        400: {"msg": "Bad Request, check parameters"},
        404: {"msg": "data not found"},
        413: {"msg": "Request Entity Too Large"}
    }
)


@router.get('/')
async def unemployment_county_range(
        q: List[str] = Query(
            ...,
            alias='count-id',
            title="Unemployment IDs to Request",
            description="Query the database for the range of Unemployment County Data | "
                        "min=1 max=3141",
            example="739"
        )
):
    """
    Retrieve unemployment data in full

    :return: List of dictionaries
    """
    id_range = {'q': q}
    if len(q) > 2:
        raise HTTPException(400, "Too many arguments in the query, max is two")
    return crud.get_by_range(start_id=id_range['q'][0],
                             end_id=id_range['q'][1],
                             select=f"SELECT * FROM unemployment_county WHERE id BETWEEN {id_range['q'][0]} "
                                    f"AND {id_range['q'][1]} ORDER BY id",
                             schema_type=schema.UnemploymentCounty)


@router.get('/total-fip/')
async def fip_by_range(
        q: List[str] = Query(
            ...,
            alias='count-id',
            title="FIP IDs to Request",
            description="Query the database for the range of FIP Code | "
                        "min=1 max=3142",
            example="739"
        )
):
    """
    Retrieve fip codes by in full

    :return: List of dictionaries
    """
    id_range = {'q': q}
    if len(q) > 2:
        raise HTTPException(400, "Too many arguments in the query, max is two")
    return crud.get_by_range(start_id=id_range['q'][0],
                             end_id=id_range['q'][1],
                             select=f"SELECT * FROM fip_codes WHERE id BETWEEN {id_range['q'][0]} "
                                    f"AND {id_range['q'][1]} ORDER BY id",
                             schema_type=schema.FipCodes)


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
    return crud.get_fip(fip=fip, select=f"SELECT * FROM fip_codes WHERE full_fips = {fip}",
                        schema_type=schema.FipCodes)
