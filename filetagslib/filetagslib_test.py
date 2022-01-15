#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: <2022-01-15 23:47:08 vk>

import unittest
import re
import datetime
from filetagslib.filetagslib import filenameconvention


class TestOrgFormat(unittest.TestCase):

    def setUp(self):
        pass

    def test_filename_pattern_regex_with_timestamp_second_description_tags(self):

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
        self.assertEqual(components.group('hour'), '18')
        self.assertEqual(components.group('minute'), '01')
        self.assertEqual(components.group('second'), '23')
        self.assertEqual(components.group('description'), 'foo bar')
        self.assertEqual(components.group('filetags'), 'baz1 baz2 baz3')
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_timestamp_nosecond_description_tags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01 foo bar -- baz1 baz2 baz3.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), '18.01')
        self.assertEqual(components.group('hour'), '18')
        self.assertEqual(components.group('minute'), '01')
        self.assertEqual(components.group('second'), None)
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
        self.assertEqual(components.group('hour'), None)
        self.assertEqual(components.group('minute'), None)
        self.assertEqual(components.group('second'), None)
        self.assertEqual(components.group('description'), 'foo bar')
        self.assertEqual(components.group('filetags'), 'baz1 baz2 baz3')
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_timestamp_second_nodescription_tags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01.23 -- baz1 baz2 baz3.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01.23')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), '18.01.23')
        self.assertEqual(components.group('hour'), '18')
        self.assertEqual(components.group('minute'), '01')
        self.assertEqual(components.group('second'), '23')
        self.assertEqual(components.group('description'), None)
        self.assertEqual(components.group('filetags'), 'baz1 baz2 baz3')
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_timestamp_second_description_notags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01.23 foo bar.txt')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01.23')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('century'), '20')
        self.assertEqual(components.group('year'), '19')
        self.assertEqual(components.group('ym_sep'), '-')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('md_sep'), '-')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('datetime_sep'), 'T')
        self.assertEqual(components.group('timestamp'), '18.01.23')
        self.assertEqual(components.group('hour'), '18')
        self.assertEqual(components.group('hm_sep'), '.')
        self.assertEqual(components.group('minute'), '01')
        self.assertEqual(components.group('ms_sep'), '.')
        self.assertEqual(components.group('second'), '23')
        self.assertEqual(components.group('end_sep'), ' ')
        self.assertEqual(components.group('description'), 'foo bar')
        self.assertEqual(components.group('filetags'), None)
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_timestamp_second_nodescription_notags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01.23.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01.23')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), '18.01.23')
        self.assertEqual(components.group('hour'), '18')
        self.assertEqual(components.group('minute'), '01')
        self.assertEqual(components.group('second'), '23')
        self.assertEqual(components.group('description'), None)
        self.assertEqual(components.group('filetags'), None)
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_timestamp_nosecond_nodescription_notags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13T18.01.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13T18.01')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), '18.01')
        self.assertEqual(components.group('hour'), '18')
        self.assertEqual(components.group('minute'), '01')
        self.assertEqual(components.group('second'), None)
        self.assertEqual(components.group('description'), None)
        self.assertEqual(components.group('filetags'), None)
        self.assertEqual(components.group('extension'), 'txt')

    def test_filename_pattern_regex_with_datestamp_notimestamp_nosecond_nodescription_notags(self):

        components = re.match(filenameconvention.FILENAME_PATTERN_REGEX, '2019-12-13.txt')
        self.assertEqual(components.group('datestamp'), '2019-12-13')
        self.assertEqual(components.group('datetimestamp'), '2019-12-13')
        self.assertEqual(components.group('year'), '2019')
        self.assertEqual(components.group('month'), '12')
        self.assertEqual(components.group('day'), '13')
        self.assertEqual(components.group('timestamp'), None)
        self.assertEqual(components.group('hour'), None)
        self.assertEqual(components.group('minute'), None)
        self.assertEqual(components.group('second'), None)
        self.assertEqual(components.group('description'), None)
        self.assertEqual(components.group('filetags'), None)
        self.assertEqual(components.group('extension'), 'txt')

    def test_get_datetime(self):
        # testing various file names including seconds:
        myfilenames = ['2022-01-14T17:53:16_foo -- bar.baz',
                       '2022-01-14T17.53.16_foo -- bar.baz',
                       '2022-01-14T17.53.16 foo -- bar.baz',
                       '2022_01_14T17.53.16 foo -- bar.baz',
                       '20220114175316_foo -- bar.baz',
                       '20220114T175316_foo -- bar.baz',
                       '20220114T17.53.16_foo -- bar.baz']
        for myfilename in myfilenames:
            mymatch = re.match(filenameconvention.FILENAME_PATTERN_REGEX, myfilename)
            self.assertEqual(filenameconvention.get_datetime(mymatch), datetime.datetime(2022, 1, 14, 17, 53, 16))

        # testing various file names without seconds:
        myfilenames = ['2022-01-14T17:53_foo -- bar.baz',
                       '2022-01-14T17.53_foo -- bar.baz',
                       '2022-01-14T17.53 foo -- bar.baz',
                       '2022_01_14T17.53 foo -- bar.baz',
                       '202201141753_foo -- bar.baz',
                       '20220114T1753_foo -- bar.baz',
                       '20220114T17.53_foo -- bar.baz']
        for myfilename in myfilenames:
            mymatch = re.match(filenameconvention.FILENAME_PATTERN_REGEX, myfilename)
            self.assertEqual(filenameconvention.get_datetime(mymatch), datetime.datetime(2022, 1, 14, 17, 53))

        # testing various file names without timestamps:
        myfilenames = ['2022-01-14_foo -- bar.baz',
                       '2022_01_14_foo -- bar.baz',
                       '2022_01_14 foo -- bar.baz',
                       '2022.01.14_foo -- bar.baz']
        for myfilename in myfilenames:
            mymatch = re.match(filenameconvention.FILENAME_PATTERN_REGEX, myfilename)
            self.assertEqual(filenameconvention.get_datetime(mymatch), datetime.datetime(2022, 1, 14, 17, 53))

    def test_format_datetime_string_according_to_match(self):

        # the goal is to take the file name pattern and replace its
        # date/timestamp with the date/time of mydatetime instead of
        # the original one:
        mydatetime = datetime.datetime(2999, 12, 31, 23, 59, 58)

        # the test file names and their replaced counterparts:
        myfilenames = [['2022-01-14T17:53:16_foo -- bar.baz', '2999-12-31T23:59:58_foo -- bar.baz'],
                       ['2022-01-14T17.53.16_foo -- bar.baz', '2999-12-31T23.59.58_foo -- bar.baz'],
                       ['2022-01-14T17.53.16 foo -- bar.baz', '2999-12-31T23.59.58 foo -- bar.baz'],
                       ['2022_01_14T17.53.16 foo -- bar.baz', '2999_12_31T23.59.58 foo -- bar.baz'],
                       ['20220114175316_foo -- bar.baz', '29991231235958_foo -- bar.baz'],
                       ['20220114T175316_foo -- bar.baz', '29991231T235958_foo -- bar.baz'],
                       ['20220114T17.53.16_foo -- bar.baz', '29991231T23.59.58_foo -- bar.baz'],
                       ['2022-01-14T17:53_foo -- bar.baz', '2999-12-31T23:59_foo -- bar.baz'],
                       ['2022-01-14T17.53_foo -- bar.baz', '2999-12-31T23.59_foo -- bar.baz'],
                       ['2022-01-14T17.53 foo -- bar.baz', '2999-12-31T23.59 foo -- bar.baz'],
                       ['2022_01_14T17.53 foo -- bar.baz', '2999_12_31T23.59 foo -- bar.baz'],
                       ['202201141753_foo -- bar.baz', '299912312359_foo -- bar.baz'],
                       ['20220114T1753_foo -- bar.baz', '29991231T2359_foo -- bar.baz'],
                       ['20220114T17.53_foo -- bar.baz', '29991231T23.59_foo -- bar.baz'],
                       ['2022-01-14_foo -- bar.baz', '2999-12-31_foo -- bar.baz'],
                       ['2022_01_14_foo -- bar.baz', '2999_12_31_foo -- bar.baz'],
                       ['2022_01_14 foo -- bar.baz', '2999_12_31 foo -- bar.baz'],
                       ['2022.01.14_foo -- bar.baz', '2999.12.31_foo -- bar.baz']]

        for myfilename in myfilenames:
            mymatch = re.match(filenameconvention.FILENAME_PATTERN_REGEX, myfilename[0])
            self.assertEqual(filenameconvention.format_datetime_string_according_to_match(mydatetime, mymatch), myfilename[1])

# Local Variables:
# End:
