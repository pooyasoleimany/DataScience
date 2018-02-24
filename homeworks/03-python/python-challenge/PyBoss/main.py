import sys
from datetime import datetime, time, date
# ## Option 3: PyBoss

# ![Boss](Images/boss.jpg)

# In this challenge, you get to be the _boss_. You oversee hundreds of employees across 
# the country developing Tuna 2.0, a world-changing snack food based on canned tuna 
# fish. Alas, being the boss isn't all fun, games, and self-adulation. The company 
# recently decided to purchase a new HR system, and unfortunately for you, the new 
# system requires employee records be stored completely differently.

# Your task is to help bridge the gap by creating a Python script able to convert your 
# employee records to the required format. Your script will need to do the following:

# * Import the `employee_data1.csv` and `employee_data2.csv` files, which currently 
#   holds employee records like the below:
# ```
# Emp ID,   Name,           DOB,        SSN,            State
# 214,      Sarah Simpson,  1985-12-04, 282-01-8166,    Florida
# 15,       Samantha Lara,  1993-09-08, 848-80-7526,    Colorado
# 411,      Stacy Charles,  1957-12-20, 658-75-8526,    Pennsylvania
# ```

# * Then convert and export the data to use the following format instead:
# ```
# Emp ID,   First Name,     Last Name,  DOB,        SSN,            State
# 214,      Sarah,          Simpson,    12/04/1985, ***-**-8166,    FL
# 15,       Samantha,       Lara,0      9/08/1993,  ***-**-7526,    CO
# 411,      Stacy,          Charles,    12/20/1957, ***-**-8526,    PA
# ```

class Converter:
    _us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
    # * In summary, the required conversions are as follows:

    #   * The `Name` column should be split into separate `First Name` and `Last Name` 
    #     columns.

    #   * The `DOB` data should be re-written into `DD/MM/YYYY` format.
    def reformat_date(self, date):
        return datetime.strptime(date, "%Y-%m-%d").strftime("%m/%d/%Y")

    #   * The `SSN` data should be re-written such that the first five numbers are 
    #     hidden from view.
    def obfuscate_ssn(self, ssn):
        return "***-**-{}".format(ssn.rpartition('-')[2])

    #   * The `State` data should be re-written as simple two-letter abbreviations.    
    # * Special Hint: You may find this link to be helpful—[Python Dictionary for State 
    #   Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).
    def get_state_abbrevation(self, state_name):
        return Converter._us_state_abbrev[state_name]

def Main():
    pass

import unittest
class TestConverter(unittest.TestCase):
    def test_obfuscate_ssn(self):
        self.assertEqual('***-**-1234',Converter().obfuscate_ssn('123-12-1234'))
    def test_get_state_abbrevation(self):
        self.assertEqual('CA',Converter().get_state_abbrevation('California'))
    def test_reformat_date(self):
        self.assertEqual('12/20/1957',Converter().reformat_date('1957-12-20'))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main()
    else:
        Main()