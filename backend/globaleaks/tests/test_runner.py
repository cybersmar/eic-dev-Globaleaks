# -*- coding: utf-8 -*-

from globaleaks.tests import helpers

from globaleaks.runner import GlobaLeaksRunner
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from twisted.scripts._twistd_unix import ServerOptions

class TestRunner(helpers.TestGL):
    @inlineCallbacks
    def test_runner(self):
        # TODO: currently this test is mainly fake and is intended at list to
        #       spot errors like typos etcetera by raising the code coverage

        config = ServerOptions()
        #runner.GLBaseRunner(config).run()
        #return

        globaleaks_runner = GlobaLeaksRunner(config)
        #a = yield globaleaks_runner.start_globaleaks()
        #print a

        #globaleaks_runner.start_asynchronous_jobs()
        yield globaleaks_runner.start_globaleaks()
