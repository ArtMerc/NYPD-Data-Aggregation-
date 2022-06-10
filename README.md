# NYPD-Data-Aggregation-
Data Aggregation Analysis on the 123rd NYPD Precinct, containing age, race, and sex.



INFORMATION ABOUT NYPD DATASET:


This is a breakdown of every arrest effected in NYC by the NYPD during the current year.
This data is manually extracted every quarter and reviewed by the Office of Management Analysis and Planning.
Each record represents an arrest effected in NYC by the NYPD and includes information about the type of crime, the location and time of enforcement.
In addition, information related to suspect demographics is also included.
This data can be used by the public to explore the nature of police enforcement activity.
Please refer to the attached data footnotes for additional information about this dataset.


Column Name	Description	Type
ARREST_KEY	
Randomly generated persistent ID for each arrest
Plain Text
ARREST_DATE	
Exact date of arrest for the reported event
Date & Time
PD_CD	
Three digit internal classification code (more granular than Key Code)
Number
PD_DESC	
Description of internal classification corresponding with PD code (more granular than Offense Description)
Plain Text
KY_CD	
Three digit internal classification code (more general category than PD code)
Number
OFNS_DESC	
Description of internal classification corresponding with KY code (more general category than PD description)
Plain Text
LAW_CODE	
Law code charges corresponding to the NYS Penal Law, VTL and other various local laws
Plain Text
LAW_CAT_CD	
Level of offense: felony, misdemeanor, violation
Plain Text
ARREST_BORO	
Borough of arrest. B(Bronx), S(Staten Island), K(Brooklyn), M(Manhattan), Q(Queens)
Plain Text
ARREST_PRECINCT	
Precinct where the arrest occurred
Number
JURISDICTION_CODE	
Jurisdiction responsible for arrest. Jurisdiction codes 0(Patrol), 1(Transit) and 2(Housing) represent NYPD whilst codes 3 and more represent non NYPD jurisdictions
Number
AGE_GROUP	
Perpetrator’s age within a category
Plain Text
PERP_SEX	
Perpetrator’s sex description
Plain Text
PERP_RACE	
Perpetrator’s race description
Plain Text
X_COORD_CD	
Midblock X-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104)
Number
Y_COORD_CD	
Midblock Y-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104)
Number
Latitude	
Latitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326)
Number
Longitude	
Longitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326)
Number
New Georeferenced Column	
Point
