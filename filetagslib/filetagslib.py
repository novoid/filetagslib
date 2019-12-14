#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; -*-
# Time-stamp: <2019-12-13 17:00:43 vk>

import logging
import re


class RegEx():
    """
    Utility library for regular expressions related to filetags.
    """

    BETWEEN_TAG_SEPARATOR = ' '
    FILENAME_TAG_SEPARATOR = ' -- '
    DATESTAMP_PATTERN = '(?P<datestamp>(?P<year>\d{4,4})-(?P<month>[01]\d)-(?P<day>[0123]\d))'
    HMS_PATTERN = '(?P<hours>[012]\d)\.(?P<minutes>[012345]\d)(\.(?P<seconds>[012345]\d))?'
    TIMESTAMP_PATTERN = DATESTAMP_PATTERN + '(T(?P<timestamp>' + HMS_PATTERN + '))?'
    FILETAGS_PATTERN = FILENAME_TAG_SEPARATOR.rstrip() + '([ ](?P<filetags>.+))+'
    FILENAME_PATTERN_REGEX = re.compile('^(?P<datetimestamp>' + TIMESTAMP_PATTERN + ')' +
                                        '([-_ ](?P<description>.+?))??' +
                                        '(' + FILETAGS_PATTERN + ')?' +
                                        '\.(?P<extension>\w+)$')

# Local Variables:
# End:
