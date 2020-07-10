#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length

    ticket_jumble = {}
    # start = ''
    for t in tickets:
        # print(t.source, t.destination)
        ticket_jumble[t.source] = t.destination

    pointer = ticket_jumble['NONE']
    for index in range(0, length):
        route[index] = pointer
        pointer = ticket_jumble[pointer]
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))