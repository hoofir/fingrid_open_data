# Fingrid Open Datasets via API
Fingrid's open data platform provides machine readable access to datasets through open REST API interface.


## Registration
Fingrid provides equal service for all users of the open data platform through the free of charge API-access which requires registration.

- Make sure you have an active email address.
- Do [register](https://data.fingrid.fi/open-data-forms/registration/) and approve the license and terms of use. 
- You will receive a personal API-key right away. If you don't receive the email, please check your junk mail folder.
- Registered users may opt-in to receive email maintenance breaks or other important changes about API.
- If you want, you can also [delete your account](https://data.fingrid.fi/open-data-forms/leave/) and the related API-key.


## How to use the API
Technical API documentation for developers:  http://data.fingrid.fi/open-data-api/

- API requests to this endpoint:  https://api.fingrid.fi/
  - For an individual variable, you can get the latest event or events from a specified date/time range.
  - For a set of variables, you can get the latest events.
  - You can access data in JSON, XML or CSV formats.
- You can make custom searches for each dataset. Each dataset has an unique link to the search interface. 
- Datasets are identified by an unique `VariableId` number that you need to use in API requests. You will find the variable id numbers [here](). 
- API-key must be inserted to the http-request header x-api-key, not into the URL-address. If you are importing data from the API into an application, it is usually possible to insert the API-key by modifying the request header parameters in your application: further instructions for doing this are usually available in the documentation of your chosen software.
- You can make 10,000 requests in 24h period with one API-key. Please contact the [administrator](mailto:avoindata@fingrid.fi) if you need to make more requests.
- Data timestamps are presented in `UTC` (previously as GMT) time format. Correct format for API requests is `YYYY-MM-ddTHH:mm:ssZ` e.g. 2023-04-02T00:00:00+00:00
- Data update frequency varies by dataset: many datasets have data that is updated hourly, and some datasets include data that is updated in 3 or 5 minute intervals. The update frequency is stated in the dataset description.
- If you request frequently updated data from an extended date range, you may receive an error message that results from exceeding the maximum allowed API payload. Shorten the date range and request the results in JSON-format. 
- If you use the API in browser environment, you need to note the requirements and limitations for Cross Origin Resource Sharing (CORS). 


## Availability and uptime
The open data API is not guaranteed to have 100% uptime. Although maximum uptime is a goal, as with any service disruptions can happen at any point along the networks and Internet between the client application and the API servers. When you register for using the API, we recommend that you opt-in to the email notifications so that we can inform you about changes that affect the use of the API. You can also get information about planned maintenance breaks from the API. It's important that your application is defensive and can handle API downtime gracefully. One such way could be by implementing good caching. Another strategy could be to aim for graceful failure if the API is not available. 
