'Advanced Data Visualization with Pandas and Matplotlib'

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def main():
    """
    Main function to perform data visualization tasks on the given dataset.

    Steps:
      1. Load the dataset into a pandas DataFrame.
      2. Perform data preprocessing tasks, such as handling missing values, encoding categorical variables, and feature scaling.
      3. Utilize pandas to create a pivot table for summarizing the data.
      4. Generate a box plot to compare the distributions of multiple variables across different categories.
      5. Create a stacked area chart to visualize the composition of different variables over time.
      6. Develop a heat map to display the correlation matrix of the numerical variables.
      7. Combine multiple visualizations into a dashboard-like layout using Matplotlib's subplots.
      8. Save the final visualization dashboard as a PDF document.

    Returns:
        None
    """
    # Step 1: Load the dataset into a pandas DataFrame
    df = pd.read_csv("E:\\Heel Internship\\ML-Internship\\10-06-24\\Datasets\\Task4\\country_vaccinations.csv")

    # Step 2: Data preprocessing
    # Handle missing values
    df.fillna(0, inplace=True)  # Replace missing values with 0 for simplicity

    # Step 3: Create a pivot table
    pivot_table = pd.pivot_table(df, index='country', values=['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'], aggfunc='sum')

    # Step 4: Generate a box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df[['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']])
    plt.title('Boxplot of Vaccination Variables')
    plt.xlabel('Variables')
    plt.ylabel('Values')
    plt.show()

    # Step 5: Create a stacked area chart
    plt.figure(figsize=(10, 6))
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df[['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']].plot(kind='area', stacked=True)
    plt.title('Stacked Area Chart of Vaccination Variables Over Time')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.show()

    # Step 6: Develop a heat map
    plt.figure(figsize=(10, 6))
    numeric_df = df.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of Numerical Variables')
    plt.show()

    # Step 7: Combine multiple visualizations into a dashboard-like layout using Matplotlib's subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Box plot
    sns.boxplot(data=df[['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']], ax=axes[0, 0])
    axes[0, 0].set_title('Boxplot of Vaccination Variables')

    # Stacked area chart
    df[['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']].plot(kind='area', stacked=True, ax=axes[0, 1])
    axes[0, 1].set_title('Stacked Area Chart of Vaccination Variables Over Time')

    # Heat map
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=axes[1, 0])
    axes[1, 0].set_title('Correlation Heatmap of Numerical Variables')

    # Remove empty subplot
    fig.delaxes(axes[1, 1])

    plt.tight_layout()
    plt.show()

    # Step 8: Save the final visualization dashboard as a PDF document
    fig.savefig("Task4_visualization_dashboard.pdf")


if __name__ =="__main__":
    main()