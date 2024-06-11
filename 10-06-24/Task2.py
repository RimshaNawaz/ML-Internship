import numpy as np
'Numerical Analysis with NumPy'

def main():

    """
    This function performs the following steps:
            1. Load the dataset into a NumPy array.
            2. Calculate the mean, median, and standard deviation of the dataset.
            3. Normalize the data using the z-score normalization technique.
            4. Identify outliers in the dataset using the IQR (Interquartile Range) method.
            5. Perform element-wise mathematical operations on the dataset (e.g., addition, subtraction, multiplication).
            6. Reshape the dataset into a different dimension.
            7. Save the processed data as a NumPy binary file.
        
        Returns
        -------
        None
        
    """

    # Task 1: Load the dataset into a NumPy array
    dataset = np.genfromtxt("E:\\Heel Internship\\ML-Internship\\10-06-24\\Datasets\\Task2\\train.csv", delimiter=',', skip_header=1)
    print("Task 1 - Loaded Dataset:")

    # Task 2: Calculate the mean, median, and standard deviation of the dataset
    mean = np.mean(dataset)
    median = np.median(dataset)
    std_dev = np.std(dataset)
    print("\nTask 2 - Mean, Median, Standard Deviation:")
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)

    # Task 3: Normalize the data using the z-score normalization technique
    normalized_data = (dataset - mean) / std_dev
    print("\nTask 3 - Normalized Data:")
    print(normalized_data)

    # Task 4: Identify outliers in the dataset using the IQR (Interquartile Range) method
    q1 = np.percentile(dataset, 25)
    q3 = np.percentile(dataset, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = dataset[(dataset < lower_bound) | (dataset > upper_bound)]
    print("\nTask 4 - Outliers Identified using IQR Method:")
    print(outliers)

    # Task 5: Perform element-wise mathematical operations on the dataset
    # For example, addition, subtraction, and multiplication
    result_addition = dataset + 5
    result_subtraction = dataset - 2
    result_multiplication = dataset * 3
    print("\nTask 5 - Element-wise Mathematical Operations:")
    print("Addition Result:")
    print(result_addition)
    print("Subtraction Result:")
    print(result_subtraction)
    print("Multiplication Result:")
    print(result_multiplication)

    # Task 6: Reshape the dataset into a different dimension
    # For example, reshaping a 1D array into a 2D array
    new_shape = (dataset.shape[0], dataset.shape[1])
    reshaped_data = np.reshape(dataset, new_shape)
    print("\nTask 6 - Reshaped Dataset:")
    print(reshaped_data)

    # Task 7: Save the processed data as a NumPy binary file
    np.savez('Task2_processed_data.npz', mean=mean, median=median, std_dev=std_dev, normalized_data=normalized_data, outliers=outliers, result_addition=result_addition, result_subtraction=result_subtraction, result_multiplication=result_multiplication, reshaped_data=reshaped_data)
    print("\nTask 2_Processed Data Saved as 'Task2_processed_data.npz'")


if __name__ =="__main__":
    main()