DROP DATABASE IF EXISTS hbnb_dev_db;

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Set all privileges.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

USE hbnb_dev_db;

-- Table 'users'
CREATE TABLE users (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    PRIMARY KEY (id)
);

-- Table 'states'
CREATE TABLE states (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
);

-- Table 'cities'
CREATE TABLE cities (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL,
    state_id VARCHAR(60) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states (id)
);

-- Table 'places'
CREATE TABLE places (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    city_id VARCHAR(60) NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    description VARCHAR(1024),
    number_rooms INTEGER,
    number_bathrooms INTEGER,
    max_guest INTEGER,
    price_by_night INTEGER,
    latitude FLOAT,
    longitude FLOAT,
    PRIMARY KEY (id),
    FOREIGN KEY (city_id) REFERENCES cities (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

-- Table 'reviews'
CREATE TABLE reviews (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    text VARCHAR(1024) NOT NULL,
    place_id VARCHAR(60) NOT NULL,
    user_id VARCHAR(60) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (place_id) REFERENCES places (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

-- Table 'amenities'
CREATE TABLE amenities (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
);

-- Table 'place_amenity' (Many-to-Many Relationship between 'places' and 'amenities')
CREATE TABLE place_amenity (
    place_id VARCHAR(60) NOT NULL,
    amenity_id VARCHAR(60) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places (id),
    FOREIGN KEY (amenity_id) REFERENCES amenities (id)
);

INSERT INTO `states` VALUES ('421a55f4-7d82-47d9-b54c-a76916479545','2017-03-25 19:42:40','2017-03-25 19:42:40','Alabama'),('421a55f4-7d82-47d9-b54c-a76916479546','2017-03-25 19:42:40','2017-03-25 19:42:40','Arizona'),('421a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','California'),('421a55f4-7d82-47d9-b54c-a76916479548','2017-03-25 19:42:40','2017-03-25 19:42:40','Colorado'),('421a55f4-7d82-47d9-b54c-a76916479549','2017-03-25 19:42:40','2017-03-25 19:42:40','Florida'),('421a55f4-7d82-47d9-b54c-a76916479550','2017-03-25 19:42:40','2017-03-25 19:42:40','Georgia'),('421a55f4-7d82-47d9-b54c-a76916479551','2017-03-25 19:42:40','2017-03-25 19:42:40','Hawaii'),('421a55f4-7d82-47d9-b54c-a76916479552','2017-03-25 19:42:40','2017-03-25 19:42:40','Illinois'),('421a55f4-7d82-47d9-b54c-a76916479553','2017-03-25 19:42:40','2017-03-25 19:42:40','Indiana'),('421a55f4-7d82-47d9-b54c-a76916479554','2017-03-25 19:42:40','2017-03-25 19:42:40','Louisiana'),('421a55f4-7d82-47d9-b54c-a76916479555','2017-03-25 19:42:40','2017-03-25 19:42:40','Minnesota'),('421a55f4-7d82-47d9-b54c-a76916479556','2017-03-25 19:42:40','2017-03-25 19:42:40','Mississippi'),('421a55f4-7d82-47d9-b54c-a76916479557','2017-03-25 19:42:40','2017-03-25 19:42:40','Oregon');

INSERT INTO `cities` VALUES ('521a55f4-7d82-47d9-b54c-a76916479545','2017-03-25 19:42:40','2017-03-25 19:42:40','Akron','421a55f4-7d82-47d9-b54c-a76916479545'),('521a55f4-7d82-47d9-b54c-a76916479546','2017-03-25 19:42:40','2017-03-25 19:42:40','Douglas','421a55f4-7d82-47d9-b54c-a76916479546'),('521a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','San Francisco','421a55f4-7d82-47d9-b54c-a76916479547'),('521a55f4-7d82-47d9-b54c-a76916479548','2017-03-25 19:42:41','2017-03-25 19:42:41','Denver','421a55f4-7d82-47d9-b54c-a76916479548'),('521a55f4-7d82-47d9-b54c-a76916479549','2017-03-25 19:42:41','2017-03-25 19:42:41','Miami','421a55f4-7d82-47d9-b54c-a76916479549'),('521a55f4-7d82-47d9-b54c-a76916479551','2017-03-25 19:42:41','2017-03-25 19:42:41','Honolulu','421a55f4-7d82-47d9-b54c-a76916479551'),('521a55f4-7d82-47d9-b54c-a76916479552','2017-03-25 19:42:41','2017-03-25 19:42:41','Chicago','421a55f4-7d82-47d9-b54c-a76916479552'),('521a55f4-7d82-47d9-b54c-a76916479554','2017-03-25 19:42:41','2017-03-25 19:42:41','New Orleans','421a55f4-7d82-47d9-b54c-a76916479554'),('521a55f4-7d82-47d9-b54c-a76916479555','2017-03-25 19:42:41','2017-03-25 19:42:41','Saint Paul','421a55f4-7d82-47d9-b54c-a76916479555'),('521a55f4-7d82-47d9-b54c-a76916479556','2017-03-25 19:42:41','2017-03-25 19:42:41','Jackson','421a55f4-7d82-47d9-b54c-a76916479556'),('521a55f4-7d82-47d9-b54c-a76916479557','2017-03-25 19:42:41','2017-03-25 19:42:41','Portland','421a55f4-7d82-47d9-b54c-a76916479557'),('531a55f4-7d82-47d9-b54c-a76916479545','2017-03-25 19:42:40','2017-03-25 19:42:40','Babbie','421a55f4-7d82-47d9-b54c-a76916479545'),('531a55f4-7d82-47d9-b54c-a76916479546','2017-03-25 19:42:40','2017-03-25 19:42:40','Kearny','421a55f4-7d82-47d9-b54c-a76916479546'),('531a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','San Jose','421a55f4-7d82-47d9-b54c-a76916479547'),('531a55f4-7d82-47d9-b54c-a76916479549','2017-03-25 19:42:41','2017-03-25 19:42:41','Orlando','421a55f4-7d82-47d9-b54c-a76916479549'),('531a55f4-7d82-47d9-b54c-a76916479551','2017-03-25 19:42:41','2017-03-25 19:42:41','Kailua','421a55f4-7d82-47d9-b54c-a76916479551'),('531a55f4-7d82-47d9-b54c-a76916479552','2017-03-25 19:42:41','2017-03-25 19:42:41','Peoria','421a55f4-7d82-47d9-b54c-a76916479552'),('531a55f4-7d82-47d9-b54c-a76916479554','2017-03-25 19:42:41','2017-03-25 19:42:41','Baton rouge','421a55f4-7d82-47d9-b54c-a76916479554'),('531a55f4-7d82-47d9-b54c-a76916479556','2017-03-25 19:42:41','2017-03-25 19:42:41','Tupelo','421a55f4-7d82-47d9-b54c-a76916479556'),('531a55f4-7d82-47d9-b54c-a76916479557','2017-03-25 19:42:41','2017-03-25 19:42:41','Eugene','421a55f4-7d82-47d9-b54c-a76916479557'),('541a55f4-7d82-47d9-b54c-a76916479545','2017-03-25 19:42:40','2017-03-25 19:42:40','Calera','421a55f4-7d82-47d9-b54c-a76916479545'),('541a55f4-7d82-47d9-b54c-a76916479546','2017-03-25 19:42:40','2017-03-25 19:42:40','Tempe','421a55f4-7d82-47d9-b54c-a76916479546'),('541a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','Fremont','421a55f4-7d82-47d9-b54c-a76916479547'),('541a55f4-7d82-47d9-b54c-a76916479551','2017-03-25 19:42:41','2017-03-25 19:42:41','Pearl city','421a55f4-7d82-47d9-b54c-a76916479551'),('541a55f4-7d82-47d9-b54c-a76916479552','2017-03-25 19:42:41','2017-03-25 19:42:41','Naperville','421a55f4-7d82-47d9-b54c-a76916479552'),('541a55f4-7d82-47d9-b54c-a76916479554','2017-03-25 19:42:41','2017-03-25 19:42:41','Lafayette','421a55f4-7d82-47d9-b54c-a76916479554'),('541a55f4-7d82-47d9-b54c-a76916479556','2017-03-25 19:42:41','2017-03-25 19:42:41','Meridian','421a55f4-7d82-47d9-b54c-a76916479556'),('551a55f4-7d82-47d9-b54c-a76916479545','2017-03-25 19:42:40','2017-03-25 19:42:40','Fairfield','421a55f4-7d82-47d9-b54c-a76916479545'),('551a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','Napa','421a55f4-7d82-47d9-b54c-a76916479547'),('551a55f4-7d82-47d9-b54c-a76916479552','2017-03-25 19:42:41','2017-03-25 19:42:41','Urbana','421a55f4-7d82-47d9-b54c-a76916479552'),('561a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','Sonoma','421a55f4-7d82-47d9-b54c-a76916479547'),('561a55f4-7d82-47d9-b54c-a76916479552','2017-03-25 19:42:41','2017-03-25 19:42:41','Joliet','421a55f4-7d82-47d9-b54c-a76916479552');

INSERT INTO `amenities` VALUES ('821a55f4-7d82-47d9-b54c-a76916479551','2017-03-25 19:44:42','2017-03-25 19:44:42','Wifi'),('821a55f4-7d82-47d9-b54c-a76916479552','2017-03-25 19:44:42','2017-03-25 19:44:42','Pets friendly'),('821a55f4-7d82-47d9-b54c-a76916479553','2017-03-25 19:44:42','2017-03-25 19:44:42','Elevator in building'),('821a55f4-7d82-47d9-b54c-a76916479554','2017-03-25 19:44:42','2017-03-25 19:44:42','Doorman'),('821a55f4-7d82-47d9-b54c-a76916479555','2017-03-25 19:44:42','2017-03-25 19:44:42','Cable TV'),('821a55f4-7d82-47d9-b54c-a76916479556','2017-03-25 19:44:42','2017-03-25 19:44:42','Dryer'),('821a55f4-7d82-47d9-b54c-a76916479557','2017-03-25 19:44:42','2017-03-25 19:44:42','Hair dryer'),('821a55f4-7d82-47d9-b54c-a76916479558','2017-03-25 19:44:42','2017-03-25 19:44:42','Iron'),('821a55f4-7d82-47d9-b54c-a76916479559','2017-03-25 19:44:42','2017-03-25 19:44:42','Washer'),('821a55f4-7d82-47d9-b54c-a76916479560','2017-03-25 19:44:42','2017-03-25 19:44:42','Laundry room'),('821a55f4-7d82-47d9-b54c-a76916479561','2017-03-25 19:44:42','2017-03-25 19:44:42','Air conditioning'),('821a55f4-7d82-47d9-b54c-a76916479562','2017-03-25 19:44:42','2017-03-25 19:44:42','Hot tub'),('821a55f4-7d82-47d9-b54c-a76916479563','2017-03-25 19:44:42','2017-03-25 19:44:42','Smoking allowed');
