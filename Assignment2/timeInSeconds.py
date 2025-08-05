hours=int(input("Enter hours:"))
mins=int(input("Enter mins:"))
secs=int(input("Enter secs:"))

total_seconds= (hours*3600)+ (mins * 60) + secs

print(f'Total time in seconds:{total_seconds}')