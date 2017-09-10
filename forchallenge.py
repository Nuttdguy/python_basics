numberOfIpToEnter = int(input('How many IP addresses will you be entering?\n')) # get number of IP addresses to input into program
ipAddress = [i for i in range(numberOfIpToEnter)] # create an array of 'x' indices using i for in


for ip in ipAddress:
    ipAddress[ip] = input('%d: IP Address: ' % ip) # get IP Address from input and store into an array

    if (ipAddress[ip] == ''): # check if IP Address is empty
        print('IP Address is not valid.')
    else:

        segmentCount = 1 # set segment count to one
        checkFirstIdx = 0 #
        message = ''
        for ipSegment in ipAddress[ip]: # get character value

            if (ipSegment == '.' and checkFirstIdx >= 1): # check first indexl; does it contain an invalid start deliminator
                segmentCount += 1
            elif (checkFirstIdx == 0 and ipSegment == '.' ): # check first index only for '.'
                message = '{0} IP address is invalid'.format(ipAddress[ip])  # assign error message
                break # break loop, IP has an invalid start deliminator

            checkFirstIdx += 1

        if (message != ''): # if message is not empty, then print error
            print(message)
        else:
            print('{0} IP address has {1} segments'.format(ipAddress[ip], segmentCount)) # print number of segments if valid IP address

        # reset counters for next inputted IP address
        segmentCount = 1
        count = 0

print(ipAddress)