# Weather data CLI project


Run the CLI by executing the cli.py file

This will present the menu: 

Weather Database CLI
1. View all entries
2. Fetch and store latest weather
3. Modify an entry
4. Delete an entry
5. Exit

Fetch and Store Weather Data<br>
Select option 2 to fetch the latest weather data and store it in the database.<br>

View Stored Entries<br>
Select option 1 to display all stored weather data.<br>

Modify an Entry<br>
Select option 3 and follow the prompts to update a specific field.<br>

Delete an Entry<br>
Select option 4 and enter the ID of the entry you wish to delete.<br>

The SQLite database (weather_data.db) contains a weather table with the following structure:

```
id          INTEGER PRIMARY KEY AUTOINCREMENT<br>
date        TEXT NOT NULL<br>
temperature REAL<br>
feels_like  REAL<br>
humidity    INTEGER<br>
wind_speed  REAL<br>
description TEXT<br>
```


