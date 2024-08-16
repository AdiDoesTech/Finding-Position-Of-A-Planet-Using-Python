from astropy.coordinates import get_body, EarthLocation
from astropy.time import Time

# Get the current time
now = Time.now()

# Define the location (e.g., Greenwich)
location = EarthLocation.of_site('greenwich')

# Input for the celestial body (not Earth itself)
body_name = input("Enter the name of the planet (e.g., 'venus'): ").lower()

# Get the celestial body's position
try:
    body_position = get_body(body_name, now)
    print(f"{body_name.capitalize()} Position: RA = {body_position.ra}, Dec = {body_position.dec}")
except KeyError:
    print("Invalid celestial body name. Please enter a valid celestial body name.")

# For some people you might need to get the astropy, / pip install astropy i think, or esle just follow this code! :D
