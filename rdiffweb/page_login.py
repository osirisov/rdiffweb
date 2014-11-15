#!/usr/bin/python
# -*- coding: utf-8 -*-
# rdiffweb, A web interface to rdiff-backup repositories
# Copyright (C) 2012 rdiffweb contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import cherrypy
import logging
import page_main

# Define the logger
logger = logging.getLogger(__name__)


class rdiffLoginPage(page_main.rdiffPage):

    @cherrypy.expose
    def index(self, redirect=u"", login=u"", password=""):
        assert isinstance(login, unicode)
        assert isinstance(password, unicode)

        params = {'redirect': redirect,
                  'login': login}

        if self._is_submit():
            # check for login credentials
            logger.info("check credentials for [%s]" % login)
            errorMsg = self.checkpassword(login, password)
            if not errorMsg:
                self.setUsername(login)
                if not redirect:
                    redirect = "/"
                raise cherrypy.HTTPRedirect(redirect)

            # update form values
            params["warning"] = errorMsg

        return self._writePage("login.html", **params)