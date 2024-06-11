'Data Visualization with Matplotlib'
import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
    Main function to perform data visualization tasks on the given dataset.

    Steps:
        1. Load the dataset from a CSV file into a pandas DataFrame.
        2. Create a line plot to visualize the trend of the 'Fare' variable over time.
        3. Generate a bar chart to compare the distribution of the 'Pclass' variable.
        4. Construct a scatter plot to examine the relationship between 'Age' and 'Fare'.
        5. Design a histogram to display the distribution of the 'Age' variable.
        6. Customize the visualizations by adding appropriate labels, titles, and legends.
        7. Save the generated plots as image files (PNG).

    Returns:
        None
    """
    # Step 1: Load the dataset into a pandas DataFram
    df = pd.read_csv("E:\\Heel Internship\\ML-Internship\\10-06-24\\Datasets\\Task3\\train.csv")
    
    # Step 2: Create a line plot to visualize the trend of a specific variable over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['PassengerId'], df['Fare'], label='Fare')
    plt.xlabel('Passenger ID')
    plt.ylabel('Fare')
    plt.title('Fare Trend Over Time')
    plt.legend()
    plt.savefig('Task3_line_plot.png')
    plt.show()

    # Step 3: Generate a bar chart to compare the distribution of a categorical variable
    plt.figure(figsize=(10, 6))
    df['Pclass'].value_counts().plot(kind='bar')
    plt.xlabel('Pclass')
    plt.ylabel('Count')
    plt.title('Distribution of Passenger Classes')
    plt.savefig('Task3_bar_chart.png')
    plt.show()

    # # Step 4: Construct a scatter plot to examine the relationship between two numerical variables
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Age'], df['Fare'], alpha=0.5)
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.title('Scatter Plot of Age vs Fare')
    plt.savefig('Task3_scatter_plot.png')
    plt.show()

    # # Step 5: Design a histogram to display the distribution of a continuous variable
    plt.figure(figsize=(10, 6))
    df['Age'].plot(kind='hist', bins=30, alpha=0.7)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Distribution of Age')
    plt.savefig('Task3_histogram.png')
    plt.show()

    # Step 6: Customize the visualizations by adding appropriate labels, titles, and legends
    # Note: Customizations have been added in the above steps
    
    # Step 7: Save the generated plots as image files (e.g., PNG, JPEG)
    # Note: Saving plots as images is already included in the above steps

if __name__ =="__main__":
    main()
