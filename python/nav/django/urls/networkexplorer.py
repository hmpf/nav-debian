#
# Copyright (C) 2007-2008 UNINETT AS
#
# This file is part of Network Administration Visualized (NAV).
#
# NAV is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.  You should have received a copy of the GNU General Public
# License along with NAV. If not, see <http://www.gnu.org/licenses/>.
#
"""Django URL configuration for Network Explorer"""

from django.conf.urls.defaults import patterns, include

def get_urlpatterns():
    urlpatterns = patterns('',
        # Give the networkexplorer namespace to the Network Explorer subsystem
        (r'^networkexplorer/', include('nav.web.networkexplorer.urls')),
    )
    return urlpatterns
