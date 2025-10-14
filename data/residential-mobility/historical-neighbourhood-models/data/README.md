# Data
The data is split into before, middle, and after. This covers the 10 year period that best captures before and after the development of transit. For example:
- A station built in 2003: before_opening_date = 1996, middle_opening_date = 2001, after_opening_date = 2006
- A station built in 2004: before_opening_date = 2001, middle_opening_date = 2006, after_opening_date = 2011
- A station built in 2008: before_opening_date = 2001, middle_opening_date = 2006, after_opening_date = 2011
- A station built in 2009: before_opening_date = 2006, middle_opening_date = 2011, after_opening_date = 2016
Census years is every 5th year ending in 1 or 6.

## Before, Middle, After
The data is split into before, middle, and after. This covers the 10 year period that best captures before and after the development of transit. For example:
- A station built in 2003: before_year = 1996, middle_year = 2001, after_year = 2006
- A station built in 2004: before_year = 2001, middle_year = 2006, after_year = 2011
- A station built in 2008: before_year = 2001, middle_year = 2006, after_year = 2011
- A station built in 2009: before_year = 2006, middle_year = 2011, after_year = 2016
Census years is every 5th year ending in 1 or 6.

Every column starting with before is census data from the before_year
Every column starting with middle is census data from the middle_year
Every column starting with after is census data from the after_year


### Columns 
- **General Information**: Population Density per square kilometer, Dwellings, Private Dwellings
- Dwelling Types: Single-detached house, Semi-detached house, Row house, Apartment, Apartment Duplex, Apartment that has fewer than five storeys, Apartment that has five or more storeys, Other dwelling, Other single-attached house, Moveable dwelling
- **Number of bedrooms**: No bedrooms, 0 to 1 bedroom, 1 bedroom, 2 bedrooms, 3 bedrooms, 4 bedrooms, 4 or more bedrooms, 5 or more bedrooms, Average number of bedrooms per dwelling
- **Tenure**: Renter, Owner