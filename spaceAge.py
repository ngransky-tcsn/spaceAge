from datetime import date

def spaceAge(bday, planet):
	orbitalPeriods = {
		"mercury": 88,
		"venus": 225,
		"earth": 365,
		"mars": 687,
		"jupiter": 4333,
		"saturn": 10756,
		"uranus": 30687,
		"neptune": 60190
	}

	planet = planet.lower()

	if planet not in orbitalPeriods:
		return "Not a valid planet!"

	try:
		age = date.today() - date.fromisoformat(bday)
	except:
		return "Not a valid date, please enter as YYYY-MM-DD!"

	if age.days < 0:
		return "Are you from the future? Date must be from the past!"


	spaceAge = age.days / orbitalPeriods[planet]
	return round(spaceAge, 2)


birthday = input("Enter your birthday (YYYY-MM-DD): ")
p = input("Enter a planet: ")
print(spaceAge(birthday, p)) #YYYY-MM-DD