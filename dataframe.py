import hw2

data = hw2.data
check_df = hw2.test_colnames(data)

if not check_df:
    raise ValueError("DataFrame does not have expected column names.")
