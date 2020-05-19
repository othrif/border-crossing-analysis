# Border Crossing Analysis

## Problem
The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land.

My task is two fold:
- calculate the total number of times vehicles, equipment, passengers and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders each month
- calculate the running monthly average of total number of crossings for that type of crossing and border

## Solution
I used a `namedtuple` instance to read the `CSV` file in `manipCSV.py` and populate a map that holds the number of crossings as a value and the tuple
`(Border, Date, Measure)` as key. Once I calculated the number of crossings. I pass this map to `analyze.py` that iterate through the latter to
find all months before the date of the border crossing in question and also calculates how many months in total.
This information is used to calculate the running average that is then passed back to the main program `border_analytics.py`.

I implemented the solution in the form of a python module with helper functions defined in `pyUtils` folder.

I tested with the `insight_testsuite` and passed.