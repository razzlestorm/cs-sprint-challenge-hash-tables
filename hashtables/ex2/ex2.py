#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # ticket.source = previous ticket's destination
    travel_dict = {tick.source: tick.destination for tick in tickets}
    route = []
    for k, v in travel_dict:
        if v == 'NONE':
            route.append(k)

    # Route will be a list of destinations
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]
reconstruct_trip(tickets, 3)
