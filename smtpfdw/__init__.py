"""Implement Foreign Data Wrapper for PostgreSQL to allow sending mails."""

from multicorn import ForeignDataWrapper
from mailer import Mailer
from mailer import Message

class MailerForeignDataWrapper(ForeignDataWrapper):
    """Foreign Data Wrapper class."""
    def __init__(self, options, columns):
        super(MailerForeignDataWrapper, self).__init__(options, columns)
        self.columns = columns
        self._row_id_column = list(columns.keys())[0] # a primary key is required for writable API

    @property
    def rowid_column(self):
        """This property is to be implemented for the writable API to work. """
        return self._row_id_column

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

    def delete(self, rowid):
        raise "Recalling e-mails is not implemented"

    def update(self, old_values, new_values):
        raise "Rewriting formerly sent e-mails is not implemented."
