from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_home_page()
        bot.change_currency(currency="USD")
        bot.select_destination(input("Destination: "))
        bot.select_date(
            check_in_date=input("Check In Date: "),
            check_out_date=input("Check Out Date: ")
        )
        bot.select_adults(int(input("How many People: ")))
        bot.click_search()
        bot.apply_filtration()
        bot.refresh() #give more time to capture the expected data
        bot.find_result()

except Exception as e:
    if "in PATH" in e:
        print("There is a problem with the path of rhe selenium Driver Path")
    else:
        raise
