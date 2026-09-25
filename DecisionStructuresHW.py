#Inputs
SpeedLim = float(input("Enter speed limit (MPH): "))
AvgSpeed = float(input("Enter average speed (MPH): "))
Distance = float(input("Enter distance traveled (miles): "))

MinInHour = 60

#Processing
SpeedLimTime = Distance / SpeedLim
AvgSpeedTime = Distance / AvgSpeed

SpeedLimTimeMin = SpeedLimTime * MinInHour
AvgSpeedTimeMin = AvgSpeedTime * MinInHour

TimeSaved = SpeedLimTimeMin - AvgSpeedTimeMin

#Display Output
if AvgSpeedTimeMin < SpeedLimTimeMin:
    print(f'You saved {TimeSaved:.2f} minutes!')
else:
    print("No time has been saved.")