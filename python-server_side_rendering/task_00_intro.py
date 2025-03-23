#!/usr/bin/python3
import os


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
    if not isinstance(attendees, list):
        print('Error: provided attendees is not a list of dictionaries')
        return
    if not template:
        print('Error: provided template is empty')
        return
    if not attendees:
        print('Error: provided attendees list is empty')
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        for key, value in attendee.items():
            if value == "" or value is None:
                value = 'N/A'
            invitation = invitation.replace('{' + key + '}', value)

        filename = f'output_{index}.txt'

        if os.path.exists(filename):
            print(f'Error: file {filename} already exists')
            continue

        with open(filename, 'w') as file:
            file.write(invitation)
