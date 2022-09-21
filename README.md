# Low Tide Web Scraper
A Python script for scraping daylight low-tides from https://www.tide-forecast.com/ which displays the data as a HTML table or json.



# How To Run the Application WithoutDocker
git clone

cd / Tide

create a virtual environment python -m venv .venv

Activate the virtual enviroment .venv/Scripts/activate

pip install -r requirements.txt

flask run

# How To Run the Application With Docker
 
 git clone
 
 cd/ Tide
 
 docker run -d -p 5000:5000 tide
 
 open a brower with localhost and port 5000
