# Weather data CLI project


Run the CLI by executing the cli.py file

This will present the menu: 

Weather Database CLI
1. View all entries
2. Fetch and store latest weather
3. Modify an entry
4. Delete an entry
5. Exit

Fetch and Store Weather Data
Select option 2 to fetch the latest weather data and store it in the database.

View Stored Entries
Select option 1 to display all stored weather data.

Modify an Entry
Select option 3 and follow the prompts to update a specific field.

Delete an Entry
Select option 4 and enter the ID of the entry you wish to delete.

The SQLite database (weather_data.db) contains a weather table with the following structure:

id          INTEGER PRIMARY KEY AUTOINCREMENT
Date        TEXT NOT NULL
Temperature REAL
Feels_like  REAL
Humidity    INTEGER
Wind_speed  REAL
Description TEXT

