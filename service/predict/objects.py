class TicketObject(object):
    ticket_id = ""
    status = 0
    priority = 2
    created_at = ""

    def __init__(self, subject,content, **attrs):
        if 'status' in attrs:
            self.status = attrs['status']
        if 'priority' in attrs:
            self.priority = attrs['priority']
        self.subject = subject
        self.content = content
