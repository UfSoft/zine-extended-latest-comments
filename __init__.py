# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8
# =============================================================================
# $Id: __init__.py 98 2008-05-09 13:05:19Z s0undt3ch $
# =============================================================================
#             $URL: http://devnull.ufsoft.org/svn/ExtendedLatestCommentsWidget/trunk/__init__.py $
# $LastChangedDate: 2008-05-09 14:05:19 +0100 (Fri, 09 May 2008) $
#             $Rev: 98 $
#   $LastChangedBy: s0undt3ch $
# =============================================================================
# Copyright (C) 2007 Ufsoft.org - Pedro Algarvio <ufs@ufsoft.org>
#
# Please view LICENSE for additional licensing information.
# =============================================================================

from os.path import dirname, join
from textpress.api import *
from textpress.widgets import LatestComments

TEMPLATES = join(dirname(__file__), 'templates')

class ExtendedLatestComments(LatestComments):
    """
    Show the latest n comments and
    the n words of each comment.
    """
    NAME = 'get_latest_comments_extended'
    TEMPLATE = 'extended_latest_comments.html'

    def __init__(self, limit=5, show_title=False, max_words=10,
                 ignore_blocked=False):
        self.max_words = max_words
        LatestComments.__init__(self, limit, show_title, ignore_blocked)

    @staticmethod
    def get_display_name():
        return _('Latest Comments (Extended)')

    @staticmethod
    def configure_widget(initial_args, request):
        args = form = initial_args.copy()
        errors = []
        if request.method == 'POST':
            args['limit'] = limit = request.form.get('limit')
            if not limit:
                args['limit'] = None
            elif not limit.isdigit():
                errors.append(_('Limit must be omited or a valid number.'))
            else:
                args['limit'] = int(limit)
            args['max_words'] = max_words = request.form.get('max_words')
            if not max_words:
                args['max_words'] = None
            elif not max_words.isdigit():
                errors.append(_('Limit must be omited or a valid number.'))
            else:
                args['max_words'] = int(max_words)
            args['show_title'] = request.form.get('show_title') == 'yes'
            args['ignore_blocked'] = request.form.get('ignore_blocked') == 'yes'
        if errors:
            args = None
        return args, render_template('admin/extended_latest_comments.html',
                                     errors=errors, form=form)

def setup(app, plugin):
    app.add_template_searchpath(TEMPLATES)
    app.add_widget(ExtendedLatestComments)
