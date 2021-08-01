# DROP TABLES
immigration_table_drop = "DROP TABLE IF EXISTS f_immigration"
airport_table_drop = "DROP TABLE IF EXISTS d_airport"
demographics_table_drop = "DROP TABLE IF EXISTS d_demographics"
state_table_drop = "DROP TABLE IF EXISTS d_US_state"

# CREATE TABLES
immigration_table_create = ("""
    CREATE TABLE IF NOT EXISTS f_immigration ( 
        immigration_key VARCHAR NOT NULL PRIMARY KEY, 
        cicid INT NOT NULL,
        year SMALLINT NOT NULL,
        month SMALLINT NOT NULL,
        residence_country VARCHAR,
        citizenship_country VARCHAR,
        arrival_date DATE NOT NULL,
        departure_date DATE,
        arrival_mode VARCHAR,
        arrival_port VARCHAR,
        age INT NULL,
        visa_type VARCHAR NOT NULL,
        visa_category VARCHAR NOT NULL,
        birth_year INT,
        gender VARCHAR(1),
        arrival_state VARCHAR
    )
""")

airport_table_create = ("""
    CREATE TABLE IF NOT EXISTS d_airport ( 
        airport_key VARCHAR NOT NULL PRIMARY KEY, 
        identifier VARCHAR(10), 
        airport_name VARCHAR,
        municipality VARCHAR NOT NULL, 
        iata_code VARCHAR,
        state_code VARCHAR NOT NULL,
        type VARCHAR
    )
    diststyle all
""")

demographics_table_create = ("""
    CREATE TABLE IF NOT EXISTS d_demographics ( 
        demographics_key VARCHAR NOT NULL PRIMARY KEY, 
        city VARCHAR(100) NOT NULL, 
        state VARCHAR(20) NOT NULL, 
        median_age DECIMAL, 
        male_population INT,
        female_population INT,
        total_population INT,
        num_veterans INT,
        foreign_born INT,
        avg_household_size DECIMAL,
        state_code VARCHAR NOT NULL,
        race VARCHAR
    ) 
    diststyle all
""")

state_table_create = ("""
    CREATE TABLE IF NOT EXISTS d_US_state ( 
        state_key VARCHAR NOT NULL PRIMARY KEY, 
        state_code VARCHAR (2) NOT NULL,
        state_name VARCHAR(100) NOT NULL
    )
    diststyle all
""")


# QUERIES
create_table_queries = [immigration_table_create, airport_table_create, demographics_table_create, state_table_create]
drop_table_queries = [immigration_table_drop, airport_table_drop, demographics_table_drop, state_table_drop]