from fastapi import HTTPException
from data_seed.populate_data import connect_database, db_full_path

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


# MIDDLEWARE
def qualify_size(**kwargs):
    """
    Qualify the size of the data based on the parameters
    :param kwargs: start_id, end_id, difference
    :return: void
    """
    if kwargs['difference'] > 250:
        raise HTTPException(413, "Payload size too large")
    else:
        if kwargs['end_id'] < kwargs['start_id']:
            raise HTTPException(400, "End ID must be larger than starting ID")
        elif kwargs['start_id'] > kwargs['end_id']:
            raise HTTPException(400, "Start ID must be smaller than ending ID")
        elif kwargs['start_id'] <= 0:
            raise HTTPException(400, "Start ID must be greater than 0")
        elif kwargs['end_id'] >= 3142:
            raise HTTPException(400, "End ID must be smaller than max table size")


def qualify_fip(**kwargs):
    """
    Qualify the size of the data based on the parameters
    :param kwargs: fip
    :return: void
    """
    if kwargs['fip'] > 56045:
        raise HTTPException(400, "FIP must be smaller than max table size")
    elif kwargs['fip'] <= 1001:
        raise HTTPException(400, "FIP must be greater than 0")


def get_all_items(**kwargs):
    """
    Retrieve all items from database
    :param kwargs: select, schema_type
    :return: List
    """
    return add_items(select=kwargs['select'], schema_type=kwargs['schema_type'])


def get_by_range(**kwargs):
    """
    Retrieve data by range
    :param kwargs: **kwargs
    :return: List
    """
    qualify_size(start_id=int(kwargs['start_id']),
                 end_id=int(kwargs['end_id']),
                 difference=int(kwargs['end_id']) - int(kwargs['start_id']))
    return add_items(select=kwargs['select'], schema_type=kwargs['schema_type'])


def get_fip(**kwargs):
    """
    Retrieve data by specific item
    :param kwargs: **kwargs
    :return: List
    """
    qualify_fip(fip=int(kwargs['fip']))
    return add_items(select=kwargs['select'], schema_type=kwargs['schema_type'])
