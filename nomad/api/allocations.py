from nomad.api.base import Requester


class Allocations(Requester):

    """
    The allocations endpoint is used to query the status of allocations.
    By default, the agent's local region is used; another region can be
    specified using the ?region= query parameter.

    https://www.nomadproject.io/docs/http/allocs.html
    """
    ENDPOINT = "allocations"

    def __init__(self, **kwargs):
        super(Allocations, self).__init__(**kwargs)

    def __str__(self):
        return "{0}".format(self.__dict__)

    def __repr__(self):
        return "{0}".format(self.__dict__)

    def __getattr__(self, item):
        raise AttributeError

    def __len__(self):
        response = self.get_allocations()
        return len(response)

    def __iter__(self):
        response = self.get_allocations()
        return iter(response)

    def get_allocations(self, prefix=None):
        """ Lists all the allocations.

           https://www.nomadproject.io/docs/http/allocs.html
            arguments:
              - prefix :(str) optional, specifies a string to filter allocations on based on an prefix.
                        This is specified as a querystring parameter.
            returns: list of dicts
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = {"prefix": prefix}
        return self.request(method="get", params=params).json()

    def get_allocations_by_status(self, status='running', prefix=None):
        """ Lists plain list of allocations with particular status.
            By default, returns only running allocations

           https://www.nomadproject.io/docs/http/allocs.html
            arguments:
              - status :(str) optional, specifies a string to filter allocations on based on a status
              - prefix :(str) optional, specifies a string to filter allocations on based on a prefix.
                        This is specified as a querystring parameter.
            returns: list
            raises:
              - nomad.api.exceptions.BaseNomadException
              - nomad.api.exceptions.URLNotFoundNomadException
        """
        params = {"prefix": prefix}
        alloc_list = []
        for alloc in self.request(method="get", params=params).json():
            if status == alloc['ClientStatus']:
                alloc_list.append(alloc['ID'])

        return alloc_list
