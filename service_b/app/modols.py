import pandas as pd
from pandas import DataFrame
from schemas import Records

    
class CleanData():

    @staticmethod
    def convert_to_dataframe(data):
        df = pd.DataFrame(data=data)
        return df
    

    @staticmethod
    def add_describe_weather_columns(df):
        df["temperature_category"] = pd.cut(df["temperature"],[0,18,25,float("inf")],labels=["cold", "moderate", "hot"],include_lowest=True)
        df["wind_status"] = pd.cut(df["wind_speed"],[0,10,float("inf")],labels=["calm", "windy"],include_lowest=True)
        return df
    
    @staticmethod
    def convert_df_to_json(df:DataFrame):
        list_of_df = df.to_dict("records")
        data = Records(record=list_of_df)
        return data.model_dump(mode="json")






    
    @staticmethod
    def main_function(data):
        to_df = CleanData.convert_to_dataframe(data)
        add_column = CleanData.add_describe_weather_columns(to_df)
        to_json = CleanData.convert_df_to_json(add_column)
        return to_json