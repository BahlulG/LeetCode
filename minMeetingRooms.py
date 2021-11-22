def minMeetingRooms(intervals):
    if not intervals:
        # if length of "intervals" is 0 (meaning if "intervals" list is empty), return nothing
        return

    rooms = 0
    available = 0
    curr = 0
    starts = []
    ends = []

    for interval in range(len(intervals)):
        starts.append(intervals[interval][0])
        ends.append(intervals[interval][1])

    starts, ends = sorted(starts), sorted(ends)
    # Sort both "starts" and "ends" lists

    for start in starts:
        while ends[curr] <= start:
            # In sorted "ends", if end is smaller or equal to start, it means we have one available room for another meeting. Because there's no time clash
            available += 1
            curr += 1
        if available:
            # here we check, if end is greater than start, then we will use on of the available rooms
            available -= 1
        else:
            # here check if end is greater than start and no available room, we need one more room for another meeting
            rooms += 1
    return rooms


intervals = [[0, 30], [5, 10], [15, 20]]
minMeetingRooms(intervals)
