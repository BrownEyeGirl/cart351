# Start with a new python script: and using the requests package, access the planet names, their diameter and populations.
# Then ... explore and install the RICH API in order to be able to output the following in your terminal/powershell/cmd Prompt window :)

# Notes 
    # to create a new virtual environment with conda: conda create --name webAPisenv python=3.13
    # to activete virtual environment: conda activate webAPisenv
    # download standard messages manager pip to manage the request package: pip install requests

#import the lib
import requests

# import rich 
from rich.console import Console # to load the colour and style   
from rich.table import Table # to load the table / columns / rows 


# url for starwars planet api 
planet_url ="https://swapi.info/api/planets"

#url with the api key appeneded
url_to_send = planet_url 

# make the request
response = requests.get(url_to_send) # get the url to send 

#get the response as json
data = response.json() 

#print the planet data 
# print(data) 

# create a console 
console = Console()
table = Table(title="Star Wars Planets")

# add columns
table.add_column("NAME", style="cyan")
table.add_column("DIAMETER", style="magenta")
table.add_column("POLULATION", style="green")

# add rows to columns
for planet in data: 
    table.add_row(planet["name"], planet["diameter"], planet["population"])

console.print(table)