import csv


def create_debit_dict(transaction_dict):
    # create & return a new dict of {'Transaction description': float('Debit Amount'), ...}
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

    # aliases
    amazon = {'Amazon': ['Amazon', 'AMZN', 'AMAZON']}
    scottish_pwr = {'Scottish Power': ['SCOTTISHPOWER']}
    co_op = {'Co-op': ['CO-OP', 'COOP']}

    # list of aliases to check
    aliases = [amazon, scottish_pwr, co_op]

    for alias in aliases:

        alias_name = next(iter(alias.keys()))
        if any(v in description for v in alias[alias_name]):
            return alias_name
        else:
            continue
    return description


def parse_csv(filename):
    # csv headers we are interested in
    relevant_fields = ['Credit amount', 'Debit Amount', 'Transaction date', 'Transaction description']

    with open(filename) as file:

        # parse csv and create dict from each row using our relevant_fields above
        rows = [row for row in csv.DictReader(file)]
        relevant_items = [[(k, item[k]) for k in relevant_fields] for item in rows]
        item_dict = [dict(item) for item in relevant_items]
        return item_dict


csv_file = 'budgeting.csv'
debit_dict = create_debit_dict(parse_csv(csv_file))

a = 1

