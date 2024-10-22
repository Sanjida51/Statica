import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
df = pd.read_csv("ecommerce_customer_behavior_dataset.csv")

PRIMARY_COLOR = '#2A2D34'
SECONDARY_COLOR = '#4A6FA5'
ACCENT_COLOR = '#E59500'
BACKGROUND_GRADIENT = 'linear-gradient(to bottom, #F5F5F5, #EDEDED)'
SIDEBAR_BACKGROUND_COLOR = '#2A2D34'
SIDEBAR_TEXT_COLOR = '#FFFFFF'
TEXT_COLOR = '#333333'

# Set page config
st.set_page_config(page_title='E-Commerce Dashboard', page_icon='📊', layout='wide')

# Style settings
st.markdown(
    f"""
    <style>
    
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    
    .reportview-container {{
        background: {BACKGROUND_GRADIENT};  
        color: {TEXT_COLOR};  
        font-family: 'Poppins', sans-serif;  
    }}

    
    .sidebar .sidebar-content {{
        background-color: {SIDEBAR_BACKGROUND_COLOR};  
        color: {SIDEBAR_TEXT_COLOR};  
        font-family: 'Poppins', sans-serif;
        border-radius: 10px;
    }}

   
    .stButton > button {{
        background-color: {PRIMARY_COLOR};  
        color: white;  
        border-radius: 10px;  
        padding: 10px 15px;  
        font-size: 16px;
        transition: background-color 0.3s ease;  
        font-family: 'Poppins', sans-serif;
    }}

    
    .stButton > button:hover {{
        background-color: {ACCENT_COLOR};  
        color: #ffffff;
    }}

    
    h1, h2, h3, h4, h5, h6 {{
        color: {PRIMARY_COLOR};  
        font-family: 'Poppins', sans-serif;  
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);  
    }}

    
    .level-basic {{
        background-color: {PRIMARY_COLOR};
        color: white;
        padding: 5px;
        border-radius: 8px;
        font-weight: bold;
        font-family: 'Poppins', sans-serif;
    }}

    
    .level-intermediate {{
        background-color: {SECONDARY_COLOR};
        color: white;
        padding: 5px;
        border-radius: 8px;
        font-weight: bold;
        font-family: 'Poppins', sans-serif;
    }}

    .level-critical {{
        background-color: {ACCENT_COLOR};
        color: white;
        padding: 5px;
        border-radius: 8px;
        font-weight: bold;
        font-family: 'Poppins', sans-serif;
    }}

    /* Subtle hover effect for links */
    a:hover {{
        color: {ACCENT_COLOR};  /* Highlight links when hovering */
        text-decoration: underline;
    }}

    /* Add transitions to make interactions smoother */
    * {{
        transition: all 0.3s ease;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Add some content to test the styles
st.title("Welcome to the E-Commerce Dashboard")
st.header("Customer Behavior Insights")
st.subheader("Visualize and Analyze Customer Data by STATICA")
st.markdown(
    "This dashboard provides insights into customer behavior, including purchase patterns, product preferences, and more.")

# Sample button to test styles
if st.button("Explore Data"):
    st.write("Button clicked!")

def main():
    st.title('E-Commerce Data Analysis Dashboard')

    # Sidebar navigation for selecting the level
    st.sidebar.title('Navigation')
    level = st.sidebar.selectbox('Choose Level',
                                 ['Level 1: Basic Insights',
                                  'Level 2: Intermediate Insights',
                                  'Level 3: Critical Thinking Insights'])

    # Level 1: Basic Insights
    if level == 'Level 1: Basic Insights':
        st.subheader("Level 1: Basic Insights")
        level1_option = st.sidebar.selectbox('Choose a Question',
                                             ['Q1: Find Mean, Median, and Mode (Age)',
                                              'Q2: Find variance, standard deviation, and z-score (Purchase Amount)',
                                              'Q3: Top three product categories based on purchases',
                                              'Q4: How many customers are classified as return customers?',
                                              'Q5: Average review score given by customers',
                                              'Q6: Average delivery time by subscription status (Free, Premium)',
                                              'Q7: Number of customers subscribed to the service',
                                              'Q8: Percentage of customers using different devices (Mobile, Desktop, Tablet)',
                                              'Q9: Average purchase amount with and without discounts',
                                              'Q10: Most common payment method used by customers'])
        if level1_option == 'Q1: Find Mean, Median, and Mode (Age)':
            if level1_option == 'Q1: Find Mean, Median, and Mode (Age)':
                # Calculate mean, median, and mode of Age
                mean_age = df['Age'].mean()
                median_age = df['Age'].median()
                mode_age = df['Age'].mode()[0]

                # Data for visualization
                statistics = ['Mean', 'Median', 'Mode']
                values = [mean_age, median_age, mode_age]

                # Create a smaller bar chart
                plt.figure(figsize=(5, 3))  # Further reduced size
                plt.bar(statistics, values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])

                # Add title and labels
                plt.title('Mean, Median, and Mode of Age', fontsize=12)  # Smaller font size
                plt.ylabel('Age', fontsize=9)  # Smaller font size

                # Add values on top of each bar
                for i, v in enumerate(values):
                    plt.text(i, v + 0.2, f'{v:.2f}', ha='center', fontsize=9)  # Smaller font size for values

                # Show the chart in Streamlit
                st.pyplot(plt)


        elif level1_option == 'Q2: Find variance, standard deviation, and z-score (Purchase Amount)':
            # Variance and Standard Deviation of Purchase Amount
            variance_purchase = df['Purchase Amount ($)'].var()
            std_purchase = df['Purchase Amount ($)'].std()

            # Z-score calculation for each purchase amount
            df['Z-score'] = (df['Purchase Amount ($)'] - df['Purchase Amount ($)'].mean()) / df[
                'Purchase Amount ($)'].std()

            # Create two columns in Streamlit
            col1, col2 = st.columns(2)

            # Display variance and standard deviation in the first column
            with col1:
                st.write("### Variance and Standard Deviation of Purchase Amount")
                st.write(f"Variance: {variance_purchase}")
                st.write(f"Standard Deviation: {std_purchase}")

                # Display the first few rows with Z-scores
                st.write("### Data with Z-scores")
                st.dataframe(df[['Purchase Amount ($)', 'Z-score']].head())

            # Plot Z-scores in the second column
            with col2:
                st.write("### Z-scores of Purchase Amounts")

                # Set up the figure for Z-scores scatter plot
                plt.figure(figsize=(10, 6))
                sns.scatterplot(x=df.index, y=df['Z-score'], hue=df['Z-score'], palette='coolwarm', edgecolor='w',
                                s=100)
                plt.axhline(0, color='black', linewidth=1, linestyle='--')
                plt.axhline(3, color='red', linestyle='--', label='Z = 3')
                plt.axhline(-3, color='red', linestyle='--', label='Z = -3')
                plt.title('Z-scores of Purchase Amounts')
                plt.xlabel('Index')
                plt.ylabel('Z-score')
                plt.legend()

                # Show the plot in Streamlit
                st.pyplot(plt)

        elif level1_option == 'Q3: Top three product categories based on purchases':
            top_categories = df['Product Category'].value_counts().head(3)

            # Create two columns in Streamlit
            col1, col2 = st.columns(2)

            # Display top categories in the first column
            with col1:
                st.subheader("Top 3 Product Categories")
                for category, count in top_categories.items():
                    st.write(f"{category}: {count} purchases")

            # Plotting the top 3 categories in the second column
            with col2:
                st.subheader("Top 3 Product Categories by Number of Purchases")

                # Create a bar plot
                plt.figure(figsize=(8, 6))
                bars = top_categories.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])

                # Adding titles and labels
                plt.title('Top 3 Product Categories by Number of Purchases', fontsize=14)
                plt.xlabel('Product Categories', fontsize=12)
                plt.ylabel('Number of Purchases', fontsize=12)

                # Adding the count values on top of each bar
                for index, value in enumerate(top_categories):
                    plt.text(index, value, str(value), ha='center', va='bottom', fontsize=10)

                # Show the plot in Streamlit
                st.pyplot(plt)

        elif level1_option == 'Q4: How many customers are classified as return customers?':

            total_customers = df['Return Customer'].count()

            # Counting the number of return customers
            return_customers = df['Return Customer'].sum()

            # Calculating the percentage of return customers
            return_customer_percentage = (return_customers / total_customers) * 100

            # Filter return customers
            return_customers_df = df[df['Return Customer'] == 1]

            # Group by Product Category and count return customers, then sort in descending order
            return_customers_summary = return_customers_df.groupby(['Product Category']).size().reset_index(
                name='Return Count')

            total_purchases_summary = df.groupby(['Product Category']).size().reset_index(name='Total Purchases')

            comparison_summary = pd.merge(total_purchases_summary, return_customers_summary, on='Product Category',
                                          how='left')
            comparison_summary['Return Count'].fillna(0, inplace=True)
            comparison_summary['Return Rate (%)'] = (comparison_summary['Return Count'] / comparison_summary[
                'Total Purchases']) * 100
            comparison_summary = comparison_summary.sort_values(by='Return Rate (%)', ascending=False)

            # Age Range Analysis
            age_bins = [0, 18, 25, 35, 45, 60, 100]
            age_labels = ['<18', '18-25', '26-35', '36-45', '46-60', '60+']
            return_customers_df['Age Range'] = pd.cut(return_customers_df['Age'], bins=age_bins, labels=age_labels,
                                                      right=False)

            age_gender_return_summary = return_customers_df.groupby(['Age Range', 'Gender']).size().reset_index(
                name='Count')
            age_gender_return_summary = age_gender_return_summary.sort_values(by='Count', ascending=False)

            # Create a 2x2 grid layout in Streamlit
            col1, col2 = st.columns(2)

            # Display the number of return customers in the first column
            with col1:
                st.subheader("Number of Return Customers")
                st.write(return_customers)

            # Display the percentage of return customers in the second column
            with col2:
                st.subheader("Percentage of Return Customers")
                st.write(f"{return_customer_percentage:.2f}%")

            # Create a new row for the visualizations
            col3, col4 = st.columns(2)

            # Plotting the return rate by product category in the third column
            with col3:
                st.subheader("Return Rate by Product Category")

                # Data for visualization: Product Category and Return Rate
                categories = comparison_summary['Product Category']
                return_rates = comparison_summary['Return Rate (%)']

                # Create a horizontal bar chart
                plt.figure(figsize=(10, 6))
                plt.barh(categories, return_rates, color='#4c72b0')

                # Add title and labels
                plt.title('Return Rate by Product Category', fontsize=16)
                plt.xlabel('Return Rate (%)', fontsize=12)
                plt.ylabel('Product Category', fontsize=12)

                # Add value labels to each bar
                for index, value in enumerate(return_rates):
                    plt.text(value + 0.5, index, f'{value:.2f}%', va='center', fontsize=10)

                # Show the chart in Streamlit
                plt.tight_layout()
                st.pyplot(plt)

            # Display the summary of return customers in the fourth column
            with col4:
                st.subheader("Return Customers Summary")
                st.dataframe(return_customers_summary)

            # New row for Age Range and Gender Analysis
            st.subheader("Return Customers by Age Range and Gender")

            # Set up the plot style for age range analysis
            sns.set(style="whitegrid")

            # Create the grouped bar plot for age and gender
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Age Range', y='Count', hue='Gender', data=age_gender_return_summary, palette='Set2')

            # Add title and labels
            plt.title('Return Customers by Age Range and Gender', fontsize=16)
            plt.xlabel('Age Range', fontsize=12)
            plt.ylabel('Count of Return Customers', fontsize=12)

            # Show the chart in Streamlit
            plt.tight_layout()
            st.pyplot(plt)


        elif level1_option == 'Q5: Average review score given by customers':

            # Calculate the average review score
            average_review_score = df['Review Score (1-5)'].mean()

            # Group by Product Category and calculate average review score
            average_review_by_product = df.groupby(['Product Category'])['Review Score (1-5)'].mean().reset_index()
            average_review_by_product.columns = ['Product Category', 'Average Review Score']

            # Define threshold for low average review scores
            low_average_review_threshold = 3
            low_average_review_products = average_review_by_product[
                average_review_by_product['Average Review Score'] <= low_average_review_threshold]

            # Count total reviews by product category
            reviews_count_by_product = df.groupby(['Product Category']).size().reset_index(name='Total Reviews')

            # Merge the two summaries for comparison
            comparison_summary = pd.merge(reviews_count_by_product, average_review_by_product, on='Product Category',
                                          how='left')
            comparison_summary = comparison_summary.sort_values(by='Total Reviews', ascending=True)

            # Streamlit layout
            st.title("Product Review Analysis")

            # Create two columns for displaying metrics
            col1, col2 = st.columns(2)

            # Display average review score
            with col1:
                st.subheader("Average Review Score")
                st.write(f"{average_review_score:.2f}")

            # Display products with low average review scores
            with col2:
                st.subheader("Products with Low Average Review Scores")
                st.dataframe(low_average_review_products)

            # Create a row for the total reviews count by product category
            st.subheader("Total Reviews Count by Product Category")
            st.dataframe(reviews_count_by_product)

            # Create a new section for visualizations
            st.subheader("Visualizations")

            # 1. Pie chart for distribution of total reviews by product category
            st.subheader("Distribution of Total Reviews by Product Category")

            fig1, ax1 = plt.subplots(figsize=(10, 8))
            ax1.pie(comparison_summary['Total Reviews'],
                    labels=comparison_summary['Product Category'],
                    autopct='%1.1f%%',
                    startangle=140,
                    colors=plt.cm.tab20.colors)
            ax1.set_title('Distribution of Total Reviews by Product Category', fontsize=16)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig1)

            # 2. Horizontal bar plot for total reviews and average review scores
            st.subheader("Total Reviews and Average Review Scores by Product Category")

            fig2, ax2 = plt.subplots(figsize=(12, 8))

            bar_width = 0.35
            index = np.arange(len(comparison_summary['Product Category']))

            colors_total_reviews = plt.cm.Blues(np.linspace(0.3, 1, len(comparison_summary)))
            colors_avg_review_score = plt.cm.Greens(np.linspace(0.3, 1, len(comparison_summary)))

            bars1 = ax2.barh(index, comparison_summary['Total Reviews'], bar_width, label='Total Reviews',
                             color=colors_total_reviews)
            bars2 = ax2.barh(index + bar_width, comparison_summary['Average Review Score'], bar_width,
                             label='Average Review Score', color=colors_avg_review_score)

            ax2.set_ylabel('Product Categories', fontsize=12)
            ax2.set_xlabel('Count / Score', fontsize=12)
            ax2.set_title('Total Reviews and Average Review Scores by Product Category', fontsize=16)

            ax2.set_yticks(index + bar_width / 2)
            ax2.set_yticklabels(comparison_summary['Product Category'])

            ax2.legend()

            for bar in bars1:
                xval = bar.get_width()
                ax2.text(xval, bar.get_y() + bar.get_height() / 2, int(xval), va='center', ha='left', color='black')

            for bar in bars2:
                xval = bar.get_width()
                ax2.text(xval, bar.get_y() + bar.get_height() / 2, f'{xval:.1f}', va='center', ha='left', color='black')

            # Show the bar plot in Streamlit
            plt.tight_layout()
            st.pyplot(fig2)


        elif level1_option == 'Q6: Average delivery time by subscription status (Free, Premium)':

            # Calculate average delivery time based on subscription status
            avg_delivery_time = df.groupby('Subscription Status')['Delivery Time (days)'].mean()

            # Reset the index for easier plotting
            avg_delivery_time_df = avg_delivery_time.reset_index()

            # Streamlit layout
            st.title("Delivery Time Analysis")

            # Description of the analysis
            st.write(
                "This analysis shows the average delivery time based on subscription status. The bar plot visualizes the differences in delivery times for various subscription levels.")

            # Create two columns for displaying metrics and plots
            col1, col2 = st.columns(2)

            # Display average delivery time in the first column
            with col1:
                st.subheader("Average Delivery Time by Subscription Status")
                st.dataframe(avg_delivery_time_df)

            # Create the bar plot in the second column
            with col2:
                st.subheader("Bar Plot of Average Delivery Time")

                # Set up the plot style
                sns.set(style="whitegrid")

                # Create the bar plot
                plt.figure(figsize=(8, 5))
                sns.barplot(x='Subscription Status', y='Delivery Time (days)', data=avg_delivery_time_df,
                            palette='muted')

                # Add title and labels
                plt.title('Average Delivery Time by Subscription Status', fontsize=16)
                plt.xlabel('Subscription Status', fontsize=12)
                plt.ylabel('Average Delivery Time (days)', fontsize=12)

                # Show the plot in Streamlit
                plt.tight_layout()
                st.pyplot(plt)



        elif level1_option == 'Q7: Number of customers subscribed to the service':
            subscribed_customers = df['Subscription Status'].notna().sum()  # Count of non-null subscription statuses
            unsubscribed_customers = df.shape[0] - subscribed_customers  # Total customers - subscribed customers

            # Streamlit layout
            st.title("Subscription Status Analysis")

            # Display the number of subscribed customers
            st.write(f"Number of Subscribed Customers: {subscribed_customers}")
            st.write(f"Number of Unsubscribed Customers: {unsubscribed_customers}")

            # Create a pie chart
            labels = ['Subscribed Customers', 'Unsubscribed Customers']
            sizes = [subscribed_customers, unsubscribed_customers]
            colors = ['lightcoral', 'lightgreen']
            explode = (0.1, 0)  # explode the first slice

            # Create the pie chart using Matplotlib
            plt.figure(figsize=(8, 5))
            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True, startangle=140)
            plt.title('Subscription Status Distribution')
            plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.

            # Show the plot in Streamlit
            st.pyplot(plt)

        elif level1_option == 'Q8: Percentage of customers using different devices (Mobile, Desktop, Tablet)':
            device_usage_percentage = df['Device Type'].value_counts(normalize=True) * 100

            # Streamlit layout
            st.title("Device Usage Analysis")

            # Create two columns for displaying metrics and plots
            col1, col2 = st.columns(2)

            # Display device usage percentage in the first column
            with col1:
                st.subheader("Device Usage Percentage")
                st.write(device_usage_percentage)

            # Create the pie chart in the second column
            with col2:
                st.subheader("Pie Chart of Device Usage Percentage")

                # Create the pie chart
                plt.figure(figsize=(7, 7))
                plt.pie(device_usage_percentage, labels=device_usage_percentage.index,
                        autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
                plt.title('Device Usage Percentage')
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

                # Show the plot in Streamlit
                st.pyplot(plt)


        elif level1_option == 'Q9: Average purchase amount with and without discounts':
            avg_purchase_discount = df.groupby('Discount Availed')['Purchase Amount ($)'].mean()

            # Streamlit layout
            st.title("Average Purchase Amount Analysis")

            # Create two columns for displaying metrics and plots
            col1, col2 = st.columns(2)

            # Display average purchase amount by discount status in the first column
            with col1:
                st.subheader("Average Purchase Amount by Discount Status")
                st.write(avg_purchase_discount)

            # Create the bar plot in the second column
            with col2:
                st.subheader("Bar Plot of Average Purchase Amount")

                # Visualization
                plt.figure(figsize=(7, 5))
                sns.barplot(x=avg_purchase_discount.index, y=avg_purchase_discount.values, palette='Set2')
                plt.title('Average Purchase Amount by Discount Status')
                plt.ylabel('Average Purchase Amount ($)')
                plt.xlabel('Discount Availed (0 = No, 1 = Yes)')

                # Show the plot in Streamlit
                st.pyplot(plt)

        elif level1_option == 'Q10: Most common payment method used by customers':
            payment_method_counts = df['Payment Method'].value_counts()

            # Find the most common payment method
            most_common_payment_method = df['Payment Method'].mode()[0]

            # Streamlit layout
            st.title("Payment Method Analysis")

            # Create two columns for displaying metrics and plots
            col1, col2 = st.columns(2)

            # Display the most common payment method in the first column
            with col1:
                st.subheader("Most Common Payment Method")
                st.write(f"Most Common Payment Method: {most_common_payment_method}")

            # Create the bar plot in the second column
            with col2:
                st.subheader("Payment Method Distribution")

                # Bar chart for payment method distribution
                plt.figure(figsize=(8, 6))
                sns.barplot(x=payment_method_counts.index, y=payment_method_counts.values, palette='Set3')
                plt.title('Payment Method Distribution')
                plt.ylabel('Number of Users')
                plt.xlabel('Payment Method')

                # Show the plot in Streamlit
                st.pyplot(plt)


    # Level 2: Intermediate Insights
    elif level == 'Level 2: Intermediate Insights':
        st.subheader("Level 2: Intermediate Insights")
        level2_option = st.sidebar.selectbox('Choose a Question',
                                             ['Q1: Average review scores of users of the most common payment method',
                                              'Q2: Correlation between time on site and purchase amount',
                                              'Q3: Percentage of satisfied (rating 4-5) return customers',
                                              'Q4: Relationship between number of items purchased and satisfaction',
                                              'Q5: Location with 2nd highest average purchase amount'])
        if level2_option == 'Q1: Average review scores of users of the most common payment method':
            plot_reviews_by_payment_method(df)
            most_common_payment_method = df['Payment Method'].mode()[0]
            average_review_score = df[df['Payment Method'] == most_common_payment_method]['Review Score (1-5)'].mean()

            # Age distribution of Bank Transfer users
            bank_transfer_users = df[df['Payment Method'] == 'Bank Transfer']
            bins = range(10, 81, 10)
            labels = [f"{i}-{i + 9}" for i in bins[:-1]]
            bank_transfer_users['Age Group'] = pd.cut(bank_transfer_users['Age'], bins=bins, labels=labels, right=False)
            age_group_counts = bank_transfer_users['Age Group'].value_counts().sort_index()

            # Payment methods used by customers aged 10-19
            age_filtered_users = df[(df['Age'] >= 10) & (df['Age'] <= 19)]
            payment_method_counts = age_filtered_users['Payment Method'].value_counts()

            # Distribution of users by location
            location_counts = df['Location'].value_counts()

            # Locations of interest for pie charts
            locations_of_interest = ['Dhaka', 'Sylhet', 'Barisal']

            # Streamlit layout: create two rows and columns for visuals
            st.write("### Dashboard: Payment Method Insights")

            # First row: Most common payment method and average review score
            col1, col2 = st.columns(2)

            with col1:
                st.write(f"### Most Common Payment Method: {most_common_payment_method}")
                st.write(f"### Average Review Score: {average_review_score:.2f}")

            with col2:
                plt.figure(figsize=(6, 4))
                sns.barplot(x=[most_common_payment_method], y=[average_review_score], palette='Blues_d')
                plt.title(f'Average Review Score for {most_common_payment_method}', fontsize=14)
                plt.xlabel('Payment Method', fontsize=12)
                plt.ylabel('Average Review Score', fontsize=12)
                plt.text(0, average_review_score, f'{average_review_score:.2f}', ha='center', va='bottom', fontsize=12)
                plt.tight_layout()
                st.pyplot(plt)

            # Second row: Age distribution of Bank Transfer users and payment methods used by customers aged 10-19
            col3, col4 = st.columns(2)

            with col3:
                st.write("### Age Distribution of Bank Transfer Users")
                st.write(
                    "This chart shows the number of users grouped by age who use 'Bank Transfer' as a payment method.")

                plt.figure(figsize=(6, 4))
                age_group_counts.plot(kind='bar', color='skyblue')
                plt.title('Number of Bank Transfer Users by Age Group')
                plt.xlabel('Age Group')
                plt.ylabel('Number of Users')
                plt.xticks(rotation=45)
                st.pyplot(plt)

            with col4:
                st.write("### Payment Methods Used by Customers Aged 10-19")
                st.write("This bar chart visualizes the different payment methods used by customers aged 10-19.")

                plt.figure(figsize=(6, 4))
                payment_method_counts.plot(kind='bar', color='lightblue')
                plt.title('Payment Methods Used by Customers Aged 10-19')
                plt.xlabel('Payment Method')
                plt.ylabel('Number of Users')
                plt.xticks(rotation=45)
                st.pyplot(plt)

            # Distribution of users by location (First figure)
            st.write("### Number of Users by Location")
            plt.figure(figsize=(10, 6))
            location_counts.plot(kind='bar', color='lightcoral')
            plt.title('Number of Users by Location')
            plt.xlabel('Location')
            plt.ylabel('Number of Users')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(plt)

            # Second figure: Pie charts for payment methods by selected locations
            st.write("### Payment Methods by Location")
            st.write("The following pie charts show the payment methods used in Dhaka, Sylhet, and Barisal.")

            fig, axes = plt.subplots(1, len(locations_of_interest), figsize=(18, 6))

            for ax, location in zip(axes, locations_of_interest):
                # Filter users by location
                filtered_users = df[df['Location'] == location]

                # Count payment methods for that location
                payment_method_counts = filtered_users['Payment Method'].value_counts()

                # Pie chart for each location
                ax.pie(payment_method_counts, labels=payment_method_counts.index, autopct='%1.1f%%', startangle=90,
                       colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
                ax.set_title(f'Payment Methods Used in {location}')
                ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle

            plt.tight_layout()
            st.pyplot(fig)

        elif level2_option == 'Q2: Correlation between time on site and purchase amount':
            bins = list(range(0, 76, 2))
            labels = [f'{bins[i]}-{bins[i + 1]}' for i in range(len(bins) - 1)]
            df['Time Bins'] = pd.cut(df['Time Spent on Website (min)'], bins=bins, labels=labels, right=False)

            # Aggregating data for plotting directly from the existing 'df'
            df_grouped = df.groupby('Time Bins').agg({
                'Purchase Amount ($)': 'mean',
                'Number of Items Purchased': 'mean'
            }).reset_index()

            # Streamlit layout: 2 rows, 1 column
            st.write("### Dashboard: Time Spent on Website Insights")

            # First Row: Line plots for Average Purchase Amount and Number of Items Purchased
            st.write("#### Time Spent on Website vs Purchase Behavior")
            st.write(
                "This section explores the relationship between the time users spend on the website and their purchasing behavior. "
                "The line charts display the average purchase amount and the average number of items purchased, segmented by "
                "time spent on the website. Understanding these patterns can help in optimizing the user experience and "
                "increasing sales."
            )

            plt.figure(figsize=(16, 10))

            # Subplot 1: Average Purchase Amount by Time Spent on Website
            plt.subplot(2, 1, 1)
            sns.lineplot(data=df_grouped, x='Time Bins', y='Purchase Amount ($)', marker='o', color='blue')
            plt.title('Average Purchase Amount by Time Spent on Website')
            plt.xlabel('Time Spent on Website (min)')
            plt.ylabel('Average Purchase Amount ($)')
            plt.xticks(rotation=45)
            plt.ylim(450, 600)

            # Subplot 2: Average Number of Items Purchased by Time Spent on Website
            plt.subplot(2, 1, 2)
            sns.lineplot(data=df_grouped, x='Time Bins', y='Number of Items Purchased', marker='o', color='green')
            plt.title('Average Number of Items Purchased by Time Spent on Website')
            plt.xlabel('Time Spent on Website (min)')
            plt.ylabel('Average Number of Items Purchased')
            plt.xticks(rotation=45)
            plt.ylim(4, df_grouped['Number of Items Purchased'].max() * 1.1)

            plt.tight_layout()
            st.pyplot(plt)

            # Second Row: Correlation analysis
            st.write("#### Correlation Analysis")
            st.write(
                "In this section, we examine the correlation between the time spent on the website and two key metrics: "
                "the purchase amount and the number of items purchased. A strong positive correlation would suggest that "
                "longer time spent on the website leads to higher purchase amounts and more items bought, indicating a potential "
                "for targeted marketing strategies."
            )

            # Calculate correlation between time spent and purchase amount/items directly
            correlation_time_purchase = df[['Time Spent on Website (min)', 'Purchase Amount ($)']].corr().iloc[0, 1]
            correlation_time_items = df[['Time Spent on Website (min)', 'Number of Items Purchased']].corr().iloc[0, 1]

            # Display the correlation results
            st.write(
                f"Correlation between time spent on website and purchase amount: **{correlation_time_purchase:.2f}**")
            st.write(
                f"Correlation between time spent on website and number of items purchased: **{correlation_time_items:.2f}**")

        elif level2_option == 'Q3: Percentage of satisfied (rating 4-5) return customers':
            satisfied_return_customers = df[(df['Review Score (1-5)'] >= 4) & (df['Return Customer'] == True)].shape[0]

            # Calculate the total number of return customers
            total_return_customers = df[df['Return Customer'] == True].shape[0]

            # Calculate the percentage of satisfied return customers
            if total_return_customers > 0:
                percentage_satisfied_return_customers = (satisfied_return_customers / total_return_customers) * 100
            else:
                percentage_satisfied_return_customers = 0  # Avoid division by zero

            # Display the result in Streamlit
            st.title("Customer Satisfaction Dashboard")
            st.write(f"Percentage of satisfied return customers: **{percentage_satisfied_return_customers:.2f}%**")

        elif level2_option == 'Q4: Relationship between number of items purchased and satisfaction':
            # Calculate average items purchased based on customer satisfaction
            average_items_per_satisfaction = df.groupby('Customer Satisfaction')['Number of Items Purchased'].mean()

            # Display the average items purchased
            st.write("Average number of items purchased based on customer satisfaction:")
            st.write(average_items_per_satisfaction)

            # Plotting
            plt.figure(figsize=(8, 5))
            sns.barplot(x=average_items_per_satisfaction.index, y=average_items_per_satisfaction.values)
            plt.title('Relationship between Customer Satisfaction and Number of Items Purchased')
            plt.xlabel('Customer Satisfaction')
            plt.ylabel('Average Number of Items Purchased')

            # Display the plot in Streamlit
            st.pyplot(plt)


        elif level2_option == 'Q5: Location with 2nd highest average purchase amount':
            average_purchase_by_location = df.groupby('Location')['Purchase Amount ($)'].mean()

            # Get the location with the second highest average purchase amount
            sorted_average_purchase = average_purchase_by_location.sort_values(ascending=False)
            second_highest_location = sorted_average_purchase.index[1]
            second_highest_avg_purchase = sorted_average_purchase.iloc[1]

            # Display the result
            st.write(
                f"The location with the 2nd highest average purchase amount is **{second_highest_location}** with an average of **${second_highest_avg_purchase:.2f}**.")

            # Plotting
            plt.figure(figsize=(10, 6))
            sns.barplot(x=sorted_average_purchase.index, y=sorted_average_purchase.values, palette='viridis')
            plt.axhline(y=second_highest_avg_purchase, color='r', linestyle='--', label='2nd Highest Average Purchase')
            plt.title('Average Purchase Amount by Location')
            plt.xlabel('Location')
            plt.ylabel('Average Purchase Amount ($)')
            plt.xticks(rotation=45)
            plt.legend()

            # Display the plot in Streamlit
            st.pyplot(plt)

    # Level 3: Critical Thinking Insights
    elif level == 'Level 3: Critical Thinking Insights':
        st.subheader("Level 3: Critical Thinking Insights")
        level3_option = st.sidebar.selectbox('Choose a Question',
                                             ['Q1: Factors contributing to being classified as a return customer',
                                              'Q2: How payment methods influence customer satisfaction and return rates',
                                              'Q3: How location influences both purchase amount and delivery time',
                                              'Q4: Major insights with explanation'])
        if level3_option == 'Q1: Factors contributing to being classified as a return customer':
            # Implement logic for critical thinking question
            st.write("Analyze various features that contribute to a customer being classified as a return customer.")

        elif level3_option == 'Q2: How payment methods influence customer satisfaction and return rates':
            df['Return Customer'] = df['Return Customer'].astype(int)

            # Calculate return rate by payment method
            return_rate_by_payment = df.groupby('Payment Method')['Return Customer'].mean().reset_index()
            return_rate_by_payment['Return Rate (%)'] = return_rate_by_payment['Return Customer'] * 100
            return_rate_by_payment = return_rate_by_payment.sort_values(by='Return Rate (%)', ascending=False)

            # Calculate satisfaction by payment method (example calculation)
            satisfaction_by_payment = df.groupby('Payment Method')['Review Score (1-5)'].mean().reset_index()

            # Combine data
            combined_data = pd.merge(satisfaction_by_payment, return_rate_by_payment, on='Payment Method')

            # Create the combined plot
            fig, ax1 = plt.subplots(figsize=(10, 6))  # Adjust the size as needed

            # Bar plot for average review score
            sns.barplot(x='Payment Method', y='Review Score (1-5)', data=combined_data, ax=ax1, palette='viridis')
            ax1.set_ylabel('Average Review Score (1-5)', fontsize=12)
            ax1.set_title('Customer Satisfaction and Return Rate by Payment Method', fontsize=16)

            # Line plot for return rate
            ax2 = ax1.twinx()
            sns.lineplot(x='Payment Method', y='Return Rate (%)', data=combined_data, ax=ax2, color='red', marker='o',
                         label='Return Rate (%)')
            ax2.set_ylabel('Return Rate (%)', fontsize=12)
            ax2.legend(loc='upper right')

            plt.xticks(rotation=45)
            plt.tight_layout()

            # Display the description for the plot
            st.write("""
            ### Customer Satisfaction and Return Rate Analysis
            This plot illustrates the average review scores of customers based on their chosen payment methods, alongside the corresponding return rates. 
            The bar chart represents customer satisfaction, while the line graph indicates the percentage of return customers.
            """)

            # Display the combined plot in Streamlit
            st.pyplot(fig)

        elif level3_option == 'Q3: How location influences both purchase amount and delivery time':
            # Assuming 'df' is already defined in your environment with required columns
            location_data = df.groupby('Location').agg({
                'Purchase Amount ($)': 'mean',
                'Delivery Time (days)': 'mean'
            }).reset_index()

            # Display the location data in Streamlit
            st.write("### Average Purchase Amount and Delivery Time by Location")
            st.dataframe(location_data)

            # Calculate correlation
            correlation = location_data['Purchase Amount ($)'].corr(location_data['Delivery Time (days)'])
            st.write(f"Correlation between Average Purchase Amount and Delivery Time: {correlation:.2f}")

            # Create the plots
            fig, axs = plt.subplots(1, 2, figsize=(14, 6))

            # Plot Average Purchase Amount by Location
            sns.barplot(x='Location', y='Purchase Amount ($)', data=location_data, palette='Blues_d', ax=axs[0])
            axs[0].set_title('Average Purchase Amount by Location')
            axs[0].set_xticklabels(axs[0].get_xticks(), rotation=45)
            axs[0].set_ylabel('Average Purchase Amount ($)')

            # Plot Average Delivery Time by Location
            sns.barplot(x='Location', y='Delivery Time (days)', data=location_data, palette='Greens_d', ax=axs[1])
            axs[1].set_title('Average Delivery Time by Location')
            axs[1].set_xticklabels(axs[1].get_xticks(), rotation=45)
            axs[1].set_ylabel('Average Delivery Time (days)')

            # Adjust layout
            plt.tight_layout()

            # Display the plots in Streamlit
            st.pyplot(fig)

        elif level3_option == 'Q4: Major insights with explanation':
            data = {
                'Gender': ['Male', 'Female', 'Other'],
                'Count': [450, 350, 100]
            }

            labels = data['Gender']
            sizes = data['Count']
            colors = ['#ff9999', '#66b3ff', '#99ff99']  # Define colors for each section

            # Create the pie chart with a smaller figure size
            plt.figure(figsize=(3, 3))  # Further reduced figure size
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors,
                    explode=(0.05, 0.05, 0.05), shadow=True)

            plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
            plt.title('Gender Distribution of Customers', fontsize=10)  # Smaller title font size

            # Display the pie chart in Streamlit
            st.pyplot(plt)

            # Description for the pie chart with smaller text
            description = """
            ### Gender Distribution of Customers

            This pie chart illustrates the distribution of customers based on gender. The chart shows that **Male** customers constitute the largest group at **450** individuals, followed by **Female** customers with **350**, and **Other** gender identities, totaling **100**. The percentages displayed highlight the proportional representation of each gender within the customer base, providing valuable insights into the demographic composition.
            """

            # Display the description in Streamlit
            st.markdown(description)

# Function to plot average review scores and count of reviews by payment method
def plot_reviews_by_payment_method(df):
    avg_reviews_by_payment = df.groupby('Payment Method')['Review Score (1-5)'].mean()
    count_reviews_by_payment = df.groupby('Payment Method')['Review Score (1-5)'].count()

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:blue'
    ax1.set_xlabel('Payment Method')
    ax1.set_ylabel('Average Review Score (1-5)', color=color)
    avg_reviews_by_payment.plot(kind='bar', color=color, ax=ax1, position=1, width=0.4)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 5)

    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('Count of Reviews', color=color)
    count_reviews_by_payment.plot(kind='bar', color=color, ax=ax2, position=0, width=0.4)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Average Review Scores and Count of Reviews by Payment Method')
    plt.xticks(rotation=45)
    st.pyplot(fig)

if __name__ == "__main__":
    main()