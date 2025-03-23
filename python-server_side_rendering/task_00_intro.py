#!/usr/bin/python3


def generate_invitations(template: str, attendees: list[dict]):
    """
    Generates invitation letters for attendees based on the provided template.
    attendees is a list of dictionaries, where each dictionary contains the
    name, event_title, event_date, and event_location of the attendee.  
    template is a string that contains placeholders for the name, event_title,
    event_date, and event_location.  The placeholders are enclosed in curly braces.
    The function will generate an invitation letter for each attendee by replacing
    the placeholders with the actual values.  The function will write each
    invitation letter to a file named 'invitation_X.txt', where X is the index of
    the attendee in the attendees list.
    """

    if not isinstance(template, str):
        print('Error: provided template is not a string')
        return
    if not isinstance(attendees, list or not all(isinstance(attendee, dict) for attendee in attendees)):
        print('Error: provided attendees is not a list of dictionaries')
        return
    if not template:
        print('Error: provided template is empty')
        return
    if not attendees:
        print('Error: provided attendees list is empty')
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template.format(
            name=attendee.get('name', 'N/A'),
            event_title=attendee.get('event_title', 'N/A'),
            event_date=attendee.get('event_date', 'N/A'),
            event_location=attendee.get('event_location', 'N/A')
        )

        filename = f'invitation_{index}.txt'

        with open(filename, 'w') as file:
            file.write(invitation)
