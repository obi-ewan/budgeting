import csv
from budgeting.settings import (
    ALIASES,
    CSV_HEADERS,
)


def create_debit_dict(transaction_dict):
    """
    Create & return a new dict of {'Transaction description': 'Debit Amount', ...}
    """
    debit_dict = {}

    for item in transaction_dict:
        if item['Debit Amount']:
            transaction_amt = float(item['Debit Amount'])
            transaction_name = item['Transaction description']

            name = match_aliases(transaction_name)

            try:
                print(debit_dict)
                print(match_aliases(transaction_name))
                debit_dict[name] += transaction_amt
            except KeyError:
                debit_dict[name] = transaction_amt
        else:
            continue
    return debit_dict


def match_aliases(description):
    """
    Match common Transaction descriptions, and return the aggregated description
    e.g. AMZN, AMAZON Transactions will be return as Amazon
    """
    # aggregate aliases
    for alias in ALIASES:
        alias_name = next(iter(alias.keys()))
        if any(v in description for v in alias[alias_name]):
            return alias_name
        else:
            continue
    return description


def parse_csv(filename):
    """
    Parse csv statement into a dict of relevant fields
    """
    # csv headers we are interested in
    relevant_fields = CSV_HEADERS

    with open(filename) as file:

        # parse csv and create dict from each row using our relevant_fields above
        rows = [row for row in csv.DictReader(file)]
        relevant_items = [[(k, item[k]) for k in relevant_fields] for item in rows]
        item_dict = [dict(item) for item in relevant_items]
        return item_dict


csv_file = '../data/statement.csv'
debit_dict = create_debit_dict(parse_csv(csv_file))


a = 1


