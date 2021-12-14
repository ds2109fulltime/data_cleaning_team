def Unix_to_UTC(unixdate):
    '''This Function transforms data in UNIX time format to UTC time format.
    Arguments: unixdate= Date in Unix format in interger type
    Unix time is a system for describing a point in time, it is the number of seconds that have elapsed since the Unix epoch.
    The Unix epoch is 00:00:00 UTC on 1 January 1970, IMPORTANT --> UNIX input has to have less than 11 digits'''
    import datetime
    int(unixdate)
    if unixdate == unixdate>10000000000:
        print('UNIX input has to have less than 11 digits')
    else:
        return datetime.datetime.utcfromtimestamp(unixdate).strftime('%Y-%m-%d:%H:%M')