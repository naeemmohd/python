import time
# Get EPOC time
theTime = time.time()
print('EPOC time: ' + str(theTime))

# Get Local time
theLocalTime = time.localtime(theTime)
print('Local time: ' + str(theLocalTime))

# Get Formatted time
theFormattedLocalTime = time.asctime(theLocalTime)
print('Formatted Local Current time: ' + str(theFormattedLocalTime))

import calendar
print(calendar.month(2019, 1))