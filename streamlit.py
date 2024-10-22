import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Load data
df = pd.read_csv("ecommerce_customer_behavior_dataset.csv")


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


# Function to plot bank transfer users by location
def plot_bank_transfer_users_by_location(df):
    bank_transfer_users = df[df['Payment Method'] == 'Bank Transfer']
    location_counts = bank_transfer_users['Location'].value_counts()

    plt.figure(figsize=(10, 6))
    location_counts.plot(kind='bar', color='lightgreen')
    plt.title('Number of Bank Transfer Users by Location')
    plt.xlabel('Location')
    plt.ylabel('Number of Users')
    plt.xticks(rotation=45)
    st.pyplot(plt)


# Function to plot payment method distribution by locations of interest
def plot_payment_method_distribution_by_location(df, locations_of_interest):
    fig, axes = plt.subplots(1, len(locations_of_interest), figsize=(18, 6))

    for ax, location in zip(axes, locations_of_interest):
        filtered_users = df[df['Location'] == location]
        payment_method_counts = filtered_users['Payment Method'].value_counts()

        ax.pie(payment_method_counts, labels=payment_method_counts.index, autopct='%1.1f%%', startangle=90,
               colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
        ax.set_title(f'Payment Methods Used in {location}')
        ax.axis('equal')

    plt.tight_layout()
    st.pyplot(fig)


# Streamlit Layout
def main():
    st.title('E-Commerce Data Analysis Dashboard')

    # Sidebar navigation
    st.sidebar.title('Navigation')
    level1 = st.sidebar.selectbox('Choose Visualization Level',
                                  ['Level 1: Payment Method Reviews', 'Level 2: Location-Specific Data'])

    # Level 1: Select the option
    if level1 == 'Level 1: Payment Method Reviews':
        level1_option = st.sidebar.selectbox('Choose Level 1 Visualization',
                                             ['Review Scores by Payment Method', 'Bank Transfer Users by Location'])
        if level1_option == 'Review Scores by Payment Method':
            plot_reviews_by_payment_method(df)
        elif level1_option == 'Bank Transfer Users by Location':
            plot_bank_transfer_users_by_location(df)

    # Level 2: Location-Specific Data
    elif level1 == 'Level 2: Location-Specific Data':
        locations_of_interest = st.sidebar.multiselect('Select Locations of Interest',
                                                       ['Dhaka', 'Sylhet', 'Barisal'])
        if locations_of_interest:
            plot_payment_method_distribution_by_location(df, locations_of_interest)


if __name__ == "__main__":
    main()
