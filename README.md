The White Lotus is a renowned hotel chain that strategically invests into a couple of new
locations every year to expand their iconic portfolio of hotels. They have recently come to
Predictive Hospitality Partners (PHP) to advise them on what the optimal location of their next
hotel should be.

The COO of the White Lotus has expressed a strong preference for the new location to be in
Florida, where she likes to spend her winters playing golf and relaxing with her family. The board
has agreed with her preference, given the popularity of the Sunshine state and the fact that the
chain currently doesn't own any hotels in Florida yet.

Although the White Lotus is mostly known for their luxury resorts, they also own a considerable
portfolio of hotels in all types of categories, from business over budget to airport hotels. For this
particular property in Florida, they don’t have a strong preference for any particular type of hotel,
as long as the return on investment is high enough. Consequently, their allocated budget is also
flexible towards the investment that is needed.

Although the White Lotus has their own internal data team, they do not have access to the large
amounts of market data and industry expertise that PHP have built up during the last years. That’s
why your group, the Data Science team of PHP, has been given full capacity and responsibility to
work on this project. Predictive Hospitality Partners (PHP) owns large data volumes relevant to
the hospitality industry that can help make this decision. Next to information on existing
accommodations in Florida, the travel-based consultancy and software provider has massive
amounts of rates data extracted from booking.com, as well as aggregated final occupancy data
for the most popular travel destinations in the state.

The White Lotus is a strategically vital client for PHP, not only due to the firm's existing portfolio of
hotels that already generate substantial revenue, but also because this project represents a key
opportunity: successful execution will establish a new, highly valuable service offering –
data-driven location recommendations – positioning PHP for significant growth in the hospitality
sector.

As part of the deal both parties have signed, the White Lotus and PHP have agreed upon several
deliverables, each targeted towards a different audience. The White Lotus will use all of this
information to make an informed decision about their new investment.



Accommodation_facts
This dataset combines information from various Online Travel Agencies (OTAs) to provide a
comprehensive list of all available accommodations in Florida, US. Even though the word “hotel”
is often used in the descriptions, also other accommodations types such as short-term rentals,
boutique hotels, .. can be found in this dataset.

Column Name Description
hotel_name The name of the hotel.
hotel_id The unique identifier of the hotel (internal).
status Last known status of the accommodation. Can be ‘open’, ‘closed’ or
‘opening_future’.
bookingdotcom_id The unique identifier of the hotel on booking.com.
bookingdotcom_review_score The review score of the hotel on booking.com.
hotel_segment Hotel Segmentation is a way to split hotels into logical segments
based on the accounts linked to them. This segmentation consists
of three larger Hotel Segments (Global Chain, Group and
Independent), and seven related Sub-Segments.
● Global Chain = A hotel with at least one link to a Global
Chain account (i.e. a list of global hotel chains). Contains the
Hotel Sub-Segment “Global Chain”.
● Group = A hotel with at least one link to a Group account,
but without a link to a Global Chain. A group account can be
either one of the below Hotel Sub-Segments:
○ Local Chain
○ Management Company
○ Ownership Company
○ Representation Company
○ Tech Provider
○ Other Business Group Company (i.e. Non-Profit
Organizations, ...)
● Independent = A hotel without a relationship to a Global
Chain or any other group account (i.e. Local Chain /
Management Company / Ownership Company / ...).
Contains the Hotel Sub-Segment “Independent”.
hotel_subsegment The subsegment of the hotel (see above).
accommodation_type_name The type of accommodation (e.g., Villa, Apartment, Hotel, ...).
room_count Physical rooms capacity of the hotel.
stars The number of stars assigned to the hotel.
brand_name The name of the hotel brand.
brand_size The size of the hotel brand (worldwide).
chain_name The name of the hotel chain.
chain_size The size of the hotel chain (worldwide).
latitude The latitude of the hotel location.
longitude The longitude of the hotel location.
city The city where the hotel is located.
timezone_name The name of the timezone where the hotel is located.
country_code_alpha_2 The ISO 3166-1 alpha-2 country code where the hotel is located.
travel_destination_name The name of the travel destination* where the hotel is located.
bookingdotcom_url URL of the hotel found on booking.com
amenities_list List of hotel amenities that are shown on booking.com


Market_otb
Market OTB data contains aggregated final occupancies for all of PHP’s travel destinations*. The
final occupancy is expressed as a percentage, indicating the final percentage of total available
rooms sold on a certain stay date.
*PHP uses a simple algorithm to identify the geophysical boundaries of popular travel
destinations in Florida

Column Name Description
travel_destination_name Name of the travel destination
stay_date Stay date
avg_occupancy Average occupancy, aggregated over all hotels within the travel
destination for which occupancy data is available


Rates
Rates data is data that is extracted from booking.com. An extract date indicates the day on which
these rates were extracted. A stay date (i.e. the arrival date of the guest) indicates the day for
which these rates were extracted. Data extraction was done for lead time 1, 3, 7, 14 and 28. That
means that on a given extract date, the stay dates 1, 3, 7, 14 and 28 days out from that extract
date are retrieved. Even though PHP has more lead times, this sample should be large enough to
draw conclusions from how the rates of a hotel have evolved over time.

Column Name Description
bookingdotcom_id The unique identifier of the hotel on booking.com.
stay_date The stay date for which the relevant rates information is displayed
extract_date The day on which the rates were extracted
lead_time Difference between stay date and extract date (in days)
price_value Price charged for a one-night stay with the most flexible cancellation
option available
sold_out Flag indicating if the entire hotel was sold out. If true, this means no rates
could be found for a one-night stay on the relevant stay date.
currency Currency of the price_value
meal_type_included Meal type that is included in the price_value
max_persons Maximum number of guests that are allowed to stay in the room
room_name Name of the room as displayed on booking.com
breakfast_cost Separate breakfast rate displayed on booking.com
vat_incl Boolean flag indicating if taxes are included in the price_value (VAT =
Value Added Tax)

## Cleaning and Structuring the Data

A helper script is provided in `scripts/clean_datasets.py` to standardize the datasets and
combine the daily rate files. The script performs the following steps:

1. **Accommodation Facts** – column names are converted to `snake_case`, numeric fields
   are coerced to numbers and rows missing a `bookingdotcom_id` are dropped.
2. **Market OTB** – date columns are parsed to proper `datetime` objects and column
   names are normalized.
3. **Rates** – all CSV files in `Data/Rates/` are concatenated into a single file with
   normalized column names and parsed dates.

Running the script creates a new `Data/clean/` directory containing cleaned CSV files for
all three datasets.

Usage:
```bash
python scripts/clean_datasets.py
```
