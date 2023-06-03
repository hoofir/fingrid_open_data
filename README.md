# Fingrid Open Datasets via API
Fingrid's open data platform provides machine readable access to datasets through open **REST API** interface.


## Registration
Fingrid provides equal service for all users of the open data platform through the free of charge API-access which requires registration.

1. Make sure you have an active email address.
2. Do [register](https://data.fingrid.fi/open-data-forms/registration/) and approve the license and terms of use. 
3. You will receive a personal API-key right away. If you don't receive the email, please check your Junk Mail folder.
4. Registered users may opt-in to receive email maintenance breaks or other important changes about API.
5. If you want, you can also [delete your account](https://data.fingrid.fi/open-data-forms/leave/) and the related API-key.


## How to use the API
Technical API documentation for developers:  http://data.fingrid.fi/open-data-api/

- API requests to this endpoint:  https://api.fingrid.fi/
- For an individual variable, you can get the latest event or events from a specified date/time range. For a set of variables, you can get the latest events.
- You can access data in JSON, XML or CSV formats.
- You can make [custom searches](https://data.fingrid.fi/open-data-forms/search/en/) for each dataset. Each dataset has an unique link to the search interface. 
- Each dataset has a unique `VariableId` number that you need to use in API requests. See them all in [here](https://github.com/hoofir/fingrid_open_data/raw/main/Avoin%2Bdata%2Btietoaineistoluettelo%2B9.6.2021.xlsx). 
- API-key must be inserted to the http-request header `x-api-key`, not into the URL-address. If you are importing data from the API into an application, it is usually possible to insert the API-key by modifying the request header parameters in your application.
- You can make 10,000 requests in 24h period with one API-key. Please contact the [administrator](mailto:avoindata@fingrid.fi) if you need to make more requests.
- Data timestamps are presented in `UTC` (previously as GMT) time format. Correct format for API requests is `YYYY-MM-ddTHH:mm:ssZ` e.g. 2023-04-02T00:00:00+00:00
- Data update frequency varies by dataset: many datasets have data that is updated hourly, and some datasets include data that is updated in 3 or 5 minute intervals. The update frequency is stated in the dataset description.
- If you request frequently updated data from an extended date range, you may receive an error message that results from exceeding the maximum allowed API payload. Shorten the date range and request the results in JSON-format. 
- If you use the API in browser environment, you need to note the requirements and limitations for Cross Origin Resource Sharing ([CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS)). 


## Availability and uptime
The open data API is not guaranteed to have 100% uptime. Although maximum uptime is a goal, as with any service disruptions can happen at any point along the networks and Internet between the client application and the API servers. Make your application defensive that can handle API downtime gracefully. One such way could be by implementing good caching. Another strategy could be to aim for graceful failure if the API is not available. 


## Data List

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>NIMI</th>
      <th>NAME</th>
      <th>YKSIKKÖ</th>
      <th>AIKAVÄLI</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>252.0</td>
      <td>Aktivoitu alassäätöteho</td>
      <td>Activated down-regulation power</td>
      <td>MW</td>
      <td>15 min</td>
      <td>https://data.fingrid.fi/dataset/aktivoitu-alassaatoteho</td>
    </tr>
    <tr>
      <th>1</th>
      <td>253.0</td>
      <td>Aktivoitu ylössäätöteho</td>
      <td>Activated up-regulation power</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/aktivoitu-ylossaatoteho</td>
    </tr>
    <tr>
      <th>2</th>
      <td>53.0</td>
      <td>Automaattinen taajuudenhallintareservi, aktivoitu, alas</td>
      <td>Automatic Frequency Restoration Reserve, activated, down</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/activated-automatic-frequency-restoration-reserve-down</td>
    </tr>
    <tr>
      <th>3</th>
      <td>54.0</td>
      <td>Automaattinen taajuudenhallintareservi, aktivoitu, ylös</td>
      <td>Automatic Frequency Restoration Reserve, activated, up</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/activated-automatic-frequency-restoration-reserve-up</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.0</td>
      <td>Automaattinen taajuudenhallintareservi, alassäätökapasiteetti</td>
      <td>Automatic Frequency Restoration Reserve, capacity, down</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/procured-automatic-frequency-restoration-reserve-capacity-down</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.0</td>
      <td>Automaattinen taajuudenhallintareservi, ylössäätökapasiteetti</td>
      <td>Automatic Frequency Restoration Reserve, capacity, up</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/procured-automatic-frequency-restoration-reserve-capacity-up</td>
    </tr>
    <tr>
      <th>6</th>
      <td>51.0</td>
      <td>Automaattinen taajuudenhallintareservi, alassäätökapasiteetin hinta</td>
      <td>Automatic Frequency Restoration Reserve, price, down</td>
      <td>€/MWh</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/procured-afrr-capacity-price-down</td>
    </tr>
    <tr>
      <th>7</th>
      <td>52.0</td>
      <td>Automaattinen taajuudenhallintareservi, ylössäätökapasiteetin hinta</td>
      <td>Automatic Frequency Restoration Reserve, price, up</td>
      <td>€/MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/procured-a-frr-capacity-price-up</td>
    </tr>
    <tr>
      <th>8</th>
      <td>270.0</td>
      <td>Säätökapasiteettimarkkinat, tarjoukset</td>
      <td>Balancing Capacity Market bids</td>
      <td>MW</td>
      <td>1 wk</td>
      <td>https://data.fingrid.fi/dataset/saatokapasiteettimarkkinat-tarjoukset</td>
    </tr>
    <tr>
      <th>9</th>
      <td>262.0</td>
      <td>Säätökapasiteettimarkkinat, marginaalihinta</td>
      <td>Balancing Capacity Market price</td>
      <td>€</td>
      <td>1 wk</td>
      <td>https://data.fingrid.fi/dataset/saatokapasiteettimarkkinat-hinta</td>
    </tr>
    <tr>
      <th>10</th>
      <td>261.0</td>
      <td>Säätökapasiteettimarkkinat, toteutunut hankinta</td>
      <td>Balancing Capacity Market results</td>
      <td>MW</td>
      <td>1 wk</td>
      <td>https://data.fingrid.fi/dataset/saatokapasiteettimarkkinat-toteutunut-hankinta</td>
    </tr>
    <tr>
      <th>11</th>
      <td>68.0</td>
      <td>Bilateraalikaupat välillä FI-RUS</td>
      <td>Bilateral trade between FI-RUS</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/bilateral-trade-between-finland-and-russia</td>
    </tr>
    <tr>
      <th>12</th>
      <td>101.0</td>
      <td>Bilateraalikaupan kapasiteetti FI-RUS</td>
      <td>Bilateral trade capacity FI-RUS</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/bilateral-trade-capacity-fi-rus</td>
    </tr>
    <tr>
      <th>13</th>
      <td>49.0</td>
      <td>Bilateraalikaupan käyttämätön kapasiteetti FI-RUS</td>
      <td>Bilateral trade capacity FI-RUS, unused</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/unused-bilateral-trade-capacity-fi-rus</td>
    </tr>
    <tr>
      <th>14</th>
      <td>65.0</td>
      <td>Bilateraalikaupan kapasiteetti RUS-FI</td>
      <td>Bilateral trade capacity RUS-FI</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/bilateral-trade-capacity-rus-fi</td>
    </tr>
    <tr>
      <th>15</th>
      <td>64.0</td>
      <td>Bilateraalikaupan käyttämätön kapasiteetti RUS-FI</td>
      <td>Bilateral trade capacity RUS-FI, unused</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/unused-bilateral-trade-capacity-rus-fi</td>
    </tr>
    <tr>
      <th>16</th>
      <td>201.0</td>
      <td>Kaukolämmön yhteistuotanto - reaaliaikatieto</td>
      <td>Cogeneration of district heating - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/cogeneration</td>
    </tr>
    <tr>
      <th>17</th>
      <td>140.0</td>
      <td>Kaupallinen siirto välillä FI-EE</td>
      <td>Commercial transmission of electricity between FI-EE</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/commercial-flow-fi-ee</td>
    </tr>
    <tr>
      <th>18</th>
      <td>31.0</td>
      <td>Kaupallinen siirto välillä FI-SE1</td>
      <td>Commercial transmission of electricity between FI-SE1</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/commercial-flow-fi-se1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>32.0</td>
      <td>Kaupallinen siirto välillä FI-SE3</td>
      <td>Commercial transmission of electricity between FI-SE3</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/commercial-flow-fi-se3</td>
    </tr>
    <tr>
      <th>20</th>
      <td>189.0</td>
      <td>Lauhdevoimatuotanto - reaaliaikatieto</td>
      <td>Condensing power production - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/condensing-power-production-real-time-data</td>
    </tr>
    <tr>
      <th>21</th>
      <td>48.0</td>
      <td>Pullonkaulatulot välillä FI-EE</td>
      <td>Congestion income between FI-EE</td>
      <td>€</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/congestion-income-between-finland-and-estonia</td>
    </tr>
    <tr>
      <th>22</th>
      <td>70.0</td>
      <td>Pullonkaulatulot välillä FI-SE1</td>
      <td>Congestion income between FI-SE1</td>
      <td>€</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/congestion-income-between-fi-se1</td>
    </tr>
    <tr>
      <th>23</th>
      <td>71.0</td>
      <td>Pullonkaulatulot välillä FI-SE3</td>
      <td>Congestion income between FI-SE3</td>
      <td>€</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/congestion-income-between-fi-se3</td>
    </tr>
    <tr>
      <th>24</th>
      <td>86.0</td>
      <td>Rajasiirtohinta, vienti Venäjälle</td>
      <td>Cross-border transmission fee, export to Russia</td>
      <td>€/MWh</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/cross-border-transmission-fee-export-to-russia</td>
    </tr>
    <tr>
      <th>25</th>
      <td>85.0</td>
      <td>Rajasiirtohinta, tuonti Venäjältä</td>
      <td>Cross-border transmission fee, import from Russia</td>
      <td>€/MWh</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/cross-border-transmission-fee-import-from-russia</td>
    </tr>
    <tr>
      <th>26</th>
      <td>112.0</td>
      <td>Vuorokausimarkkinoiden siirtokapasiteetti EE-FI – virallinen</td>
      <td>Day-ahead transmission capacity EE-FI – official</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/intra-day-transmission-capacity-ee-fi</td>
    </tr>
    <tr>
      <th>27</th>
      <td>115.0</td>
      <td>Vuorokausimarkkinoiden siirtokapasiteetti FI-EE – virallinen</td>
      <td>Day-ahead transmission capacity FI-EE – official</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/indra-day-transmission-capacity-fi-ee</td>
    </tr>
    <tr>
      <th>28</th>
      <td>26.0</td>
      <td>Vuorokausimarkkinoiden siirtokapasiteetti FI-SE1 – virallinen</td>
      <td>Day-ahead transmission capacity FI-SE1 – official</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/vuorokausimarkkinoille-annettu-siirtokapasiteetti-fi-se1</td>
    </tr>
    <tr>
      <th>29</th>
      <td>143.0</td>
      <td>Vuorokausimarkkinoiden siirtokapasiteetti FI-SE1 – suunniteltu</td>
      <td>Day-ahead transmission capacity FI-SE1 – planned</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/planned-transmission-capacity-fi-se1</td>
    </tr>
    <tr>
      <th>30</th>
      <td>27.0</td>
      <td>Vuorokausimarkkinoiden siirtokapasiteetti FI-SE3 – virallinen</td>
      <td>Day-ahead transmission capacity FI-SE3 – official</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/vuorokausimarkkinoille-annettu-siirtokapasiteetti-fi-se3</td>
    </tr>
    <tr>
      <th>31</th>
      <td>145.0</td>
      <td>Vuorokausimarkkinoiden siirtokapasiteetti FI-SE3 – suunniteltu</td>
      <td>Day-ahead transmission capacity FI-SE3 – planned</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/suunniteltu-vuorokausimarkkinoille-annettava-siirtokapasiteetti-fi-se3</td>
    </tr>
    <tr>
      <th>32</th>
      <td>24.0</td>
      <td>Vuorokausimarkkinoiden siirtokapasiteetti SE1-FI – virallinen</td>
      <td>Day-ahead transmission capacity SE1-FI – official</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/intra-day-transmission-capacity-se1-fi</td>
    </tr>
    <tr>
      <th>33</th>
      <td>142.0</td>
      <td>Vuorokausimarkkinoiden siirtokapasiteetti SE1-FI – suunniteltu</td>
      <td>Day-ahead transmission capacity SE1-FI – planned</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/planned-transmission-capacity-se1-fi</td>
    </tr>
    <tr>
      <th>34</th>
      <td>144.0</td>
      <td>Vuorokausimarkkinoiden siirtokapasiteetti SE3-FI  – suunniteltu</td>
      <td>Day-ahead transmission capacity SE3-FI  – planned</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/planned-day-ahead-transmission-capacity-se3-fi</td>
    </tr>
    <tr>
      <th>35</th>
      <td>25.0</td>
      <td>Vuorokausimarkkinoiden siirtokapasiteetti SE3-FI – virallinen</td>
      <td>Day-ahead transmission capacity SE3-FI – official</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/vuorokausimarkkinoille-annettu-siirtokapasiteetti-se3-fi</td>
    </tr>
    <tr>
      <th>36</th>
      <td>251.0</td>
      <td>Alassäätötarjoukset, viimeksi aktivoidun tarjouksen hinta - reaaliaikatieto</td>
      <td>Down-regulation bids, price of the last activated - real time data</td>
      <td>€/MWh</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/viimeksi-aktivoidun-alassaatotarjouksen-hinta-reaaliaikainen-julkaisu</td>
    </tr>
    <tr>
      <th>37</th>
      <td>106.0</td>
      <td>Alassäätöhinta säätösähkömarkkinoilla</td>
      <td>Down-regulation price in the Balancing energy market</td>
      <td>€/MWh</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/down-regulation-price-in-the-balancing-energy-market</td>
    </tr>
    <tr>
      <th>38</th>
      <td>165.0</td>
      <td>Kulutusennuste - seuraava vuorokausi</td>
      <td>Electricity consumption forecast - next 24 hours</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/an-hourly-comsumption-forecast-for-the-next-24-hours</td>
    </tr>
    <tr>
      <th>39</th>
      <td>166.0</td>
      <td>Kulutusennuste - päivittyvä tuntienergiatieto</td>
      <td>Electricity consumption forecast - updated hourly</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/updated-electricity-consumption-forecast-of-finland</td>
    </tr>
    <tr>
      <th>40</th>
      <td>124.0</td>
      <td>Sähkönkulutus Suomessa</td>
      <td>Electricity consumption in Finland</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/electricity-consumption-in-finland</td>
    </tr>
    <tr>
      <th>41</th>
      <td>193.0</td>
      <td>Sähkönkulutus Suomesa - reaaliaikatieto</td>
      <td>Electricity consumption in Finland - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/electricity-consumption-in-finland-real-time-data</td>
    </tr>
    <tr>
      <th>42</th>
      <td>74.0</td>
      <td>Sähköntuotanto Suomessa</td>
      <td>Electricity production in Finland</td>
      <td>MWh/h</td>
      <td>1h</td>
      <td>https://data.fingrid.fi/dataset/electricity-production-in-finland</td>
    </tr>
    <tr>
      <th>43</th>
      <td>192.0</td>
      <td>Sähköntuotanto Suomessa - reaaliaikatieto</td>
      <td>Electricity production in Finland - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/electricity-production-in-finland-real-time-data</td>
    </tr>
    <tr>
      <th>44</th>
      <td>242.0</td>
      <td>Sähköntuotantoennuste - alustava tuntienergiatieto</td>
      <td>Electricity production prediction - premilinary</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/tentative-production-prediction-for-the-next-24-hours-as-an-hourly-energy</td>
    </tr>
    <tr>
      <th>45</th>
      <td>241.0</td>
      <td>Sähköntuotantoennuste - päivittyvä tuntienergiatieto</td>
      <td>Electricity production prediction - updated hourly</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/finland-electricity-production-prediction-based-on-production-plans-informed-to-fingrid</td>
    </tr>
    <tr>
      <th>46</th>
      <td>205.0</td>
      <td>Sähköntuotanto, varavoimalaitokset ja pientuotanto - reaaliaikatieto</td>
      <td>Electricity production, reserve power plants and small-scale production - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/gas-turbine-and-estimated-small-scale-production-real-time-data</td>
    </tr>
    <tr>
      <th>47</th>
      <td>198.0</td>
      <td>Sähköntuotanto, yli/alijäämä - reaaliaikatieto</td>
      <td>Electricity production, surplus/deficit - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/production-surplus-deficit-in-finland-real-time-data</td>
    </tr>
    <tr>
      <th>48</th>
      <td>265.0</td>
      <td>Suomessa kulutetun sähkön päästökerroin - reaaliaikatieto</td>
      <td>Emission factor for electricity consumed in Finland - real time data</td>
      <td>gCO2/kWh</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/suomessa-kulutetun-sahkon-paastokerroin-reaaliaikatieto</td>
    </tr>
    <tr>
      <th>49</th>
      <td>266.0</td>
      <td>Suomen sähköntuotannon päästökerroin - reaaliaikatieto</td>
      <td>Emission factor of electricity production in Finland - real time data</td>
      <td>gCO2/kWh</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/suomen-sahkontuotannon-paastokerroin-reaaliaikatieto</td>
    </tr>
    <tr>
      <th>50</th>
      <td>277.0</td>
      <td>Nopea taajuusreservi FFR, hinta</td>
      <td>Fast Frequency Reserve FFR, price</td>
      <td>€/MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/nopea-taajuusreservi-hinta</td>
    </tr>
    <tr>
      <th>51</th>
      <td>276.0</td>
      <td>Nopea taajuusreservi FFR, hankintamäärä</td>
      <td>Fast Frequency Reserve FFR, procured volume</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/nopea-taajuusreservi-hankintamaara</td>
    </tr>
    <tr>
      <th>52</th>
      <td>278.0</td>
      <td>Nopea taajuusreservi FFR, hankintaennuste</td>
      <td>Fast Frequency Reserve FFR, procurement forecast</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/nopea-taajuusreservi-hankintaennuste</td>
    </tr>
    <tr>
      <th>53</th>
      <td>275.0</td>
      <td>Nopea taajuusreservi FFR, tarjousmäärä</td>
      <td>Fast Frequency Reserve FFR, received bids</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/nopea-taajuusreservi-tarjoukset</td>
    </tr>
    <tr>
      <th>54</th>
      <td>NaN</td>
      <td>Taajuus - historiatieto</td>
      <td>Frequency - historical data</td>
      <td>Hz</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/fi/dataset/frequency-historical-data</td>
    </tr>
    <tr>
      <th>55</th>
      <td>177.0</td>
      <td>Taajuus - reaaliaikatieto</td>
      <td>Frequency - real time data</td>
      <td>Hz</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/frequency-real-time-data</td>
    </tr>
    <tr>
      <th>56</th>
      <td>82.0</td>
      <td>Taajuusohjattu häiriöreservi, hankintamäärät tuntimarkkinoilta</td>
      <td>Frequency containment reserve for disturbances, procured volumes in hourly market</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/frequency-containment-reserve-for-disturbances-procured-volumes-in-hourly-market</td>
    </tr>
    <tr>
      <th>57</th>
      <td>286.0</td>
      <td>Taajuusohjattu häiriöreservi, tarjousmäärät tuntimarkkinoilta</td>
      <td>Frequency containment reserve for disturbances, received bids in hourly market</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/fi/dataset/taajuusohjattu-hairioreservi-tarjousmaarat-tuntimarkkinoilta</td>
    </tr>
    <tr>
      <th>58</th>
      <td>123.0</td>
      <td>Taajuusohjattu käyttöreservi, aktivoitunut</td>
      <td>Frequency Containment Reserve for Normal operation, activated</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/activated-frequency-containment-reserve-for-normal-operation</td>
    </tr>
    <tr>
      <th>59</th>
      <td>287.0</td>
      <td>Taajuusohjattu käyttöreservi, ulkomaankauppa</td>
      <td>Frequency Containment Reserve for Normal operation, foreign trade</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/taajuusohjattu-kayttoreservi-ulkomaankauppa</td>
    </tr>
    <tr>
      <th>60</th>
      <td>285.0</td>
      <td>Taajuusohjattu käyttöreservi, tarjousmäärät tuntimarkkinoilta</td>
      <td>Frequency Containment Reserve for Normal operation, hourly market bids</td>
      <td>MW</td>
      <td>1h</td>
      <td>https://data.fingrid.fi/dataset/taajuusohjattu-kayttoreservi-tarjousmaarat-tuntimarkkinoilta</td>
    </tr>
    <tr>
      <th>61</th>
      <td>79.0</td>
      <td>Taajuusohjattu käyttöreservi, tuntimarkkinahinnat</td>
      <td>Frequency Containment Reserve for Normal operation, hourly market prices</td>
      <td>€/MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/frequency-containment-reserve-for-normal-operation-prices</td>
    </tr>
    <tr>
      <th>62</th>
      <td>80.0</td>
      <td>Taajuusohjattu käyttöreservi, hankintamäärät tuntimarkkinoilta</td>
      <td>Frequency Containment Reserve for Normal operation, hourly market volumes</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/frequency-containment-reserves-for-normal-operation-procured-volumes-in-hourly-market</td>
    </tr>
    <tr>
      <th>63</th>
      <td>288.0</td>
      <td>Taajuusohjattu käyttöreservi, vuosimarkkinasuunnitelmat</td>
      <td>Frequency Containment Reserve for Normal operation, yearly market plans</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/taajuusohjattu-kayttoreservi-vuosimarkkinasuunnitelmat</td>
    </tr>
    <tr>
      <th>64</th>
      <td>81.0</td>
      <td>Taajuusohjattu häiriöreservi, tuntimarkkinahinnat</td>
      <td>Frequency containment reserves for disturbances, hourly market prices</td>
      <td>€/MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/frequency-containment-reserves-for-disturbances-hourly-market-prices</td>
    </tr>
    <tr>
      <th>65</th>
      <td>289.0</td>
      <td>Taajuusohjattu häiriöreservi, ulkomaankauppa</td>
      <td>Frequency containment reserves for disturbances, nordic trade</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/fi/dataset/taajuusohjattu-hairioreservi-ulkomaankauppa</td>
    </tr>
    <tr>
      <th>66</th>
      <td>290.0</td>
      <td>Taajuusohjattu häiriöreservi, vuosimarkkinasuunnitelmat</td>
      <td>Frequency containment reserves for disturbances, reserve plans in the yearly market</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/fi/dataset/taajuusohjattu-hairioreservi-vuosimarkkinasuunnitelmat</td>
    </tr>
    <tr>
      <th>67</th>
      <td>239.0</td>
      <td>Tunninvaihdesäätö, alassäätö</td>
      <td>Hour change regulation, down-regulation</td>
      <td>MWh/h (?)</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/tunninvaihdesaato-alassaato</td>
    </tr>
    <tr>
      <th>68</th>
      <td>240.0</td>
      <td>Tunninvaihdesäätö, ylössäätö</td>
      <td>Hour change regulation, up-regulation</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/hour-change-regulation-up-regulation</td>
    </tr>
    <tr>
      <th>69</th>
      <td>191.0</td>
      <td>Vesivoimatuotanto - reaaliaikatieto</td>
      <td>Hydro power production - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/hydro-power-production-real-time-data</td>
    </tr>
    <tr>
      <th>70</th>
      <td>176.0</td>
      <td>Suomen ja Ruotsin välinen tasesähkön määrä</td>
      <td>Imbalance power between Finland and Sweden</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/imbalance-power-between-finland-and-sweden</td>
    </tr>
    <tr>
      <th>71</th>
      <td>202.0</td>
      <td>Teollisuuden yhteistuotanto - reaaliaikatieto</td>
      <td>Industrial cogeneration - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/industrial-cogeneration-real-time-data</td>
    </tr>
    <tr>
      <th>72</th>
      <td>110.0</td>
      <td>Päivän sisäisten markkinoiden siirtokapasiteetti EE-FI</td>
      <td>Intraday transmission capacity EE-FI</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/transmission-capacity-to-be-given-to-intraday-market-ee-fi</td>
    </tr>
    <tr>
      <th>73</th>
      <td>111.0</td>
      <td>Päivän sisäisten markkinoiden siirtokapasiteetti EE-FI – reaaliaikatieto</td>
      <td>Intraday transmission capacity EE-FI – real time data</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/real-time-transmission-capacity-to-be-given-to-intraday-market-ee-fi</td>
    </tr>
    <tr>
      <th>74</th>
      <td>113.0</td>
      <td>Päivän sisäisten markkinoiden siirtokapasiteetti FI-EE</td>
      <td>Intraday transmission capacity FI-EE</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/intraday-markkinoille-annettu-siirtokapasiteetti-ee-fi</td>
    </tr>
    <tr>
      <th>75</th>
      <td>114.0</td>
      <td>Päivän sisäisten markkinoiden siirtokapasiteetti FI-EE – reaaliaikatieto</td>
      <td>Intraday transmission capacity FI-EE – real time data</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/real-time-transmission-capacity-to-be-given-to-intraday-market-fi-ee</td>
    </tr>
    <tr>
      <th>76</th>
      <td>50.0</td>
      <td>Päivän sisäisten markkinoiden siirtokapasiteetti FI-RUS</td>
      <td>Intraday transmission capacity FI-RUS</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/intraday-transmission-capacity-fi-rus</td>
    </tr>
    <tr>
      <th>77</th>
      <td>44.0</td>
      <td>Päivän sisäisten markkinoiden siirtokapasiteetti FI-SE1</td>
      <td>Intraday transmission capacity FI-SE1</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/transmission-capacity-to-be-given-to-intraday-market-fi-se1</td>
    </tr>
    <tr>
      <th>78</th>
      <td>45.0</td>
      <td>Päivän sisäisten markkinoiden siirtokapasiteetti FI-SE3</td>
      <td>Intraday transmission capacity FI-SE3</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/transmission-capacity-to-be-given-to-intraday-market-fi-se3</td>
    </tr>
    <tr>
      <th>79</th>
      <td>66.0</td>
      <td>Päivän sisäisten markkinoiden siirtokapasiteetti RUS-FI</td>
      <td>Intraday transmission capacity RUS-FI</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/intraday-transmission-capacity-rus-fi</td>
    </tr>
    <tr>
      <th>80</th>
      <td>38.0</td>
      <td>Päivän sisäisten markkinoiden siirtokapasiteetti SE1-FI</td>
      <td>Intraday transmission capacity SE1-FI</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/transmission-capacity-to-be-given-to-intraday-market-se1-fi</td>
    </tr>
    <tr>
      <th>81</th>
      <td>39.0</td>
      <td>Päivän sisäisten markkinoiden siirtokapasiteetti SE3-FI</td>
      <td>Intraday transmission capacity SE3-FI</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/transmission-capacity-to-be-given-to-intraday-market-se3-fi</td>
    </tr>
    <tr>
      <th>82</th>
      <td>260.0</td>
      <td>Pohjoismaisen sähköjärjestelmän liike-energia - reaaliaikatieto</td>
      <td>Kinetic energy of the Nordic power system - real time data</td>
      <td>GWs</td>
      <td>1 min</td>
      <td>https://data.fingrid.fi/dataset/kinetic-energy-nordic-realtime</td>
    </tr>
    <tr>
      <th>83</th>
      <td>30.0</td>
      <td>Mitattu P1 siirto Suomen pohjois-eteläsuuntaisessa leikkauksessa</td>
      <td>Measured transmission of electricity in Finland from north to south</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/measured-electricity-energy-in-finland-from-north-to-south</td>
    </tr>
    <tr>
      <th>84</th>
      <td>194.0</td>
      <td>Sähkön nettotuonti/-vienti - reaaliaikatieto</td>
      <td>Net import/export of electricity - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/net-import-export-of-electricity-real-time-data</td>
    </tr>
    <tr>
      <th>85</th>
      <td>188.0</td>
      <td>Ydinvoimatuotanto - reaaliaikatieto</td>
      <td>Nuclear power production - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/nuclear-power-production-real-time-data</td>
    </tr>
    <tr>
      <th>86</th>
      <td>33.0</td>
      <td>Tilattu alassäätö Suomen säätösähkömarkkinoilta</td>
      <td>Ordered down-regulations from Balancing energy market in Finland</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/ordered-down-regulations-from-balancing-market-in-finland</td>
    </tr>
    <tr>
      <th>87</th>
      <td>34.0</td>
      <td>Tilattu ylössäätö Suomen säätösähkömarkkinoilta</td>
      <td>Ordered up-regulations from Balancing energy market in Finland</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/ordered-up-regulations-from-balancing-energy-market-in-finland</td>
    </tr>
    <tr>
      <th>88</th>
      <td>213.0</td>
      <td>Muut tehokaupat, alassäätö</td>
      <td>Other power transactions, down-regulation</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/other-power-transactions-down-regulation</td>
    </tr>
    <tr>
      <th>89</th>
      <td>214.0</td>
      <td>Muut tehokaupat, ylössäätö</td>
      <td>Other power transactions, up-regulation</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/other-power-transactions-up-regulation</td>
    </tr>
    <tr>
      <th>90</th>
      <td>183.0</td>
      <td>Tehoreservi - reaaliaikatieto</td>
      <td>Peak load power - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/peak-load-power-real-time-data</td>
    </tr>
    <tr>
      <th>91</th>
      <td>41.0</td>
      <td>Suunniteltu siirtokapasiteetti FI-RUS</td>
      <td>Planned transmission capacity FI-RUS</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/planned-transmission-capacity-fi-rus</td>
    </tr>
    <tr>
      <th>92</th>
      <td>127.0</td>
      <td>Suunniteltu siirtokapasiteetti RUS-FI</td>
      <td>Planned transmission capacity RUS-FI</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/planned-transmission-capacity-rus-fi</td>
    </tr>
    <tr>
      <th>93</th>
      <td>28.0</td>
      <td>Suunniteltu viikkokapasiteetti P1-leikkauksessa pohjoisesta etelään</td>
      <td>Planned weekly capacity from north to south</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/planned-weekly-capacity-from-north-to-south-defined-by-fingrid</td>
    </tr>
    <tr>
      <th>94</th>
      <td>29.0</td>
      <td>Suunniteltu viikkokapasiteetti P1-leikkauksessa etelästä pohjoiseen</td>
      <td>Planned weekly capacity from south to north</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/planned-weekly-capacity-from-south-to-north-defined-by-fingrid</td>
    </tr>
    <tr>
      <th>95</th>
      <td>209.0</td>
      <td>Sähköjärjestelmän käyttötilanne - reaaliaikatieto</td>
      <td>Power system state - real time data</td>
      <td>"1"</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/power-system-state-real-time-data</td>
    </tr>
    <tr>
      <th>96</th>
      <td>22.0</td>
      <td>Viimeksi aktivoidun ylössäätötarjouksen hinta - reaaliaikatieto</td>
      <td>Price of the last activated up-regulation bid - real time data</td>
      <td>€/MWh</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/real-time-price-of-up-regulation</td>
    </tr>
    <tr>
      <th>97</th>
      <td>180.0</td>
      <td>Sähkönsiirto Suomen ja Viron välillä - reaaliaikatieto</td>
      <td>Sähkönsiirto Suomen ja Viron välillä - reaaliaikatieto</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/transmission-between-finland-and-estonia-real-time-data</td>
    </tr>
    <tr>
      <th>98</th>
      <td>248.0</td>
      <td>Aurinkovoiman tuotantoennuste - päivitys tunneittain</td>
      <td>Solar power generation forecast - updated hourly</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/solar-power-generation-forecast-updated-every-hour</td>
    </tr>
    <tr>
      <th>99</th>
      <td>247.0</td>
      <td>Aurinkovoiman tuotantoennuste - päivitys kerran vuorokaudessa</td>
      <td>Solar power generation forecast - updated once a day</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/solar-power-generation-forecast-updated-once-a-day</td>
    </tr>
    <tr>
      <th>100</th>
      <td>118.0</td>
      <td>Erikoissäätö, alassäätö</td>
      <td>Special regulation, down-regulation</td>
      <td>NaN</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/erikoissaato-alassaato</td>
    </tr>
    <tr>
      <th>101</th>
      <td>119.0</td>
      <td>Erikoissäätö, ylössäätö</td>
      <td>Special regulation, up-regulation</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/special-regulation-up-regulation</td>
    </tr>
    <tr>
      <th>102</th>
      <td>102.0</td>
      <td>Pörssikaupat, siirtokapasiteetti FI-RUS</td>
      <td>Stock exchange capacity FI-RUS</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/stock-exchange-capacity-fi-rus</td>
    </tr>
    <tr>
      <th>103</th>
      <td>67.0</td>
      <td>Pörssikaupat, siirtokapasiteetti RUS-FI</td>
      <td>Stock exchange capacity RUS-FI</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/stock-exchange-capacity-rus-fi</td>
    </tr>
    <tr>
      <th>104</th>
      <td>69.0</td>
      <td>Pörssikaupat FI-RUS-FI</td>
      <td>Stock exchange trade FI-RUS-FI</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/stock-exchange-between-finland-and-russia</td>
    </tr>
    <tr>
      <th>105</th>
      <td>186.0</td>
      <td>Tuotantoyli/alijäämä kumulatiivinen - reaaliaikatieto</td>
      <td>Surplus/deficit, cumulative - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/surplus-deficit-cumulative-real-time-data</td>
    </tr>
    <tr>
      <th>106</th>
      <td>178.0</td>
      <td>Lämpötila Helsingissä - reaaliaikatieto</td>
      <td>Temperature in Helsinki - real time data</td>
      <td>°C</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/temperature-in-helsinki-real-time-data</td>
    </tr>
    <tr>
      <th>107</th>
      <td>182.0</td>
      <td>Lämpötila Jyväskylässä - reaaliaikatieto</td>
      <td>Temperature in Jyväskylä - real time data</td>
      <td>°C</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/temperature-in-jyvaskyla-real-time-data</td>
    </tr>
    <tr>
      <th>108</th>
      <td>196.0</td>
      <td>Lämpötila Oulussa - reaaliaikatieto</td>
      <td>Temperature in Oulu - real time data</td>
      <td>°C</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/temperature-in-oulu-real-time-data</td>
    </tr>
    <tr>
      <th>109</th>
      <td>185.0</td>
      <td>Lämpötila Rovaniemellä - reaaliaikatieto</td>
      <td>Temperature in Rovaniemi - real time data</td>
      <td>°C</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/temperature-in-rovaniemi-real-time-data</td>
    </tr>
    <tr>
      <th>110</th>
      <td>96.0</td>
      <td>Tuotantotasesähkön ostohinta</td>
      <td>The buying price of production imbalance electricity</td>
      <td>€/MWh</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/the-bying-price-of-production-imbalance-electricity</td>
    </tr>
    <tr>
      <th>111</th>
      <td>92.0</td>
      <td>Kulutustasesähkön hinta</td>
      <td>The price of comsumption imbalance electricity</td>
      <td>€/MWh</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/the-price-of-comsumption-imbalance-electricity</td>
    </tr>
    <tr>
      <th>112</th>
      <td>93.0</td>
      <td>Tuotantotasesähkön myyntihinta</td>
      <td>The sales price of production imbalance electricity</td>
      <td>€/MWh</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/the-sales-price-of-production-imbalance-electricity</td>
    </tr>
    <tr>
      <th>113</th>
      <td>105.0</td>
      <td>Alassäätötarjouksien summa säätösähkömarkkinoilla</td>
      <td>The sum of the down-regualtion bids in the Balancing energy market</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/the-sum-of-the-down-regualtion-bids-in-the-balancing-energy-market</td>
    </tr>
    <tr>
      <th>114</th>
      <td>243.0</td>
      <td>Ylössäätötarjouksien summa säätösähkömarkkinoilla</td>
      <td>The sum of the up-regulation bids in the balancing energy market</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/the-sum-of-the-up-regulation-bids-in-the-balancing-energy-market</td>
    </tr>
    <tr>
      <th>115</th>
      <td>206.0</td>
      <td>Aikapoikkeama - reaaliaikatieto</td>
      <td>Time deviation - real time data</td>
      <td>s</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/time-deviation-real-time-data</td>
    </tr>
    <tr>
      <th>116</th>
      <td>267.0</td>
      <td>Aurinkovoimaennusteessa käytetty kokonaiskapasiteetti</td>
      <td>Total production capacity used in the solar power forecast</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/total-solar-production-capacity</td>
    </tr>
    <tr>
      <th>117</th>
      <td>268.0</td>
      <td>Tuulivoimaennusteessa käytetty kokonaiskapasiteetti</td>
      <td>Total production capacity used in the wind power forecast</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/total-wind-production-capacity</td>
    </tr>
    <tr>
      <th>118</th>
      <td>89.0</td>
      <td>Sähkönsiirto Suomen ja Keski-Ruotsin välillä - reaaliaikatieto</td>
      <td>Transmission between Finland and Central Sweden - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/transmission-between-finland-and-central-sweden-real-time-data</td>
    </tr>
    <tr>
      <th>119</th>
      <td>87.0</td>
      <td>Sähkönsiirto Suomen ja Pohjois-Ruotsin välillä - reaaliaikatieto</td>
      <td>Transmission between Finland and Northern Sweden - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/transmission-between-finland-and-northern-sweden-real-time-data</td>
    </tr>
    <tr>
      <th>120</th>
      <td>187.0</td>
      <td>Sähkönsiirto Suomen ja Norjan välillä - reaaliaikatieto</td>
      <td>Transmission between Finland and Norway - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/transmission-between-finland-and-norway-real-time-data</td>
    </tr>
    <tr>
      <th>121</th>
      <td>195.0</td>
      <td>Sähkönsiirto Suomen ja Venäjän välillä - reaaliaikatieto</td>
      <td>Transmission between Finland and Russia - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/transmission-between-finland-and-russia-real-time-data</td>
    </tr>
    <tr>
      <th>122</th>
      <td>90.0</td>
      <td>Sähkönsiirto Ruotsin ja Ahvenanmaan välillä - reaaliaikatieto</td>
      <td>Transmission between Sweden and Åland - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/transmission-between-sweden-and-aland-real-time-data</td>
    </tr>
    <tr>
      <th>123</th>
      <td>103.0</td>
      <td>Siirtokapasiteetti FI-RUS</td>
      <td>Transmission capacity FI-RUS</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/summakapasiteetti-fi-rus</td>
    </tr>
    <tr>
      <th>124</th>
      <td>63.0</td>
      <td>Siirtokapasiteetti RUS-FI</td>
      <td>Transmission capacity RUS-FI</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/transmission-capacity-rus-fi</td>
    </tr>
    <tr>
      <th>125</th>
      <td>280.0</td>
      <td>Sähkönsiirto Suomen ja Ahvenanmaan välillä - mitattu tuntitieto</td>
      <td>Transmission of electricity between Finland and Åland - measured hourly data</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/measured-electrical-transmission-between-finland-and-aland</td>
    </tr>
    <tr>
      <th>126</th>
      <td>61.0</td>
      <td>Sähkönsiirto Suomen ja Keski-Ruotsin välillä - mitattu tuntitieto</td>
      <td>Transmission of electricity between Finland and Central Sweden - measured hourly data</td>
      <td>MW</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/measured-electrical-transmission-between-finland-and-central-sweden</td>
    </tr>
    <tr>
      <th>127</th>
      <td>55.0</td>
      <td>Sähkönsiirto Suomen ja Viron välillä - mitattu tuntitieto</td>
      <td>Transmission of electricity between Finland and Estonia - measured hourly data</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/measured-electrical-transmission-between-finland-and-estonia</td>
    </tr>
    <tr>
      <th>128</th>
      <td>60.0</td>
      <td>Sähkönsiirto Suomen ja Pohjois-Ruotsin välillä - mitattu tuntitieto</td>
      <td>Transmission of electricity between Finland and Northern Sweden - measured hourly data</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/measured-transmission-of-electiricity-between-finland-and-northern-sweden</td>
    </tr>
    <tr>
      <th>129</th>
      <td>57.0</td>
      <td>Sähkönsiirto Suomen ja Norjan välillä - mitattu tuntitieto</td>
      <td>Transmission of electricity between Finland and Norway - measured hourly data</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/measured-electrical-transmission-between-finland-and-norway</td>
    </tr>
    <tr>
      <th>130</th>
      <td>58.0</td>
      <td>Sähkönsiirto Suomen ja Venäjän välillä - mitattu tuntitieto</td>
      <td>Transmission of electricity between Finland and Russia - measured hourly data</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/measured-transmission-of-electricity-between-finland-and-russia</td>
    </tr>
    <tr>
      <th>131</th>
      <td>244.0</td>
      <td>Ylössäätöhinta säätösähkömarkkinoilla</td>
      <td>Up-regulating price in the Balancing energy market</td>
      <td>€/MWh</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/up-regulating-price-in-the-balancing-energy-market</td>
    </tr>
    <tr>
      <th>132</th>
      <td>75.0</td>
      <td>Tuulivoimatuotanto - tuntienergiatieto</td>
      <td>Wind power generation - hourly data</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/wind-power-generation</td>
    </tr>
    <tr>
      <th>133</th>
      <td>245.0</td>
      <td>Tuulivoiman tuotantoennuste - päivitys tunneittain</td>
      <td>Wind power generation forecast - updated hourly</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/wind-power-generation-forecast-updated-every-hour</td>
    </tr>
    <tr>
      <th>134</th>
      <td>246.0</td>
      <td>Tuulivoiman tuotantoennuste - päivitys kerran vuorokaudessa</td>
      <td>Wind power generation forecast - updated once a day</td>
      <td>MWh/h</td>
      <td>1 h</td>
      <td>https://data.fingrid.fi/dataset/wind-power-generation-forecast-updated-once-a-day</td>
    </tr>
    <tr>
      <th>135</th>
      <td>181.0</td>
      <td>Tuulivoimatuotanto - reaaliaikatieto</td>
      <td>Wind power production - real time data</td>
      <td>MW</td>
      <td>3 min</td>
      <td>https://data.fingrid.fi/dataset/wind-power-production-real-time-data</td>
    </tr>
  </tbody>
</table>
