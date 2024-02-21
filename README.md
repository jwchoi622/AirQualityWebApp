# **대기질 지수 웹 애플리케이션**
## **개요**
이 프로젝트는 세계 도시의 최신 대기질 정보를 제공하기 위해 Django 기반으로 설계된 웹 응용 프로그램을 개발한 것입니다. AQICN API를 사용하여 대기질 데이터를 가져오고, 이를 지도에 표시하기 위해 Leaflet를 사용했습니다. 마지막으로 PythonAnywhere를 사용하여 응용 프로그램을 배포했습니다. 이 응용 프로그램은 https://jwchoi622.pythonanywhere.com 에서 접근할 수 있습니다.

## **기능**
**대기질 정보:** 
첫 번째 표는 사용자가 입력한 도시의 현재 대기질 정보입니다. 또한 해당 도시의 현재 대기질에 대한 간결한 요약이 포함된 위젯도 제공됩니다. API가 주요 도시에 대해서만 위젯을 제공하기 때문에 모든 도시에 대한 위젯이 제공되지는 않습니다. 또한 CO(일산화탄소)나 O3(오존)과 같은 다양한 종류의 오염 물질에 대한 정보도 포함되지 않을 수 있습니다.

**인터랙티브 지도:** 
지도는 요청받은 도시를 중심에 배치하고 그 주변 지역의 AQI 지수를 타일 형태로 배치합니다. 작은 도시는 대기질 센서가 많지 않아 타일이 적을 수 있습니다. 사용자는 인접 도시를 살펴보기 위해 확대하거나 축소할 수도 있습니다.

**PM 2.5 예보:** 
예보는 한국에서 가장 유해한 PM 2.5 예측에 집중하고 있습니다. 예보는 며칠 동안의 PM 2.5 예측치를 보여주며, 해당 날짜의 평균 수준에 따라 색상이 코드화된 날짜를 표시합니다.

**캘린더:** 
캘린더는 PM 2.5 지수를 보고 야외 활동에 안전한 날을 표시합니다.

## **향후 개선사항**
1) PM10에 대한 예보를 추가하여 향후 대기질을 판단하는 데 도움이 되려고 합니다.   
2) 캘린더에도 좋음, 보통, 나쁨 대기질에 대한 표시를 포함하려고 합니다.  
3) 다양한 언어 옵션을 포함하려고 합니다.  

## **사용된 API**
**AQICN API**  
설명: AQICN API를 사용하여 대기질 데이터, 위젯, 예보 데이터 및 지도 타일을 가져왔습니다.  
문서: https://aqicn.org/api/  

**Leaflet API**  
설명: Leaflet API를 사용하여 조회된 도시의 인터랙티브 지도를 가져왔습니다.  
문서: https://leafletjs.com/reference.html  

**OpenCage 지오코딩 API**  
설명: OpenCage API를 사용하여 도시의 위도와 경도를 가져오고 이 좌표를 Leaflet 지도에 입력했습니다.  
문서: https://opencagedata.com/api  

# Air Quality Index Web Application with Django
## Overview
This project is a Django-based web application designed to provide up to date air quality information for any city in the world. I used the AQICN API to get the air quality data and Leaflet to get the map on the website. Lastly I used PythonAnywhere to deploy the application. The application is accessible at [https://jwchoi622.pythonanywhere.com](https://jwchoi622.pythonanywhere.com). 
## Features
- **Air Quality Information:** The first table will give the current air quality information for the city that the user inputs. It also includes a widget 
  that has a concise summary of current air quality for that city. Not all cities will get a widget because the API seems to only return a widget for major cities. 
  It also may not have information on all of the different types of pollutants such as CO or O3. 
- **Interactive Map:** The map will be centered on the queried city and also have tiles that indicate the AQI index for different neighborhoods within the city. 
  Smaller cities may not have as many tiles because they do not have as many air quality sensors. The user can also zoom in or zoom out to look at neighboring cities. 
- **PM 2.5 Forecast:** The forecast focuses on PM 2.5 because it is the most harmful of pollutants and also a big problem in Korea. The forecast will usually show 
  the PM 2.5 forecast for the next couple days in the week and have color coded dates according to the average level for that date. 
- **Calendar:** The calendar will indicate which days are safe for outdoor activity by looking at the PM 2.5 index. 

## Future Improvements
- Adding a forecast for PM10 would also be helpful in determining what the air quality would be like for future days.
- The calendar could also include markers for good, average and poor air quality.
- Including different language options.

## External APIs Used
### AQICN API
- **Description:** I used this AQICN to get the air quality data, widget, forecast data and also the map tiles.
- **Documentation:** [https://aqicn.org/api/](https://aqicn.org/api/)

### Leaflet API
- **Description:** I used the Leaflet API to get an interactive map of the queried city.
- **Documentation:** [https://leafletjs.com/reference.html](https://leafletjs.com/reference.html)

### OpenCage Geocoding API
- **Description:** I used the OpenCage API to get the latitude and longitude of the city and fed those coordinates into the Leaflet map. 
- **Documentation:** [https://opencagedata.com/api](https://opencagedata.com/api)
