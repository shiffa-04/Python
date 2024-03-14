from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H")

if current_time >= "5" and  current_time <= "12":
    print("GOOD MORNING")

elif current_time > "12" and current_time < "5":
    print("GOOD AFTERNOON")

elif current_time > "5" and current_time < "9":
    print("GOOD EVENING")
    
else:
    print("GOOD NIGHT")