class CapitalizerMixin(object):
    """
    Here is a loop for string capitalizer for educational purpose only.
    To check how many issues we can cause with it.
    """

    def get_upper(self, string):
        if isinstance(string, str):
            return string.upper()
        return self.get_upper(string)
