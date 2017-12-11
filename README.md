# csv2csv

This is a small script that takes a .csv file and transforms it into a _different_ format based on some mappings.

## Instructions

1. Install Python 3 if needed.
2. Place your .csv file you wish to transform within the directory of this repo and name it `input.csv`.
3. Create another .csv file with the name of `new_headers.csv` in the following format.
   1. The first row are the headers desired for the transformed format.
   2. The second row are the corresponding names of the headers from the input .csv. If this is a new column with no data, just leave the value blank.
   3. Here is an example of [input.csv](input_example.csv) & [new_headers.csv](new_headers_example.csv)
4. `python main.py`
5. `open output.csv`
