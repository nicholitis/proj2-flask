import arrow


utc = arrow.now('US/Pacific').format('DD-MMM')

if utc == '05-Oct':