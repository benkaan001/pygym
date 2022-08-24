import random

""" (2) Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
    Conditons:
            The lottery number must be 10 digits long.
            All 100 ticket number must be unique.
"""


def generate_tickets():
    ticket_list = []
    for i in range(100):
        ticket_list.append(random.randrange(1000000000, 9999999999))
    lucky_tickets = random.sample(ticket_list, 2)
    return lucky_tickets


ticket1, ticket2 = generate_tickets()
print(f"Lucky ticket numbers are: {ticket1} and {ticket2} ")
