# NBA Final Double Yous

## Objective
Predict each NBA playoff team's final W count.

## Background
21 years of regular season NBA team stats data was scraped, starting at 1997 till 2018. The scraped data was used in fitting the ML model. The SVM model is able to predict the final season's Win score per team with a mean STD of 3.5 wins. The model metrics information is stored at this location `./src/static/model/support_vector_machines.txt`.

## Usage
// Complete this section later when I have time.

## Development Process
**Step 1 - Data Gathering and Cleaning**
* Data was collected from <a href="https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1">HERE</a>.
* Bonus, live score board
** The endpoint http://data.nba.net/10s/prod/v1/<today>/scoreboard.json

**Step 2 - ML Model Build**
The code and process I used for developing the various model's used in this application is located >> `./model_building.ipynb`

**Step 3 - Flask**
Python Flask is the framework used to establish the various routes, APIs, as well as the templating system to tie the backend with what you see in the browser application.

**Step 4 - Hosting**
This application is hosted on Heroku. To veiw the app and possibly place a bet before the next NBA series is over (disclosure: we aren't liable for any of your loses, gamble at your own discretion) - [*CLICK HERE*](#) ! **not launched yet**
