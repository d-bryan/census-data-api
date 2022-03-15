from fastapi import APIRouter, Query, HTTPException
from data_seed import crud

router = APIRouter(
    prefix='/apportionment',
    tags=['apportionment'],
    responses={
        404: {"msg": "data not found"}
    }
)


@router.get('/')
async def total():
    """
    Retrieve total rows from apportionment table

    :return: List of dictionary items
    """
    return crud.get_apportionment_total()


@router.get('/state/')
async def by_state(
        state: str = Query(
            ...,
            title="State Value",
            description="Query the database for the state in question",
            min_length=4,
            max_length=20,
            example="maryland"
        )
):
    """
    Retrieve apportionment data by state

    :param state: state
    :return: List of dictionary items
    """
    return crud.get_apportionment_by_state(state.lower())


@router.get('/year/')
async def by_year(
        year: int = Query(
            ...,
            title="Year Value",
            description="Query the database for the year in question, must be increments of 10 | min=1930 max=2020",
            ge=1930,
            le=2020,
            example="1950"
        )
):
    """
    Retrieve apportionment data by year

    :param year: year
    :return: List of dictionary items
    """
    if year % 10 != 0:
        raise HTTPException(status_code=400, detail={"msg": "Years must be increments of ten, "
                                                            "EX: [2020, 2010, 2000, 1990]"})
    return crud.get_apportionment_by_year(year)


@router.get('/pop-greater/')
async def by_pop_greater(
        pop: int = Query(
            ...,
            title="Population Value",
            description="Query the database for the population greater than specific "
                        "value in question | min=0 max=39576757",
            ge=0,
            le=39576757,
            example="5346279"
        )
):
    """
    Retrieve apportionment data by population - must be greater than

    :param pop: population
    :return: List of dictionary items
    """
    return crud.get_apportionment_by_population_greater(pop)


@router.get('/pop-less/')
async def by_pop_less(
        pop: int = Query(
            ...,
            title="Population Value",
            description="Query the database for the population less than specific "
                        "value in question | min=0 max=39576757",
            ge=0,
            le=39576757,
            example="5346279"
        )
):
    """
    Retrieve apportionment data by population - must be less than

    :param pop: population
    :return: List of dictionary items
    """
    return crud.get_apportionment_by_population_less(pop)


@router.get('/reps-greater/')
async def by_rep_greater(
        reps: int = Query(
            ...,
            title="Reps Value",
            description="Query the database for the number of reps greater than specific "
                        "value in question | min=0 max=53",
            ge=0,
            le=53,
            example="25"
        )
):
    """
    Retrieve apportionment data by number of reps - must be greater than

    :param reps: reps
    :return: List of dictionary items
    """
    return crud.get_apportionment_by_num_reps_greater(reps)


@router.get('/reps-less/')
async def by_rep_less(
        reps: int = Query(
            ...,
            title="Reps Value",
            description="Query the database for the number of reps less than specific "
                        "value in question | min=0 max=53",
            ge=0,
            le=53,
            example="25"
        )
):
    """
    Retrieve apportionment data by number of reps - must be less than

    :param reps: reps
    :return: List of dictionary items
    """
    return crud.get_apportionment_by_num_reps_less(reps)
