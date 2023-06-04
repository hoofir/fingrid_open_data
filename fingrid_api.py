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

def get_events(api_key,
               var_id, 
               start_time, 
               end_time, 
               format = 'json',
               ):
    """
    Description:
        This function is for getting data from Fingrid
        open data platform through the provided API.
    Args:
        api_key (str):  Provided personal API key
        var_id (int):   ID of the desired variable.
        start (str):    First time index of the timeseries data. {2023-04-02T00:00:00+00:00}
        end (str):      Last time index of the timeseries data. {2023-04-02T00:00:00+00:00}
        format (str):   Desired format of the receiving data e.g. {'csv','json','xml'}
    Return:
        data (*):       Timeseries of the fetched data in {'csv','json','xml'} formats.
    """
    import pandas as pd
    import requests

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

def get_last_event(api_key,
                   var_id,
                   ):
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
def data_list():
    """
    Description:
        This function returns the Fingrid open data information.
    Returns:
        Fingrid's data list in Markdown forms.
    """
    import pandas as pd
    
    path = "Avoin_data 9.6.2021.xlsx"

    df = pd.read_excel(path, index_col='ID')

    df = df.drop(columns=['NIMI','URL'])

    df = df.rename(columns={'YKSIKKÖ':'UNIT','AIKAVÄLI':'INTERVAL'})

    return print(df.to_markdown())

    # ================================================

def get_events(api_key: str,
               var_id: int, 
               start_time: str, 
               end_time: str, 
               format: str = 'json',
               ):
    """
    Description:
        This function is for getting data from Fingrid
        open data platform through the provided API.
    Args:
        api_key (str):   Provided personal API key.
        var_id (int):    ID of the desired variable.
        start (str):     Timeserie from this date e.g. {2023-04-02}.
        end (str):       Timeserie to this date e.g. {2023-05-09}.
        format (str):    Desired format of output data e.g. {JSON:'json', DataFrame:'df'}.
    Return:
        data (*):        Timeseries of the fetched data.
    """
    import pandas as pd
    import requests
    from dateutil import parser

    start_time = start_time + 'T00:00:00+00:00'
    end_time = end_time + 'T23:59:59+00:00'

    # API request configuration
    url = f'https://api.fingrid.fi/v1/variable/{var_id}/events/json'

    headers = {
        'Accept': 'application/json',
        'x-api-key': api_key,
        }
    
    params = {
        'start_time': start_time,
        'end_time': end_time,
        }

    # Make a GET request to the API
    response = requests.get(url, headers=headers, params=params)      
    
    # Check if the request was successful (status OK code: 200)
    if response.status_code == 200:

        events = response.json()

        # Convert data to Pandas DataFrame, if needed
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
        print(f"\n\nRequest failed with status code:  {response.status_code}\n")
        
        if response.status_code == 404:
            print('\nInvalid variable id.\n')
        
        elif response.status_code == 503:
            print('\nThe variable is currently on maintenance break.\n')

        elif response.status_code == 416:
            print('\nRequested row count is too large.\n')

        elif response.status_code == 422:
            print('\nInvalid input data provided.\n')

    # ================================================

def get_last_event(api_key: str,
                   var_id: int):
    """
    Description:
        This function gets the last event of a data from 
        Fingrid open data through the provided API.
    Args:
        api_key (str):  Provided personal API key
        var_id (int):   ID of the desired variable.
    Return:
        data (dict):    Dictionary of the last event.
    """   
    import requests

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

        if response.status_code == 404:
            print('\nInvalid variable id.')
        
        elif response.status_code == 503:
            print('\nThe variable is currently on maintenance break.')

    return event

    # ================================================