# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

#function that uses csv library to save data as a file
def save_csv (csvpath, data):
    csvpath = Path(csvpath)
    with open (csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in data:
         csvwriter.writerow(row)



# Loan Qualifier App

This is an app that takes users data and let them see what loans they are qualified for
---

## Technologies

Describe the technologies required to use your project such as programming languages, libraries, frameworks, and operating systems. Be sure to include the specific versions of any critical dependencies that you have used in the stable version of your project.
The project uses python 3.7 as a programming languages and uses different libraries such as sys, fire, questionary, and path. 
---

## Installation Guide

For this project, I had to install fire and questionary at the beginning. These were:
```python
pip install fire
pip install questionary
```
---

## Usage

Users can use this app through thier termina. For example, users can go to their Git Bash and do the following:
![screenshot of app.py usage in terminal]/c/Users/yasmi/challenge2pic.png)
---

## Contributors

Yasmin Sharbaf
Questions? Contact through linkedin:
[Yasmin Sharbaf Linkedin] (https://www.linkedin.com/in/yasmin-sharbaf)

---

## License

UC Berkeley Fintech Bootcamp