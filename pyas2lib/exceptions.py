from __future__ import absolute_import, unicode_literals

__all__ = [
    'ImproperlyConfigured', 'AS2Exception', 'DecompressionError',
    'DecryptionError', 'InsufficientSecurityError', 'IntegrityError',
    'UnexpectedError', 'MDNNotFound', 'PartnerNotFound', 'DuplicateDocument'
]


class ImproperlyConfigured(Exception):
    """
    Exception raised when the config passed to the client is inconsistent
    or invalid.
    """


class AS2Exception(Exception):
    """
    Base class for all exceptions raised by this package's operations (doesn't
    apply to :class:`~pyas2lib.ImproperlyConfigured`).
    """

    def __init__(self, disposition_modifier=None, *args, **kwargs):
        super(Exception, self).__init__(*args, **kwargs)
        self.disposition_type = 'failed/Failure'
        self.disposition_modifier = disposition_modifier


class PartnerNotFound(AS2Exception):
    """Raised when the partner/organization for the message could not be found
    in the system"""

    def __init__(self, *args, **kwargs):
        super(AS2Exception, self).__init__(*args, **kwargs)
        self.disposition_type = 'processed/Error'
        self.disposition_modifier = 'unknown-trading-partner'


class DuplicateDocument(AS2Exception):
    """Raised when a message with a duplicate message ID has been received"""

    def __init__(self, *args, **kwargs):
        super(AS2Exception, self).__init__(*args, **kwargs)
        self.disposition_type = 'processed/Warning'
        self.disposition_modifier = 'duplicate-document'


class InsufficientSecurityError(AS2Exception):
    """Exception raised when the message security is not as per the
    settings for the partner."""

    def __init__(self, *args, **kwargs):
        super(AS2Exception, self).__init__(*args, **kwargs)
        self.disposition_type = 'processed/Error'
        self.disposition_modifier = 'insufficient-message-security'


class DecompressionError(AS2Exception):
    """Raised when the decompression process fails."""

    def __init__(self, *args, **kwargs):
        super(AS2Exception, self).__init__(*args, **kwargs)
        self.disposition_type = 'processed/Error'
        self.disposition_modifier = 'decompression-failed'


class DecryptionError(AS2Exception):
    """Exception raised when decryption process fails."""

    def __init__(self, *args, **kwargs):
        super(AS2Exception, self).__init__(*args, **kwargs)
        self.disposition_type = 'processed/Error'
        self.disposition_modifier = 'decryption-failed'


class IntegrityError(AS2Exception):
    """Raised when a signed message signature verification fails"""

    def __init__(self, *args, **kwargs):
        super(AS2Exception, self).__init__(*args, **kwargs)
        self.disposition_type = 'processed/Error'
        self.disposition_modifier = 'authentication-failed'


class UnexpectedError(AS2Exception):
    """A catch all exception to be raised for any error found while parsing
     a received AS2 message"""

    def __init__(self, *args, **kwargs):
        super(AS2Exception, self).__init__(*args, **kwargs)
        self.disposition_type = 'processed/Error'
        self.disposition_modifier = 'unexpected-processing-error'


class MDNNotFound(AS2Exception):
    """
    Raised when no MDN is found when parsing the received MIME message.
    """
