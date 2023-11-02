import pandas as pd
from pandas import DataFrame
import joblib
from models.telemarketing import Telemarketing


def preproces_data(data: Telemarketing) -> DataFrame:
    """
    Preprocess the data for the model

    Args:
        data (Telemarketing): The data to preprocess

    Returns:
        DataFrame: The processed data
    """
    data_dict = data.__dict__

    # Recieve the Data
    df = pd.DataFrame(data_dict, index=[0])

    # retrieve the artifacts
    pt = joblib.load("artifacts/pt.pkl")  # Load the transformer
    ohe = joblib.load("artifacts/ohe.pkl")  # Load the OnehotEncoder
    oe = joblib.load("artifacts/oe.pkl")  # Load the OrdinalEncoder
    ss = joblib.load("artifacts/ss.pkl")  # Load the StandardScaler

    # Define the columns
    binary_cols = ["default", "housing", "loan"]
    imbalanced_num_cols = ["balance", "campaign", "duration"]
    ohe_cols = ["job", "marital", "contact", "poutcome", "month"]
    oe_col = ["education"]
    num_cols = ["day", "campaign", "previous", "pdays", "balance", "duration", "age"]

    # Convert Binary columns to numerical values
    df[binary_cols] = df[binary_cols].apply(
        lambda x: x.map({"yes": 1, "no": 0}))

    # Apply the PowerTransformer
    df[imbalanced_num_cols] = pt.transform(df[imbalanced_num_cols])

    # Apply the OneHotEncoder
    ohe_data = ohe.transform(df[ohe_cols])
    ohe_df = pd.DataFrame(ohe_data.toarray(),
                          columns=ohe.get_feature_names_out(ohe_cols))
    df.drop(ohe_cols, axis=1, inplace=True)
    df = pd.concat([df.reset_index(drop=True),
                   ohe_df.reset_index(drop=True)], axis=1)

    # Apply the OrdinalEncoder
    df[oe_col] = oe.transform(df[oe_col])

    # Apply the StandardScaler
    df[num_cols] = ss.transform(df[num_cols])

    return df
