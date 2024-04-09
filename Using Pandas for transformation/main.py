from extraction import import_data
from transformation import apply_cleaning
from load import load_cleaned_data, load_raw_data

def main():
    load_raw_data()
    load_cleaned_data()

if __name__ == "__main__":
    main()