# tod-on-main

## Terms
- DA: Dissemination Area
- CT: Census Tract

## Notebooks

### data_collection(DA).ipynb
This notebook collects the census data from cancensus using thier R package. The notebook uses ```find_census_vectors``` to find the vector codes of the census data that we are interested in. It then collects and saves this data for 2001-2021

### data_cleaning(DA).ipynb
This notebook cleans the data by selecting and renaming the columns we are interested in. It also removes all dissemination areas we are not interested in.

### data_collection(CT).ipynb
This notebook loads the census data from the downloaded raw data files. It then cleans the data by renaming the columns we are interested in. Finally, the 1976-1996 census data is saved.

### data_extraction.ipynb
This notebook combines the census data, boundary data, and station data. It creaters a buffer zone 800m around the stations and finds a weighted average of the data we are interested in given the census tracts/dissemination areas it intersects. It merges all this data together and saves it as ```tod-on-main.csv``` in /data

### NB
Data from 2021 - 2001 is broken down by Dissemination Area and collected through cancensus. 1996 and later is broken down by Census Tract andcollected through UNICEN.