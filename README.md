# mi-weather

## Description of the application
MI-Weather is a web application that provides the user with current weather information and forecasts for different locations around the world.

## How the application works
### Using docker:
* Clone the repository: git clone https://github.com/Nhlosokuhle/mi-weather.git
* Navigate to the project directory: cd mi-weather
* MAKE SURE THAT DOCKER DESKTOP IS OPENED
* Build the Docker image: docker build -t mi-weather .
* Run the Docker container: docker run -p 8000:8000 mi-weather
* After following the installation instructions, you should be able to access the Django project by navigating to http://localhost:8000 in your web browser. From there, you can create the account and access the menu.

### On your pc:
* Clone the repository: git clone https://github.com/Nhlosokuhle/mi-weather.git
* Navigate to the project directory: cd mi-weather
* Run the following command: py managr.py runserver
* After following the installation instructions, you should be able to access the Django project by navigating to http://localhost:8000 in your web browser.

The application is available online at https://mi-weather7.herokuapp.com/

## Credits
MI-Weather7 is created by Nhlosokuhle Bandile Khoza and is based on the OpenWeatherMap API. The application is licensed under the MIT License.
