import pandas as pd

'Data Manipulation with pandas'

def main():

    """
    This function performs the following steps:
        1. Loads the dataset from a CSV file into a pandas DataFrame.
        2. Removes any duplicate rows or missing values from the DataFrame.
        3. Extracts a subset of relevant columns for the analysis.
        4. Calculates the total sales amount for each product line category.
        5. Identifies the top-selling product line by quantity ordered and its sales quantity.
        6. Generates a summary report with descriptive statistics for the numerical columns.
        7. Exports the cleaned and processed data to a new CSV file.
    
    Returns
    -------
    None
    """    
    # Step 1: Load the dataset into a pandas DataFrame
    df = pd.read_csv("E:\\Heel Internship\\ML-Internship\\10-06-24\\Datasets\\Task1\\sales_data_sample.csv", encoding='ISO-8859-1')

    # Step 2: Remove any duplicate rows or missing values
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)


    # Step 3: Extract a subset of columns that are relevant to the analysis
    relevant_columns = ['QUANTITYORDERED','PRICEEACH','SALES','PRODUCTLINE']
    df_subset = df[relevant_columns]

    # Step 4: Calculate the total sales amount for each category
    total_sales_per_category = df_subset.groupby('PRODUCTLINE')['SALES'].sum()

    # Step 5: Identify the top-selling product and its sales quantity
    total_quantity_per_product = df_subset.groupby('PRODUCTLINE')['QUANTITYORDERED'].sum()
    top_selling_product = total_quantity_per_product.idxmax()
    top_selling_product_quantity = total_quantity_per_product.max()

    # Step 6: Generate a summary report with descriptive statistics for numerical columns
    summary_report = df_subset.describe()
    print("\nSummary Report:")
    print(summary_report)


    # Step 7: Export the cleaned and processed data to a new CSV file
    df_subset.to_csv('Task1_Cleaned_sales_data.csv', index=False)

    # Output results
    print("Total Sales Amount per Category:")
    print(total_sales_per_category)
    print("\nTop Selling Product:", top_selling_product)
    print("Quantity Sold:", top_selling_product_quantity)
    print("\nSummary Report:")
    print(summary_report)


if __name__ =="__main__":
    main()