
def data_list():
    """
    Description:
        This function returns the Fingrid's datasets' information.
    Returns:
        Fingrid's data list in Markdown forms.
    """
    path = "Avoin_data 9.6.2021.xlsx"

    import pandas as pd
   
    df = pd.read_excel(path, index_col='ID')

    df = df.drop(columns=['NIMI','URL'])

    df = df.rename(columns={'YKSIKKÖ':'UNIT','AIKAVÄLI':'INTERVAL'})

    return print(df.to_markdown())

    # ================================================

def get_events(var_id, 
               start_time, 
               end_time, 
               format = 'json',
               ):
    """
    Description:
        This function is for getting data from Fingrid
        open data platform through the provided API.
    Args:
        var_id (int):   ID of the desired variable.
        start (str):    First time index of the timeseries data. {2023-04-02T00:00:00+00:00}
        end (str):      Last time index of the timeseries data. {2023-04-02T00:00:00+00:00}
        format (str):   Desired format of the receiving data e.g. {'csv','json','xml'}
    Return:
        data (*):       Timeseries of the fetched data in {'csv','json','xml'} formats.
    """    
    import requests
    import pandas as pd

    # Provided API key
    api_key = 'ztg5duGi563hu7TyxDylU7yVc1yC2nMh66etRaxw'

    # API request configuration
    url = f'https://api.fingrid.fi/v1/variable/{var_id}/events/json'

    headers = {
        'Accept': 'application/json',
        'x-api-key': api_key,
        }

    params = {
        'start_time': start_time+'T00:00:00+00:00',
        'end_time': end_time+'T23:00:00+00:00',
        }

    # Make a GET request to the API
    response = requests.get(url, headers=headers, params=params)      
    
    # Check if the request was successful (status OK code: 200)
    if response.status_code == 200:

        events = response.json()

        # Convert data to Pandas DataFrame
        if format == 'df':

            df = pd.DataFrame(columns= list(events[0].keys()))
            df_row = {}

            for i in events:

                for key in list(i.keys()):

                    df_row[key] = i[key]

                df = pd.concat([df, pd.DataFrame(df_row, index=[0])], ignore_index=True)

            data = df

        else:
            data = events

        return data
        
    else:
        print(f"\n\nRequest failed with status code:  {response.status_code}\n\n")

    # ================================================

def get_last_event(var_id):
    """
    Description:
        This function gets the last event of a data from 
        Fingrid open data through the provided API.
    Args:
        var_id (int):   ID of the desired variable.
    Return:
        data (dict):    Dictionary of the last event.
    """   
    import requests
    import json

    # Provided API key
    api_key = "ztg5duGi563hu7TyxDylU7yVc1yC2nMh66etRaxw"

    # API endpoint & Event controller address
    api_url = f"https://api.fingrid.fi/v1/variable/{var_id}/event/json"

    # Make a GET request to the API
    response = requests.get(url= api_url,
                            params= {"variable_id": var_id,
                                     "x-api-key": api_key})
    
    # Check if the request was successful (status OK code: 200)
    if response.status_code == 200:

        event = response.json()

    else:
        print(f"\n\nRequest failed with status code:  {response.status_code}\n\n")    

    return event

    # ================================================