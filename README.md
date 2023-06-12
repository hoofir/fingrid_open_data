# Fingrid Open Data via API
Fingrid's open data platform provides machine readable access to datasets through open **REST API** interface.


## How to Get Started
1. Make sure you have an active email address.
2. Do [register](https://data.fingrid.fi/open-data-forms/registration/) and approve the license and terms of use. 
3. You will receive a personal API-key right away. If you don't receive the email, please check your Junk Mail folder.
4. Registered users may opt-in to receive email maintenance breaks or other important changes about API.
5. If you want, you can also [delete your account](https://data.fingrid.fi/open-data-forms/leave/) and the related API-key.


## How to Fetch the Data
1. Clone the repository into your local machine.
2. Add the full path to folder `fingrid_open_data` to your system's path via `sys.path.append("C:/.../.../fingrid_open_data/")`.
3. Run `fingrid_api.data_list()` command to see the full list of the available datasets.
4. Choose the data you want and find out its ID from previous step or [here](https://github.com/hoofir/fingrid_open_data/edit/main/README.md#list-of-the-available-datasets-source).
5. Use `fingrid_api.get_ts()` to get timeseries data, and `fingrid_api.get_latest()` to get the latest value of the corresponding data.

* Make sure you have installed these packages: `pandas`  `requests`


## Information for Developers
Technical API documentation for developers:  http://data.fingrid.fi/open-data-api/

- API requests to this endpoint:  https://api.fingrid.fi/
- For an individual variable, you can get the latest event or events from a specified date/time range. For a set of variables, you can get the latest events.
- You can access data in JSON, XML or CSV formats.
- You can make [custom searches](https://data.fingrid.fi/open-data-forms/search/en/) for each dataset. Each dataset has an unique link to the search interface. 
- Each dataset has a unique `VariableId` number that you need to use in API requests. See them all in [here](https://github.com/hoofir/fingrid_open_data/blob/main/README.md#list-of-the-available-datasets). 
- API-key must be inserted to the http-request header `x-api-key`, not into the URL-address. If you are importing data from the API into an application, it is usually possible to insert the API-key by modifying the request header parameters in your application.
- You can make 10,000 requests in 24h period with one API-key. Please contact the [administrator](mailto:avoindata@fingrid.fi) if you need to make more requests.
- Data timestamps are presented in `UTC` (previously as GMT) time format. Correct format for API requests is `YYYY-MM-ddTHH:mm:ssZ` e.g. 2023-04-02T00:00:00+00:00
- Data update frequency varies by dataset: many datasets have data that is updated hourly, and some datasets include data that is updated in 3 or 5 minute intervals. The update frequency is stated in the dataset description.
- If you request frequently updated data from an extended date range, you may receive an error message that results from exceeding the maximum allowed API payload. Shorten the date range and request the results in JSON-format. 
- If you use the API in browser environment, you need to note the requirements and limitations for Cross Origin Resource Sharing ([CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS)). 
 

## Example of one response  
<div class="snippet_json" style="display: block;">
        <pre><code class="hljs json">[
  {
    "<span class="hljs-attr">end_time</span>": <span class="hljs-string">"string"</span>,
    "<span class="hljs-attr">start_time</span>": <span class="hljs-string">"string"</span>,
    "<span class="hljs-attr">value</span>": <span class="hljs-number">0</span>
  }
]</code></pre>

  
## Availability and uptime
The open data API is not guaranteed to have 100% uptime. Although maximum uptime is a goal, as with any service disruptions can happen at any point along the networks and Internet between the client application and the API servers. Make your application defensive that can handle API downtime gracefully. One such way could be by implementing good caching. Another strategy could be to aim for graceful failure if the API is not available. 


## List of the available datasets ([source](https://fingrid-public.s3-eu-west-1.amazonaws.com/files/Avoin+data+tietoaineistoluettelo+9.6.2021.xlsx))

|   ID | NAME                                                                                     | UNIT      | INTERVAL   |
|-----:|:-----------------------------------------------------------------------------------------|:----------|:-----------|
|  252 | Activated down-regulation power                                                          | MW        | 15 min     |
|  253 | Activated up-regulation power                                                            | MW        | 3 min      |
|   53 | Automatic Frequency Restoration Reserve, activated, down                                 | MWh/h     | 1 h        |
|   54 | Automatic Frequency Restoration Reserve, activated, up                                   | MWh/h     | 1 h        |
|    2 | Automatic Frequency Restoration Reserve, capacity, down                                  | MW        | 1 h        |
|    1 | Automatic Frequency Restoration Reserve, capacity, up                                    | MW        | 1 h        |
|   51 | Automatic Frequency Restoration Reserve, price, down                                     | €/MWh     | 1 h        |
|   52 | Automatic Frequency Restoration Reserve, price, up                                       | €/MW      | 1 h        |
|  270 | Balancing Capacity Market bids                                                           | MW        | 1 wk       |
|  262 | Balancing Capacity Market price                                                          | €         | 1 wk       |
|  261 | Balancing Capacity Market results                                                        | MW        | 1 wk       |
|   68 | Bilateral trade between FI-RUS                                                           | MWh/h     | 1 h        |
|  101 | Bilateral trade capacity FI-RUS                                                          | MW        | 1 h        |
|   49 | Bilateral trade capacity FI-RUS, unused                                                  | MW        | 1 h        |
|   65 | Bilateral trade capacity RUS-FI                                                          | MW        | 1 h        |
|   64 | Bilateral trade capacity RUS-FI, unused                                                  | MW        | 1 h        |
|  201 | Cogeneration of district heating - real time data                                        | MW        | 3 min      |
|  140 | Commercial transmission of electricity between FI-EE                                     | MWh/h     | 1 h        |
|   31 | Commercial transmission of electricity between FI-SE1                                    | MWh/h     | 1 h        |
|   32 | Commercial transmission of electricity between FI-SE3                                    | MWh/h     | 1 h        |
|  189 | Condensing power production - real time data                                             | MW        | 3 min      |
|   48 | Congestion income between FI-EE                                                          | €         | 1 h        |
|   70 | Congestion income between FI-SE1                                                         | €         | 1 h        |
|   71 | Congestion income between FI-SE3                                                         | €         | 1 h        |
|   86 | Cross-border transmission fee, export to Russia                                          | €/MWh     | 1 h        |
|   85 | Cross-border transmission fee, import from Russia                                        | €/MWh     | 1 h        |
|  112 | Day-ahead transmission capacity EE-FI – official                                         | MW        | 1 h        |
|  115 | Day-ahead transmission capacity FI-EE – official                                         | MW        | 1 h        |
|   26 | Day-ahead transmission capacity FI-SE1 – official                                        | MW        | 1 h        |
|  143 | Day-ahead transmission capacity FI-SE1 – planned                                         | MW        | 1 h        |
|   27 | Day-ahead transmission capacity FI-SE3 – official                                        | MW        | 1 h        |
|  145 | Day-ahead transmission capacity FI-SE3 – planned                                         | MW        | 1 h        |
|   24 | Day-ahead transmission capacity SE1-FI – official                                        | MW        | 1 h        |
|  142 | Day-ahead transmission capacity SE1-FI – planned                                         | MW        | 1 h        |
|  144 | Day-ahead transmission capacity SE3-FI  – planned                                        | MW        | 1 h        |
|   25 | Day-ahead transmission capacity SE3-FI – official                                        | MW        | 1 h        |
|  251 | Down-regulation bids, price of the last activated - real time data                       | €/MWh     | 1 h        |
|  106 | Down-regulation price in the Balancing energy market                                     | €/MWh     | 1 h        |
|  165 | Electricity consumption forecast - next 24 hours                                         | MWh/h     | 1 h        |
|  166 | Electricity consumption forecast - updated hourly                                        | MWh/h     | 1 h        |
|  124 | Electricity consumption in Finland                                                       | MWh/h     | 1 h        |
|  193 | Electricity consumption in Finland - real time data                                      | MW        | 3 min      |
|   74 | Electricity production in Finland                                                        | MWh/h     | 1h         |
|  192 | Electricity production in Finland - real time data                                       | MW        | 3 min      |
|  242 | Electricity production prediction - premilinary                                          | MWh/h     | 1 h        |
|  241 | Electricity production prediction - updated hourly                                       | MWh/h     | 1 h        |
|  205 | Electricity production, reserve power plants and small-scale production - real time data | MW        | 3 min      |
|  198 | Electricity production, surplus/deficit - real time data                                 | MW        | 3 min      |
|  265 | Emission factor for electricity consumed in Finland - real time data                     | gCO2/kWh  | 3 min      |
|  266 | Emission factor of electricity production in Finland - real time data                    | gCO2/kWh  | 3 min      |
|  277 | Fast Frequency Reserve FFR, price                                                        | €/MW      | 1 h        |
|  276 | Fast Frequency Reserve FFR, procured volume                                              | MW        | 1 h        |
|  278 | Fast Frequency Reserve FFR, procurement forecast                                         | MW        | 1 h        |
|  275 | Fast Frequency Reserve FFR, received bids                                                | MW        | 1 h        |
|  nan | Frequency - historical data                                                              | Hz        | 1 h        |
|  177 | Frequency - real time data                                                               | Hz        | 3 min      |
|   82 | Frequency containment reserve for disturbances, procured volumes in hourly market        | MW        | 1 h        |
|  286 | Frequency containment reserve for disturbances, received bids in hourly market           | MW        | 1 h        |
|  123 | Frequency Containment Reserve for Normal operation, activated                            | MWh/h     | 1 h        |
|  287 | Frequency Containment Reserve for Normal operation, foreign trade                        | MW        | 1 h        |
|  285 | Frequency Containment Reserve for Normal operation, hourly market bids                   | MW        | 1h         |
|   79 | Frequency Containment Reserve for Normal operation, hourly market prices                 | €/MW      | 1 h        |
|   80 | Frequency Containment Reserve for Normal operation, hourly market volumes                | MW        | 1 h        |
|  288 | Frequency Containment Reserve for Normal operation, yearly market plans                  | MW        | 1 h        |
|   81 | Frequency containment reserves for disturbances, hourly market prices                    | €/MW      | 1 h        |
|  289 | Frequency containment reserves for disturbances, nordic trade                            | MW        | 1 h        |
|  290 | Frequency containment reserves for disturbances, reserve plans in the yearly market      | MW        | 1 h        |
|  239 | Hour change regulation, down-regulation                                                  | MWh/h (?) | 1 h        |
|  240 | Hour change regulation, up-regulation                                                    | MWh/h     | 1 h        |
|  191 | Hydro power production - real time data                                                  | MW        | 3 min      |
|  176 | Imbalance power between Finland and Sweden                                               | MWh/h     | 1 h        |
|  202 | Industrial cogeneration - real time data                                                 | MW        | 3 min      |
|  110 | Intraday transmission capacity EE-FI                                                     | MW        | 1 h        |
|  111 | Intraday transmission capacity EE-FI – real time data                                    | MW        | 1 h        |
|  113 | Intraday transmission capacity FI-EE                                                     | MW        | 1 h        |
|  114 | Intraday transmission capacity FI-EE – real time data                                    | MW        | 1 h        |
|   50 | Intraday transmission capacity FI-RUS                                                    | MW        | 1 h        |
|   44 | Intraday transmission capacity FI-SE1                                                    | MW        | 1 h        |
|   45 | Intraday transmission capacity FI-SE3                                                    | MW        | 1 h        |
|   66 | Intraday transmission capacity RUS-FI                                                    | MW        | 1 h        |
|   38 | Intraday transmission capacity SE1-FI                                                    | MW        | 1 h        |
|   39 | Intraday transmission capacity SE3-FI                                                    | MW        | 1 h        |
|  260 | Kinetic energy of the Nordic power system - real time data                               | GWs       | 1 min      |
|   30 | Measured transmission of electricity in Finland from north to south                      | MWh/h     | 1 h        |
|  194 | Net import/export of electricity - real time data                                        | MW        | 3 min      |
|  188 | Nuclear power production - real time data                                                | MW        | 3 min      |
|   33 | Ordered down-regulations from Balancing energy market in Finland                         | MWh/h     | 1 h        |
|   34 | Ordered up-regulations from Balancing energy market in Finland                           | MWh/h     | 1 h        |
|  213 | Other power transactions, down-regulation                                                | MWh/h     | 1 h        |
|  214 | Other power transactions, up-regulation                                                  | MWh/h     | 1 h        |
|  183 | Peak load power - real time data                                                         | MW        | 3 min      |
|   41 | Planned transmission capacity FI-RUS                                                     | MW        | 1 h        |
|  127 | Planned transmission capacity RUS-FI                                                     | MW        | 1 h        |
|   28 | Planned weekly capacity from north to south                                              | MWh/h     | 1 h        |
|   29 | Planned weekly capacity from south to north                                              | MWh/h     | 1 h        |
|  209 | Power system state - real time data                                                      | "1"       | 3 min      |
|   22 | Price of the last activated up-regulation bid - real time data                           | €/MWh     | 1 h        |
|  180 | Sähkönsiirto Suomen ja Viron välillä - reaaliaikatieto                                   | MW        | 3 min      |
|  248 | Solar power generation forecast - updated hourly                                         | MWh/h     | 1 h        |
|  247 | Solar power generation forecast - updated once a day                                     | MWh/h     | 1 h        |
|  118 | Special regulation, down-regulation                                                      | nan       | 1 h        |
|  119 | Special regulation, up-regulation                                                        | MWh/h     | 1 h        |
|  102 | Stock exchange capacity FI-RUS                                                           | MW        | 1 h        |
|   67 | Stock exchange capacity RUS-FI                                                           | MW        | 1 h        |
|   69 | Stock exchange trade FI-RUS-FI                                                           | MWh/h     | 1 h        |
|  186 | Surplus/deficit, cumulative - real time data                                             | MW        | 3 min      |
|  178 | Temperature in Helsinki - real time data                                                 | °C        | 3 min      |
|  182 | Temperature in Jyväskylä - real time data                                                | °C        | 3 min      |
|  196 | Temperature in Oulu - real time data                                                     | °C        | 3 min      |
|  185 | Temperature in Rovaniemi - real time data                                                | °C        | 3 min      |
|   96 | The buying price of production imbalance electricity                                     | €/MWh     | 1 h        |
|   92 | The price of comsumption imbalance electricity                                           | €/MWh     | 1 h        |
|   93 | The sales price of production imbalance electricity                                      | €/MWh     | 1 h        |
|  105 | The sum of the down-regualtion bids in the Balancing energy market                       | MW        | 1 h        |
|  243 | The sum of the up-regulation bids in the balancing energy market                         | MW        | 1 h        |
|  206 | Time deviation - real time data                                                          | s         | 3 min      |
|  267 | Total production capacity used in the solar power forecast                               | MW        | 1 h        |
|  268 | Total production capacity used in the wind power forecast                                | MW        | 1 h        |
|   89 | Transmission between Finland and Central Sweden - real time data                         | MW        | 3 min      |
|   87 | Transmission between Finland and Northern Sweden - real time data                        | MW        | 3 min      |
|  187 | Transmission between Finland and Norway - real time data                                 | MW        | 3 min      |
|  195 | Transmission between Finland and Russia - real time data                                 | MW        | 3 min      |
|   90 | Transmission between Sweden and Åland - real time data                                   | MW        | 3 min      |
|  103 | Transmission capacity FI-RUS                                                             | MW        | 1 h        |
|   63 | Transmission capacity RUS-FI                                                             | MW        | 1 h        |
|  280 | Transmission of electricity between Finland and Åland - measured hourly data             | MWh/h     | 1 h        |
|   61 | Transmission of electricity between Finland and Central Sweden - measured hourly data    | MW        | 1 h        |
|   55 | Transmission of electricity between Finland and Estonia - measured hourly data           | MWh/h     | 1 h        |
|   60 | Transmission of electricity between Finland and Northern Sweden - measured hourly data   | MWh/h     | 1 h        |
|   57 | Transmission of electricity between Finland and Norway - measured hourly data            | MWh/h     | 1 h        |
|   58 | Transmission of electricity between Finland and Russia - measured hourly data            | MWh/h     | 1 h        |
|  244 | Up-regulating price in the Balancing energy market                                       | €/MWh     | 1 h        |
|   75 | Wind power generation - hourly data                                                      | MWh/h     | 1 h        |
|  245 | Wind power generation forecast - updated hourly                                          | MWh/h     | 1 h        |
|  246 | Wind power generation forecast - updated once a day                                      | MWh/h     | 1 h        |
|  181 | Wind power production - real time data                                                   | MW        | 3 min      |
