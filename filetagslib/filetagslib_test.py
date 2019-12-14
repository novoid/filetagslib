#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2019-12-14 11:43:04 vk>

import unittest
import re
from filetagslib.filetagslib import filenameconvention


class TestOrgFormat(unittest.TestCase):

    def setUp(self):
        pass

    def test_filename_pattern_regex_with_timestamp_seconds_description_tags(self):

        self.assertEqual(
            re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01.23 foo bar -- baz1 baz2 baz3.txt').groups(),
            ('2019-12-13T18.01.23',
             '2019-12-13',
             '2019',
             '12',
             '13',
             'T18.01.23',
             '18.01.23',
             '18',
             '01',
             '.23',
             '23',
             ' foo bar',
             'foo bar',
             ' -- baz1 baz2 baz3',
             ' baz1 baz2 baz3',
             'baz1 baz2 baz3',
             'txt')
        )

        # the very same string can be addressed also by named groups:
        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01.23 foo bar -- baz1 baz2 baz3.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01.23')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), '18.01.23')
        self.assertEqual(components.group('hours'), '18')
        self.assertEqual(components.group('minutes'), '01')
        self.assertEqual(components.group('seconds'), '23')
        self.assertEqual(components.group('description'), 'foo bar')
        self.assertEqual(components.group('filetags'), 'baz1 baz2 baz3')
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_timestamp_noseconds_description_tags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01 foo bar -- baz1 baz2 baz3.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), '18.01')
        self.assertEqual(components.group('hours'), '18')
        self.assertEqual(components.group('minutes'), '01')
        self.assertEqual(components.group('seconds'), None)
        self.assertEqual(components.group('description'), 'foo bar')
        self.assertEqual(components.group('filetags'), 'baz1 baz2 baz3')
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_datestamp_notimestamp_description_tags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13 foo bar -- baz1 baz2 baz3.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), None)
        self.assertEqual(components.group('hours'), None)
        self.assertEqual(components.group('minutes'), None)
        self.assertEqual(components.group('seconds'), None)
        self.assertEqual(components.group('description'), 'foo bar')
        self.assertEqual(components.group('filetags'), 'baz1 baz2 baz3')
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_timestamp_seconds_nodescription_tags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01.23 -- baz1 baz2 baz3.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01.23')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), '18.01.23')
        self.assertEqual(components.group('hours'), '18')
        self.assertEqual(components.group('minutes'), '01')
        self.assertEqual(components.group('seconds'), '23')
        self.assertEqual(components.group('description'), None)
        self.assertEqual(components.group('filetags'), 'baz1 baz2 baz3')
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_timestamp_seconds_description_notags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01.23 foo bar.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01.23')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), '18.01.23')
        self.assertEqual(components.group('hours'), '18')
        self.assertEqual(components.group('minutes'), '01')
        self.assertEqual(components.group('seconds'), '23')
        self.assertEqual(components.group('description'), 'foo bar')
        self.assertEqual(components.group('filetags'), None)
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_timestamp_seconds_nodescription_notags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01.23.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01.23')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), '18.01.23')
        self.assertEqual(components.group('hours'), '18')
        self.assertEqual(components.group('minutes'), '01')
        self.assertEqual(components.group('seconds'), '23')
        self.assertEqual(components.group('description'), None)
        self.assertEqual(components.group('filetags'), None)
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_timestamp_noseconds_nodescription_notags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), '18.01')
        self.assertEqual(components.group('hours'), '18')
        self.assertEqual(components.group('minutes'), '01')
        self.assertEqual(components.group('seconds'), None)
        self.assertEqual(components.group('description'), None)
        self.assertEqual(components.group('filetags'), None)
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_datestamp_notimestamp_noseconds_nodescription_notags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), None)
        self.assertEqual(components.group('hours'), None)
        self.assertEqual(components.group('minutes'), None)
        self.assertEqual(components.group('seconds'), None)
        self.assertEqual(components.group('description'), None)
        self.assertEqual(components.group('filetags'), None)
        self.assertEqual(components.group('extension'), 'txt')

# Local Variables:
# End:
