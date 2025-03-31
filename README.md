# **Real-Time Twitter Analytics Dashboard - Power BI**

## **Project Overview**
This repository contains the implementation of a **Real-Time Twitter Analytics Dashboard** developed as part of my internship at NULLCLASS. The dashboard provides insights into Twitter engagement metrics such as likes, retweets, replies, impressions, and more. It is designed to dynamically filter data based on specified conditions and display visualizations only during designated time windows.

## **Features**
- **Top Engaged Tweets Visualization**: Displays tweets with the highest engagement (top 10%).
- **Clustered Bar Chart**: Breaks down URL clicks, profile clicks, and hashtag clicks by tweet category.
- **Scatter Plot Analysis**: Examines the relationship between media engagements and media views.
- **Comparison of Engagements**: Compares replies, retweets, and likes for high-engagement tweets.
- **Engagement Rate Analysis**: Compares engagement rates for tweets with and without app opens.
- **Time-Based Filtering**: Ensures dashboards are visible only during specified timeframes.
- **Text-Based Data Filtering**: Removes specific words from tweets based on character conditions.

## **Technologies Used**
- **Power BI**: For real-time dashboard visualization.
- **DAX (Data Analysis Expressions)**: For advanced filtering and calculations.
- **Power Query**: For preprocessing and cleaning Twitter data.

## **Installation & Setup**
1. Clone this repository:
   ```bash
   git clone [https://github.com/nehabisht11/Twitter-analysis.git]
   ```
2. Open the `.pbix` file in Power BI Desktop.
3. Connect to the Twitter dataset (Ensure data source paths are configured correctly).
4. Refresh the dataset to load the latest data.
5. Publish the dashboard to Power BI Service if needed.

## **Task Breakdown**
1. **Top Engaged Tweets Visualization**
   - Displayed only between **3 PM - 5 PM IST**.
   - Tweets must have **>50 likes** and be posted on **weekdays**.
   - Tweet **character count < 30**.
   
2. **Clustered Bar Chart for Clicks Analysis**
   - Displayed only between **3 PM - 5 PM IST**.
   - Tweets must have at least **one interaction** (URL, profile, or hashtag clicks).
   - Tweet date must be **even**, and word count **>40**.

3. **Scatter Plot for Media Engagements**
   - Displayed only between **6 PM - 11 PM IST**.
   - Tweets must have **>10 replies**.
   - Highlighted tweets with **engagement rate >5%**.
   - Tweet date must be **odd**, and word count **>50**.

4. **Comparison of Replies, Retweets, and Likes**
   - Displayed between **3 PM - 5 PM IST & 7 AM - 11 AM IST**.
   - Tweets must have **media engagements > median**.
   - Filters applied:
     - Tweet **date must be odd**.
     - **Media views must be even**.
     - **Character count >20**.
     - **Words with 'S' removed**.

5. **Engagement Rate Comparison for App Opens**
   - Displayed between **12 PM - 6 PM IST & 7 AM - 11 AM IST**.
   - Tweets must be posted between **9 AM - 5 PM on weekdays**.
   - Filters applied:
     - **Tweet impression must be even**.
     - **Tweet date must be odd**.
     - **Character count >30**.
     - **Words with 'D' removed**.

## **Contribution & Feedback**
This project was developed as an individual internship assignment, and external contributions are not required. However, feedback is always welcome!

## **License**
This project is for educational and internship purposes only. Unauthorized distribution of the `.pbix` file or dashboard is prohibited.

## **Contact**
For any queries, reach out via email: **nehabisht1911@gmail.com**

---
**GitHub Repository Link**: [https://github.com/nehabisht11/Twitter-analysis.git]
