# [Air Quality Index Web Application with Django]

## Overview
This project is a Django-based web application designed to provide up to date air quality information for any city in the world. I used the AQICN API to get the air quality data and Leaflet to get the map on the website. Lastly I used PythonAnywhere to deploy the application. The application is accessible at [https://jwchoi622.pythonanywhere.com](https://jwchoi622.pythonanywhere.com). 
## Features
- Air Quality Information: The first table will give the current air quality information for the city that the user inputs. It also includes a widget <br />
  that has a concise summary of current air quality for that city. Not all cities will get a widget because the API seems to only return a widget for major cities. <br />
  It also may not have information on all of the different types of pollutants such as CO or O3. 
- Interactive Map: The map will be centered on the queried city and also have tiles that indicate the AQI index for different neighborhoods within the city. <br />
  Smaller cities may not have as many tiles because they do not have as many air quality sensors. The user can also zoom in or zoom out to look at neighboring cities. 
- PM 2.5 Forecast: The forecast focuses on PM 2.5 because it is the most harmful of pollutants and also a big problem in Korea. The forecast will usually show <br />
  the PM 2.5 forecast for the next couple days in the week and have color coded dates according to the average level for that date. 
- Calendar: The calendar will indicate which days are safe for outdoor activity by looking at the PM 2.5 index. 

## Future Improvements
- Adding a forecast for PM10 would also be helpful in determining what the air quality would be like for future days.
- The calendar could also include markers for good, average and poor air quality.
- Including different language options.

## External APIs Used
### [AQICN API]
- **Description:** I used this AQICN to get the air quality data, widget, forecast data and also the map tiles.
- **Documentation:** [https://aqicn.org/api/](#)

### [Leaflet API]
- **Description:** I used the Leaflet API to get an interactive map of the queried city.
- **Documentation:** [https://leafletjs.com/reference.html](#)

### [OpenCage Geocoding API]
- **Description:** I used the OpenCage API to get the latitude and longitude of the city and fed those coordinates into the Leaflet map. 
- **Documentation:** [https://opencagedata.com/api](#)
