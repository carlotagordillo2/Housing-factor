# 🏠 Housing Factor

**Your gateway to smart real estate investment.**

---

## 🧑‍💼 Who We Are and Our Mission

We are a specialized consulting firm focused on advising and mediating among various stakeholders in the real estate market. Through cutting-edge data collection technology and analytical expertise, we add unparalleled value to our clients' investments.

## 🔍 Our Analysis: Approach and Origins

Our research includes data on housing characteristics across Spain, collected from real estate portals, social sources, and official cadastral records.

---

### 📊 Data Sources

#### 1. **Official Data Sources**

We gather data from reliable national sources, including:

- **Instituto Nacional de Estadística (INE)**
- **Social Security (SS)**
- **Instituto Geográfico Nacional (IGN)**
- **Servicio Público de Empleo Estatal (SEPE)**

**Key data collected:**

- Social Security affiliation by municipality
- Municipality area and housing area by municipality
- Ownership vs. rental status by municipality
- Yearly housing construction stats
- Tourist housing by municipality

#### 2. **Real Estate Portal Data (Idealista) via Web Scraping**

Through Idealista, we collected a representative sample of housing offers (sales and rentals) from the 20 largest municipalities. Due to cost and resource considerations, our focus was on the most populous neighborhoods.

*Note: The sample may reflect economic disparities within certain neighborhoods.*

**Collected metrics include:**

- Price (sale or rental)
- Number of rooms
- Square meters
- Location (City/Zone/Neighborhood)
- Garage availability
- Key property features (elevator, floor level, orientation)

### 🔄 Data Collection Process Overview

Our web scraping process involved several interdependent functions:

1. **Accessing the Website:** Filtering links by city, zone, and neighborhood, we created specific functions for different property types (rental vs. sale).
2. **Extracting Data:** A structured dataset was created from lists of offers, each converted into a data frame.
3. **Automated Iteration by Location:** Our scripts iterated through each city, zone, and neighborhood to organize the data seamlessly.

---

## 🔍 Identifying Investment Opportunities

With our dataset established, we concentrated on the top 20 most populated municipalities, analyzing housing and demographic characteristics.

### 1. 🏙 Municipality Characteristics

Our findings reveal that while Madrid and Barcelona lead in population, they don’t hold the largest areas.

Key insights:

- **Barcelona**: Has limited housing space relative to its high population, suggesting high prices and smaller home sizes. Investment in nearby, well-connected areas could offer promising returns.
- **Elche**: High land availability but lower total housing units.
- **Municipalities with High Demand**: Madrid, Barcelona, Seville, Zaragoza, and Málaga exhibit high Social Security affiliation with limited housing availability, suggesting an investment-worthy demand surplus.

### 2. 🏠 Housing Tenure by Municipality

Our tenure distribution shows a higher rental concentration in dense cities with limited space, such as Barcelona, Valencia, and Alicante.

Additional observations:

- **Granada**: High rental demand, likely due to its significant student population.
- **Madrid, Seville, and Palma**: These cities could benefit from increased rental stock.
- **L’Hospitalet**: High demand for rental properties but insufficient rental supply.

### 3. 🌴 Tourism and Housing

Tourist-heavy municipalities exhibit higher average prices and notable rental price variations, particularly visible in box plot analyses.

### 4. 🏡 Housing Size by Tenure

In general, purchased properties exhibit more uniform size ranges, while rental properties tend to be larger on average.

**Investment Opportunities:**

- **Low-cost Housing with Larger Floor Space for Sale**
- **Rental Investments in Tourist Areas**: Cities like Palma, Las Palmas, and Alicante show strong demand and potential returns.

### 5. 👥 Household Size and Room Distribution

Some noteworthy insights include:

- **L’Hospitalet**: Has the smallest housing sizes and fewest rooms, correlating with its limited municipal space.
- **Granada**: High demand for three-room rentals (student population), while four-room units represent an untapped opportunity.
- **Madrid and Barcelona**: Predominantly one- and two-person households indicate high demand for studios and one-room apartments.
- **Las Palmas**: Offers more room variety, suitable for tourism-driven demand.

### 6. 🛏 Room Count by Tenure

**Sale Range:** 1-3 rooms | **Rental Range:** 1-4 rooms

**Recommendations:**

- Expand offerings of 3+ room units for sale.
- Increase single-room rentals in high-demand urban centers (Madrid, Barcelona, Valencia).

### 7. 💸 Price Distribution

Rental prices show the highest outliers in Madrid, Barcelona, and popular coastal cities like Valencia, Málaga, and Alicante.

### 8. 📈 Gross Profitability by Municipality

Key insights from profitability rankings:

- **Elche**: Highest gross profitability, though low population and high ownership rates limit demand.
- **L’Hospitalet de Llobregat**: With over 6% profitability, this suburb of Barcelona is ideal for rental investments.
- **Madrid and Valladolid**: High-demand cities with strong profitability potential.

---

## 📈 Conclusions from Our Analysis

- **Invest in Rentals** in municipalities with high demand and profitability, like L’Hospitalet de Llobregat.
- **Expand Rental Stock in University Cities**: Prioritize areas like Granada and high-cost, space-constrained cities like Madrid and Barcelona.
- **Increase Sale Offerings of 3+ Room Apartments and Studios** in high-demand areas such as Madrid, Barcelona, and Valencia.
- **Luxury Market Potential**: Strong investment opportunities in tourist-heavy cities like Las Palmas.

## 🚀 Next Steps in Our Analysis

### Future Enhancements

1. **Evaluate Demand and Supply by Municipality** (sources like INE)
2. **Assess Local Amenities** (e.g., hospitals, schools) by municipality to measure quality of life.
3. **Analyze Garage Space Availability** to uncover potential for garage investments.
4. **Consider Neighboring, Larger-Land Municipalities** with high demand for development potential.
5. **Explore Luxury Housing Market Trends** in top tourist destinations like Las Palmas, Málaga, and Palma.

---
