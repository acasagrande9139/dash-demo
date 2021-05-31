# def create_bar_chart_by_area(data, idx):
#     res = {}
#     for d in data:
#         if d[idx] not in res:
#             res[d[idx]] = 1
#             continue
#         res[d[idx]] += 1
#     return list(res.keys()), list(res.values())

def aggregate_data_by_field(data, field=None):
    if not field:
        return None, None
    res = data[field].value_counts()
    return list(res.keys()), list(res.values)


def index_dataframe(data, field1=None, field2=None, value1=None, value2=None, group_by_fields=None, index_type=None):
    """Index a DataFrame obj according to a basic query, including multiple values (OR operator), or using an AND operator.
    Multi-level aggregation is allowed.
    :param data: the DataFrame object
    :param field1: first DataFrame column
    :param field2: second DataFrame column
    :param value1: value to which field1 is equal
    :param value2: value to which field2 is equal
    :param group_by_fields: list of fields to be used in groupby method
    :param index_type: used to select a specific indexing condition
    :return: a list of keys and values
    """
    # data is a DataFrame obj
    # Indexing DataFrame with a simple condition
    # TODO: test it
    df = None
    res = None
    if not index_type:
        return None
    if index_type == "basic_query":
        if not (field1 and value1):
            return None
        df = data.loc[data[field1] == value1]
    if index_type == "or_query":
        if not (field1 and value1 and value2):
            return None
        df = data.loc[data[field1].isin([value1, value2])]
    if index_type == "and_query":
        if not (field1 and field2 and value1 and value2):
            return None
        df = data.loc[(data[field1] == value1) & (data[field2] == value2)]
    if df:
        if group_by_fields and isinstance(group_by_fields, list):
            df = df.groupby(group_by_fields)
    if df:
        res = df.size()
    if res:
        return list(res.keys()), list(res.values)
    return None


def generate_labels(df):
    labels = []
    for label in df.label:
        a, b = str(label).split(",")
        for char in "()[], ":
            a = a.replace(char, "")
            b = b.replace(char, "")
        s = "%s-%s" % (a, b)
        if s in labels:
            continue
        labels.append(s)
    return labels[::-1]


if __name__ == "__main__":
    pass
