from pyats import aetest

class common_setup(aetest.CommonSetup):
    """ Common Setup Section """

    @aetest.subsection
    def check_topology(self):
        """ Checking topology mapping """
        pass

    @aetest.subsection
    def establish_connections(self):
        """ Checking possibility for connection to all devices  """
        pass


class PingTestcase(aetest.Testcase):
    """" Test possibility to pinging between devices """
    @aetest.setup
    def setup(self):
        """" Setup for PingTestcase """
        pass

    @aetest.test
    def ping(self):
        """" Method to ping devices """
        pass


class common_cleanup(aetest.CommonCleanup):
    """ Disconnect from all devices """
    @aetest.subsection
    def disconnect(self):
        """ Disconnect from ios routers  """
        pass


if __name__ == '__main__':
    aetest.main()
