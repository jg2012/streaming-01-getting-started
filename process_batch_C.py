"""
Batch Process C: Third transformation

Read from a file, transform, write to a new file.
In this case, covert degree K to degree F.

Note: 
This is a batch process, but the file objects we use are 
often called 'file-like objects' or 'streams'.
Streaming differs in that the input data is unbounded.

Use logging, very helpful when working with batch and streaming processes. 

"""

# Import from Python Standard Library

import csv
import logging

# Set up basic configuration for logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Declare program constants

INPUT_FILE_NAME = "batchfile_2_kelvin.csv"
OUTPUT_FILE_NAME = "batchfile_3_farenheit.csv"

# Define program functions (bits of reusable code)
# Use docstrings - and indentation matters!


def convert_k_to_f(temp_k):
    logging.debug(f"Calling convert_k_to_f() with {temp_k}.")
    farenheit = round(float(temp_k) * 9 / 5 - 459.67, 2)
    logging.debug(f"Converted {temp_k}K to {farenheit}F.")
    return farenheit


def process_rows(input_file_name, output_file_name):    
    """Read from input file, convert temperature, and write to output file."""
    logging.info(f"Calling process_rows(): {input_file_name} to {output_file_name}.")

    #Create a file boject for input(r = read access)
    with open(input_file_name, "r") as input_file:
        logging.info(f"Opened for reading: {input_file_name}.")
        #Create a CSV reader object
        reader = csv.reader(input_file, delimiter=",")

        header = next(reader)
        logging.info(f"Skipped header row: {header}")
    
        #Set the newline parameter to an empty string to avoid extra newlines in the output file
        with open(output_file_name, "w", newline="") as output_file:
            logging.info(f"Opened for writing: {output_file_name}.")
            #Create a CSV writer object
            writer = csv.writer(output_file, delimiter=",")

            #Write the header row to the output file 
            writer.writerow(["Year", "Month", "Day", "Time", "TempF"])

            #For each row in the input file, convert the temperature and write to the output file
            for row in reader:
                #Extract the values from the row
                Year, Month, Day, Time, TempK = row
                #Convert the temperature from Kelvin to Farenheit
                TempF = convert_k_to_f(TempK)
                #Write the row to the output file
                writer.writerow([Year, Month, Day, Time, TempF])

  
    


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting batch process C.")
        process_rows(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
        logging.info("Processing complete! Check for new file.")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
