#!/usr/bin/env python
#
# Copyright (C) 2008, 2011, 2017 UNINETT AS
#
# This file is part of Network Administration Visualized (NAV).
#
# NAV is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.  You should have received a copy of the GNU General Public License
# along with NAV. If not, see <http://www.gnu.org/licenses/>.
#
"""
Extracts closed issues from a NAV milestone on GitHub to produce a list of
fixed issues for a release changelog entry.
"""
from __future__ import print_function, unicode_literals

import sys
import textwrap
import operator
from argparse import ArgumentParser

from github import Github


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("version")
    parser.add_argument("--token", "-t", type=str,
                        help="GitHub API token to use")
    args = parser.parse_args()

    if args.token:
        hub = Github(args.token)
    else:
        hub = Github()

    repo = hub.get_user('UNINETT').get_repo('nav')
    milestones = [m for m in repo.get_milestones(state='all')
                  if m.title == args.version]
    if milestones:
        mstone = milestones[0]
    else:
        print("Couldn't find milestone for {}".format(args.version),
              file=sys.stderr)
        sys.exit(1)

    issues = repo.get_issues(state='closed', milestone=mstone)
    for issue in sorted(issues, key=operator.attrgetter('number')):
        print(format_issue(issue).encode('utf-8'))


def format_issue(issue):
    lead_in = "  * #{:<4} (".format(issue.number)
    indent = " " * len(lead_in)
    line = "{}{})".format(lead_in, issue.title)

    return '\n'.join(
        textwrap.wrap(line, width=72, subsequent_indent=indent))


if __name__ == '__main__':
    main()
