import pandas as pd

def main():
    # Load data from CSV
    data = pd.read_csv('data.csv')
    # Process data
    result = data.describe()
    # Save result to JSON
    result.to_json('result.json')

if __name__ == '__main__':
    main()