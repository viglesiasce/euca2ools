# Software License Agreement (BSD License)
#
# Copyright (c) 2009-2011, Eucalyptus Systems, Inc.
# All rights reserved.
#
# Redistribution and use of this software in source and binary forms, with or
# without modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the
#   following disclaimer.
#
#   Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the
#   following disclaimer in the documentation and/or other
#   materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Neil Soman neil@eucalyptus.com
#         Mitch Garnaat mgarnaat@eucalyptus.com

from boto.roboto.awsqueryrequest import AWSQueryRequest
from boto.roboto.param import Param
import euca2ools.commands.euare


class UpdateGroup(AWSQueryRequest):

    ServiceClass = euca2ools.commands.euare.Euare

    Description = """UpdateGroup"""
    Params = [Param(
        name='GroupName',
        short_name='g',
        long_name='group-name',
        ptype='string',
        optional=False,
        doc=""" Name of the group to update. If you're changing the name of the group, this is the original name. """
            ,
        ), Param(
        name='NewPath',
        short_name='n',
        long_name='new-path',
        ptype='string',
        optional=True,
        doc=""" New path for the group. Only include this if changing the group's path. """
            ,
        ), Param(
        name='NewGroupName',
        short_name=None,
        long_name='new-group-name',
        ptype='string',
        optional=True,
        doc=""" New name for the group. Only include this if changing the group's name. """
            ,
        )]

    Response = {u'type': u'object', u'name': u'UpdateGroupResponse',
                u'properties': [{
        u'type': u'object',
        u'optional': False,
        u'name': u'ResponseMetadata',
        u'properties': [{u'type': u'string', u'optional': False, u'name'
                        : u'RequestId'}],
        }]}


def main(**args):
    req = UpdateGroup(**args)
    return req.send()


def main_cli():
    req = UpdateGroup()
    req.do_cli()

