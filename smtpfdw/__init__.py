"""Implement Foreign Data Wrapper for PostgreSQL to allow sending mails."""

from multicorn import ForeignDataWrapper
from mailer import import Mailer
from mailer import import Message

class MailerForeignDataWrapper(ForeignDataWrapper):
    """Foreign Data Wrapper class."""
    def __init__(self, options, columns):
        super(UrllibForeignDataWrapper, self).__init__(options, columns)
        self.columns = columns

    def insert(self, values):
        """When an INSERT statement is set, send a mail with the 
            from, to, subject, html_body and body values."""
        message = Message(
            From=values["from"],
            To=values["to"],
            charset="utf-8")
        message.Subject = values["subject"]
        
        message.Html = values["html_body"] or None
        message.Body = values["body"]

        sender = Mailer('localhost')
        sender.send(message)

