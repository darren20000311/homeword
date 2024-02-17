def main():
    analysis_data = input("Please enter the file name: ")
    #follow the instructions, I use try to prevent the time that the user enter the wrong text.
    try:
        with open(analysis_data, 'r') as file:
            # I create an empty list to store the length of the data.
            data = [] 
            # because I want to read text only onece, so I use the more efficient way, which is readlines()
            for line in file.readlines():
                #.rstrip() can let me remove the white space.
                clean_line = line.rstrip() 
                data.append(clean_line) 
                # after it finished to read the text, i store them into the list that i have created earlier.
                total_minutes = len(data)
        # 1 hour = 60 minutes
        total_hours = total_minutes / 60
        #we need to calculate how many days the pump worked, so total_hour need to divided by 24(there are 24 hors per day).
        #we want it up by three because we don't want to have too many numbers after the decimal point.
        ONE_DAY_HOURS = 24
        ROUND_THREE = 3
        total_days = round(total_hours / ONE_DAY_HOURS, ROUND_THREE)

        # we started to calculate how long did the pump worked
        # in if block, the reason we need to int(i) > 1 is because when the number is bigger than 1 ,
        # it means that the pump is working
        time_consume = 0
        for i in data:
            if int(i) > 1:
                time_consume += 1
        #since it produces two gallons per minute, we need to multiply two.
        gallons_produced = time_consume * 2
        #we need to calculate how many gallons, so we need to multiply by 24 hours.
        gallons_per_day = gallons_produced * ONE_DAY_HOURS
        #this line is to calculate the total power, since the data in the file is not integer, I use int(j) to convert it.
        total_power = sum(int(j) for j in data)
        #And then I convertWatt minutes to kWh.
        total_power_kwh = total_power / 1000 / 60
        #This line, I strted to calculate when does it reach to 5 gallons.
        #First, i initialized when5 and index to 0 is because I want them to iterate in the while loop to count to over 2500 = 5 gallons
        when5 = 0
        index = 0
        five_gallons = 2500
        #Every time it iterate, when5 will plus one, until it reach 5 gallons.
        while when5 < five_gallons and index < len(data):
            when5 += int(data[index])
            index += 1
        #Then, this line is to count whether the data have reach 100 gallons or not. If not, return -1
        reach = 0
        hundard_gallons = 100000
        if total_power < hundard_gallons:
            reach = -1
        print(f"Data covers a total of {total_hours} hours")
        print(f"(That's {total_days} days)")
        print(f"Pump was running for {time_consume} minutes, producing {gallons_produced} gallons")
        print(f"(That's {gallons_per_day} gallons per day)")
        print(f"Pump required a total of {total_power} watt minutes of power")
        print(f"That's {total_power_kwh} kWh")
        print(f"It took {index} minutes of data to reach 5 gallons.")
        print(f"It took {reach} minutes of data to reach 100 gallons.")
    except OSError as e:
        print(f"Unable to open {analysis_data}.")



    with open('pump_data.txt', 'r') as file:
        # create an empty list, to store the data.
        data = [] 
        for line in file:
            #convert every element to interger and store in the list that I just created.
            data.append(int(line))
    #the mininum duration time is 120 minutes.
    min_run_duration = 120
    #Used to store the duration when the softener recharges
    softener_runs = [] 

    # currently run time
    current_run_duration = 0
    # currently started point
    current_run_start = 0 
    #the reason why use enumerate is because this way I can get the index when it iterate every time.
    for index, power_usage in enumerate(data):
        #if power > 0, means the softener is keep going.
        if power_usage > 0:
            current_run_duration += 1
            if current_run_duration == 1:
                # if it just started, record the index.
                current_run_start = index
        #if power becomes 0, means the softener is stop.
        else:
        # if the runtime satified the mininum, which is 120 minutes, store the time it is running and the index number.
            if current_run_duration >= min_run_duration:
                softener_runs.append((current_run_duration, current_run_start))
            # the reason why I reset the run time duration is because we only want to calculate the duration of over 120 minutes.
            current_run_duration = 0
    #Lastly, I use for loop to read the result that appended in the softener_runs.
    print("Information on water softener recharges:")
    for duration, start_index in softener_runs:
        print(f"{duration} minute run started at {start_index + 1}")
main()