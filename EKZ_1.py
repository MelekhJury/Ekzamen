card_number = "1234567891011127"
def card(card_number):
    card_number_last = card_number[11::1]
    print("*" * 11, card_number_last, sep="")

card(card_number)