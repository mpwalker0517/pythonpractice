import datetime
import googlemaps

def get_commute_duration():

    home_address = "637 W Kemper Road"
    work_address = "9140 Waterstone Blvd"

    google_maps_api_key = "API_KEY"
    gmaps = google.maps.Client(key=google_maps_api_key)

    directions = gmaps.directions(home_address, work_address)
    first_leg = directions[0]['legs'][0]
    duration = first_leg['duration']['text']
    return duration

def send_text_message(message):
    twilio_account_sid = "AC8b38ffcb6ecc28bffbfd707ba91b95c8"
    twilio_account_token = "8a91ccda15affcd37c197f9f1f43d874"
    twilio_phone_num = "+18552197302"
    your_phone_num = "5139070528"
    client = Client(twilio_account_sid, twilio_account_token)

    client.message.create(
        to=your_phone_num,
        from_=twilio_phone_num,
        body=message
    )
    

def main():
    duration = get_commute_duration()

    now = datetime.now()
    arrival_time = (now+duration).strftime('%I:%M %p')

    message = (
    f"Good morning!\n\n"
    f"Estimated commute time from home to work at 7:30 am: {duration}"
    f"Leave now for work at 7:30 am to arrive at approximately {arrival_time}"
    )

    send_text_message(message)

if __name__ == "__main__":
    main()