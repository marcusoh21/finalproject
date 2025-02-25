import sqlite3

def create_connection():
    return sqlite3.connect("weather_data.db")

def insert_entry(data):
    """Insert a new weather entry into the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO weather (date, temperature, feels_like, humidity, wind_speed, description)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (data["date"], data["temperature"], data["feels_like"], data["humidity"], data["wind_speed"], data["description"]))
    conn.commit()
    conn.close()

def get_all_entries():
    """Retrieve all weather entries from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather")
    entries = cursor.fetchall()
    conn.close()
    return entries

def delete_entry(entry_id):
    """Delete a weather entry by its ID."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM weather WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()

def update_entry(entry_id, field, new_value):
    """Update a specific field of a weather entry."""
    conn = create_connection()
    cursor = conn.cursor()
    query = f"UPDATE weather SET {field} = ? WHERE id = ?"
    cursor.execute(query, (new_value, entry_id))
    conn.commit()
    conn.close()
