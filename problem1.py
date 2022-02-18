#
# Name:Asianna/ Matthew
# Collaborator(s):
#
seconds = int(input("How many seconds? "))

days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
secondsf = (seconds % 60)
print (f"{seconds} seconds is {days} days, {hours} hours, {minutes} minutes, with {secondsf} seconds remaining")
