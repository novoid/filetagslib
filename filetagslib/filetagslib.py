#!/usr/bin/env python3
# -*- coding: utf-8; mode: python; -*-
# Time-stamp: <2022-01-15 23:49:33 vk>

import logging # let's log stuff helpful for the user and for debugging
import re      # oh, this is using regular expressions quite a bit :-)
from typing import List, Union, Tuple, Optional  # mypy: type checks

# for handling date and time:
import locale
import datetime
locale.setlocale(locale.LC_ALL, '')



class filenameconvention():
    """
    Utility library related to filenameconvention of filetags.
    """

    #DATESTAMP_PATTERN = '(?P<datestamp>(?P<year>\d{4,4})-(?P<month>[01]\d)-(?P<day>[0123]\d))'
    #HMS_PATTERN = '(?P<hours>[012]\d)\.(?P<minutes>[012345]\d)(\.(?P<seconds>[012345]\d))?'
    #TIMESTAMP_PATTERN = DATESTAMP_PATTERN + '(T(?P<timestamp>' + HMS_PATTERN + '))?'
    #FILENAME_PATTERN_REGEX = re.compile('^(?P<datetimestamp>' + TIMESTAMP_PATTERN + ')' +
    #                                    '([-_ ](?P<description>.+?))??' +
    #                                    '(' + FILETAGS_PATTERN + ')?' +
    #                                    '\.(?P<extension>\w+)$')

    YMD_SEPARATORS = '[-_.]'         # potential separator character between the entities of year, month, day
    DATETIME_SEPARATORS = '[T: -_]'  # potential separator character between the entities of datestamp and timestamp
    HMS_SEPARATORS = '[:.-]'         # potential separator character between the entities of hour, minute, second
    END_SEPARATORS = '[^a-zA-Z0-9]'  # potential separator character between the entities of datetimestamp and rest
    BETWEEN_TAG_SEPARATOR = ' '      # mandatory separator between two different tags
    FILENAME_TAG_SEPARATOR = ' -- '  # mandatory separator between normal file name and list of tags (if there are tags)
    FILETAGS_PATTERN = FILENAME_TAG_SEPARATOR.rstrip() + '([ ](?P<filetags>.+))+'

    # The regular expression matches optional date- and time-stamps as long as order is YMDHM(S).
    # Simplified:   (YY)?YY.MM.DD.HH.MM(.SS)?
    # Frequently used examples: (more combinations are matching)
    #    YYYY-MM-DDTHH.MM.SS foo.bar
    #    YYYY-MM-DDTHH.MM foo.bar
    #    YYYY-MM-DD foo.bar
    #    YYYYMMDDTHH.MM.SS_foo.bar
    #    YYYYMMDDTHHMMSS_foo.bar
    #    YYYY_MM_DDTHH:MM:SS_foo.bar
    #
    # For other orders like MM/DD/YYYY: please do re-think your life choices. ;-)  *SCNR*
    # Unsupported:
    #    - non-ISO-like orders of the entities
    #    - time zones or time offsets
    #    - weeks
    #    - durations or intervals
    #    - milliseconds
    #
    # The separation characters are limited to sets of potential characters (see regex for details).
    FILENAME_PATTERN_REGEX = \
        re.compile(r'^' +
                   r'(?P<datetimestamp>' +                              # BEGIN: datetimestamp: datetimestamp with separator (OPTIONAL)
                   r'(?P<datestamp>' +                                  #   BEGIN: datestamp
                   r'(?P<century>\d{2})?' +                             #     optional century: YY    e.g. 20 (from 2022)
                   r'(?P<year>\d{2})' +                                 #     YY    e.g. 22 (from 2022)
                   r'(?P<ym_sep>' + YMD_SEPARATORS + ')?' +             #     optional separator character
                   r'(?P<month>[01]\d)' +                               #     MM    e.g. 12 (December)
                   r'(?P<md_sep>' + YMD_SEPARATORS + ')?' +             #     optional separator character
                   r'(?P<day>[0123]\d)' +                               #     DD    e.g. 31
                   r')?' +                                              #   END: datestamp
                   r'(' +                                               #   BEGIN: timestamppart is optional
                   r'(?P<datetime_sep>' + DATETIME_SEPARATORS + ')?' +  #     optional separator character
                   r'(?P<timestamp>' +                                  #     BEGIN: timestamp
                   r'(?P<hour>[012]\d)' +                               #       HH    e.g. 23
                   r'(?P<hm_sep>' + HMS_SEPARATORS + ')?' +             #       optional separator character
                   r'(?P<minute>[012345]\d)' +                          #       MM    e.g. 59
                   r'(' +                                               #       BEGIN: seconds are optional
                   r'(?P<ms_sep>' + HMS_SEPARATORS + ')?' +             #         optional separator character
                   r'(?P<second>[012345]\d)' +                          #         SS    e.g. 59
                   r')?' +                                              #       END: seconds are optional
                   r')?' +                                              #     END: timestamp
                   r')?' +                                              #   END: timestamppart is optional
                   r')?' +                                              # END: datetimestamp: datetimestamp
                   r'(?P<end_sep>' + END_SEPARATORS + ')' +             # mandatory separator character
                   r'(?P<description>.+?)??' +                          # the usual file name which is not date/timestamp prefix, filetags or extension
                   r'(' + FILETAGS_PATTERN + ')?' +                     # the optional list of filetags
                   r'\.(?P<extension>\w+)$'                             # the mandatory file extension
        )

    # examples:

    # re.match(FILENAME_PATTERN_REGEX, '2022-01-14T17.53.16_foo -- bar.baz').groups()
    #  -> FIXXME

    # re.match(FILENAME_PATTERN_REGEX, '2022-01-14T17.53.16_foo -- bar.baz').groupdict()
    #  -> FIXXME

    def is_filenamepattern_match(self, mymatch: Union[None, re.Match]) -> bool:
        return mymatch is not None

    def has_match_century(self, mymatch: re.Match) -> bool:
        return mymatch.group('century') is not None

    def has_match_year(self, mymatch: re.Match) -> bool:
        return mymatch.group('year') is not None

    def has_match_month(self, mymatch: re.Match) -> bool:
        return mymatch.group('month') is not None

    def has_match_day(self, mymatch: re.Match) -> bool:
        return mymatch.group('day') is not None

    def has_match_datestamp(self, mymatch: re.Match) -> bool:
        return mymatch.group('datestamp') is not None

    def has_match_hours(self, mymatch: re.Match) -> bool:
        return mymatch.group('hour') is not None

    def has_match_minutes(self, mymatch: re.Match) -> bool:
        return mymatch.group('minute') is not None

    def has_match_seconds(self, mymatch: re.Match) -> bool:
        return mymatch.group('second') is not None

    def has_match_timestamp(self, mymatch: re.Match) -> bool:
        return mymatch.group('timestamp') is not None

    def has_match_description(self, mymatch: re.Match) -> bool:
        return mymatch.group('description') is not None

    def has_match_filetags(self, mymatch: re.Match) -> bool:
        return mymatch.group('filetags') is not None

    def has_match_extension(self, mymatch: re.Match) -> bool:
        return mymatch.group('extension') is not None

    def get_match_full_year(self, mymatch: re.Match) -> str:
        if not self.has_match_century(mymatch):
            return '20' + mymatch.group('year')  # this defaults to the 21th century
        else:
            return mymatch.group('century') + mymatch.group('year')

    def get_datetime(self, mymatch: re.Match) -> datetime.datetime:

        assert self.is_filenamepattern_match(mymatch)
        year = int(self.get_match_full_year(mymatch))

        if self.has_match_timestamp(mymatch):
            if self.has_match_seconds(mymatch):
                return datetime.datetime(year, int(mymatch.group('month')), int(mymatch.group('day')), int(mymatch.group('hour')), int(mymatch.group('minute')), int(mymatch.group('second')))
            else:
                return datetime.datetime(year, int(mymatch.group('month')), int(mymatch.group('day')), int(mymatch.group('hour')), int(mymatch.group('minute')), 0)
        else:
            return datetime.datetime(year, int(mymatch.group('month')), int(mymatch.group('day')) )

    def format_datetime_string_according_to_match(self, mydatetime: datetime.datetime, mymatch: re.Match) -> str:

        assert self.is_filenamepattern_match(mymatch)
        if self.has_match_century(mymatch):
            year = str(mydatetime.year)
        else:
            year = str(mydatetime.year)[2:]

        # separators: ['hm_sep', 'end_sep', 'md_sep', 'ms_sep', 'datetime_sep', 'ym_sep']

        if self.has_match_timestamp(mymatch):
            if self.has_match_seconds(mymatch):
                return year + mymatch.group('ym_sep') + str(mydatetime.month) + mymatch.group('md_sep') + str(mydatetime.day) + \
                    mymatch.group('datetime_sep') + str(mydatetime.hour) + mymatch.group('hm_sep') + \
                    str(mydatetime.minute) + mymatch.group('ms_sep') + str(mydatetime.second) + mymatch.group('end_sep')
            else:
                return year + mymatch.group('ym_sep') + str(mydatetime.month) + mymatch.group('md_sep') + \
                    str(mydatetime.day) + mymatch.group('datetime_sep') + str(mydatetime.hour) + \
                    mymatch.group('hm_sep') + str(mydatetime.minute) + mymatch.group('end_sep')
        else:
            return year + mymatch.group('ym_sep') + str(mydatetime.month) + mymatch.group('md_sep') + \
                    str(mydatetime.day) + mymatch.group('end_sep')



# Local Variables:
# End:
