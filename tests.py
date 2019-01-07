# Copyright (c) 2017, Emergence by Design Inc.

import argparse
import os
import re
import sys
from unittest import TestCase, skipIf

from collections import OrderedDict

import six
from colors import bold, color, underline
from functools import partial
from six import StringIO

from argparse_color_formatter import ColorHelpFormatter, ColorTextWrapper

try:
    from contextlib import redirect_stdout
    from contextlib import redirect_stderr
except ImportError:
    import contextlib

    @contextlib.contextmanager
    def redirect_stdout(target):
        original = sys.stdout
        sys.stdout = target
        yield
        sys.stdout = original

    @contextlib.contextmanager
    def redirect_stderr(target):
        original = sys.stderr
        sys.stderr = target
        yield
        sys.stderr = original

colors = OrderedDict((
    ('red', partial(color, fg='red', style='bold')),
    ('orange', partial(color, fg='orange', style='bold')),
    ('yellow', partial(color, fg='yellow', style='bold')),
    ('green', partial(color, fg='green', style='bold')),
    ('blue', partial(color, fg='blue', style='bold')),
    ('indigo', partial(color, fg='indigo', style='bold')),
    ('violet', partial(color, fg='violet', style='bold'))
))
positions = ['first', 'second', 'third', 'forth', 'fifth', 'sixth', 'seventh']

color_kwargs = {
    'color': bold('color'),
    'typically': underline('typically'),
}
color_pos = OrderedDict(
    (p, v(p)) for v, p in zip(colors.values(), positions)
)
color_names = OrderedDict(
    (k, v(k)) for k, v in colors.items()
)


def rainbow_text(text):
    retval = []
    colors_iter = iter(colors.values())
    cur_color = next(colors_iter)
    for char in text:
        retval.append(cur_color(char))
        try:
            cur_color = next(colors_iter)
        except StopIteration:
            colors_iter = iter(colors.values())
            cur_color = next(colors_iter)
    return ''.join(retval)


color_kwargs.update(color_pos)
color_kwargs.update(color_names)
color_kwargs.update({
    'colorful': rainbow_text('colorful'),
    'rainbow_maker': rainbow_text('rainbow_maker'),
    'bow': rainbow_text('bow'),
    'red-orange-yellow-green-blue-indigo-violet': rainbow_text('red-orange-yellow-green-blue-indigo-violet'),
})


def rainbow_maker_arg_help(color_name):
    return '{color} used when making rainbow, {typically} this would be {color_name}.'.format(
        color=bold('color'),
        typically=underline('typically'),
        color_name=color_kwargs[color_name]
    )


def rainbow_maker(args):
    parser = argparse.ArgumentParser(
        prog='{rainbow_maker}'.format(
            **color_kwargs
        ),
        usage='%(prog)s [-h] {first} {second} {third} {forth} {fifth} {sixth} {seventh}'.format(
            **color_kwargs
        ),
        epilog='This epilog has some {colorful} escapes in it as well and should not wrap on 80.'.format(
            **color_kwargs
        ),
        description='This script is a test for {rainbow_maker}. This description consists of 140 chars.'
                    ' It should be able to fit onto two 80 char lines.'.format(**color_kwargs),
        formatter_class=ColorHelpFormatter,
        add_help=False
    )
    for arg_name, color_name in zip(color_pos.keys(), color_names.keys()):
        parser.add_argument(arg_name, default=color_name, help=rainbow_maker_arg_help(color_name))
    parser.add_argument('-h', '--help', action='help', help='displays this {colorful} help text'.format(**color_kwargs))
    parser.parse_args(args)


def rainbow_maker_auto_usage(args):
    parser = argparse.ArgumentParser(
        prog='{rainbow_maker}'.format(
            **color_kwargs
        ),
        epilog='This epilog has some {colorful} escapes in it as well and should not wrap on 80.'.format(
            **color_kwargs
        ),
        description='This script is a test for {rainbow_maker}. This description consists of 140 chars.'
                    ' It should be able to fit onto two 80 char lines.'.format(**color_kwargs),
        formatter_class=ColorHelpFormatter,
        add_help=False
    )
    for arg_name, color_name in zip(color_pos.keys(), color_names.keys()):
        parser.add_argument(arg_name, default=color_name, help=rainbow_maker_arg_help(color_name))
    parser.add_argument('-h', '--help', action='help', help='displays this {colorful} help text'.format(**color_kwargs))
    parser.parse_args(args)


def rainbow_maker_auto_usage_short_prog(args):
    parser = argparse.ArgumentParser(
        prog='{bow}'.format(
            **color_kwargs
        ),
        epilog='This epilog has some {colorful} escapes in it as well and should not wrap on 80.'.format(
            **color_kwargs
        ),
        description='This script is a test for {rainbow_maker}. This description consists of 140 chars.'
                    ' It should be able to fit onto two 80 char lines.'.format(**color_kwargs),
        formatter_class=ColorHelpFormatter,
        add_help=False
    )
    for arg_name, color_name in zip(color_pos.keys(), color_names.keys()):
        parser.add_argument(arg_name, default=color_name, help=rainbow_maker_arg_help(color_name))
    parser.add_argument('-h', '--help', action='help', help='displays this {colorful} help text'.format(**color_kwargs))
    parser.parse_args(args)


def rainbow_maker_auto_usage_long_prog(args):
    parser = argparse.ArgumentParser(
        prog='{red-orange-yellow-green-blue-indigo-violet}'.format(
            **color_kwargs
        ),
        epilog='This epilog has some {colorful} escapes in it as well and should not wrap on 80.'.format(
            **color_kwargs
        ),
        description='This script is a test for {rainbow_maker}. This description consists of 140 chars.'
                    ' It should be able to fit onto two 80 char lines.'.format(**color_kwargs),
        formatter_class=ColorHelpFormatter,
        add_help=False
    )
    for arg_name, color_name in zip(color_pos.keys(), color_names.keys()):
        parser.add_argument(arg_name, default=color_name, help=rainbow_maker_arg_help(color_name))
    parser.add_argument('-h', '--help', action='help', help='displays this {colorful} help text'.format(**color_kwargs))
    parser.parse_args(args)


def rainbow_maker_no_args(args):
    parser = argparse.ArgumentParser(
        prog='{rainbow_maker}'.format(
            **color_kwargs
        ),
        epilog='This epilog has some {colorful} escapes in it as well and should not wrap on 80.'.format(
            **color_kwargs
        ),
        description='This script is a test for {rainbow_maker}. This description consists of 140 chars.'
                    ' It should be able to fit onto two 80 char lines.'.format(**color_kwargs),
        formatter_class=ColorHelpFormatter,
        add_help=False
    )
    parser.parse_args(args)


class TestColorArgsParserOutput(TestCase):
    maxDiff = None

    def test_color_output_wrapped_as_expected(self):
        out = StringIO()
        with redirect_stdout(out):
            self.assertRaises(SystemExit, rainbow_maker, ['-h'])
        out.seek(0)
        self.assertEqual(
            out.read(),
            'usage: {rainbow_maker} [-h] {first} {second} {third} {forth} {fifth} {sixth} {seventh}\n'
            '\n'
            'This script is a test for {rainbow_maker}. This description consists of 140\n'
            'chars. It should be able to fit onto two 80 char lines.\n'
            '\n'
            'positional arguments:\n'
            '  first       {color} used when making rainbow, {typically} this would be {red}.\n'
            '  second      {color} used when making rainbow, {typically} this would be {orange}.\n'
            '  third       {color} used when making rainbow, {typically} this would be {yellow}.\n'
            '  forth       {color} used when making rainbow, {typically} this would be {green}.\n'
            '  fifth       {color} used when making rainbow, {typically} this would be {blue}.\n'
            '  sixth       {color} used when making rainbow, {typically} this would be {indigo}.\n'
            '  seventh     {color} used when making rainbow, {typically} this would be {violet}.\n'
            '\n'
            'optional arguments:\n'
            '  -h, --help  displays this {colorful} help text\n'
            '\n'
            'This epilog has some {colorful} escapes in it as well and should not wrap on 80.\n'.format(**color_kwargs)
        )

    def test_color_output_wrapped_as_expected_small_width(self):
        try:
            os.environ['COLUMNS'] = '42'
            out = StringIO()
            with redirect_stdout(out):
                self.assertRaises(SystemExit, rainbow_maker, ['-h'])
            out.seek(0)
            self.assertEqual(
                out.read(),
                # usage doesnt wrap for some reason when manually specified.
                # seems like a bug but leaving alone because seems out of scope re: colors.
                'usage: {rainbow_maker} [-h] {first} {second} {third} {forth} {fifth} {sixth} {seventh}\n'
                '\n'
                'This script is a test for {rainbow_maker}.\n'
                'This description consists of 140 chars.\n'
                'It should be able to fit onto two 80\n'
                'char lines.\n'
                '\n'
                'positional arguments:\n'
                '  first       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {red}.\n'
                '  second      {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {orange}.\n'
                '  third       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {yellow}.\n'
                '  forth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {green}.\n'
                '  fifth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {blue}.\n'
                '  sixth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {indigo}.\n'
                '  seventh     {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {violet}.\n'
                '\n'
                'optional arguments:\n'
                '  -h, --help  displays this {colorful}\n'
                '              help text\n'
                '\n'
                'This epilog has some {colorful} escapes in\n'
                'it as well and should not wrap on 80.\n'.format(**color_kwargs)
            )
        finally:
            del os.environ['COLUMNS']

    def test_color_output_wrapped_as_expected_with_auto_usage(self):
        out = StringIO()
        with redirect_stdout(out):
            self.assertRaises(SystemExit, rainbow_maker_auto_usage, ['-h'])
        out.seek(0)
        self.assertEqual(
            out.read(),
            'usage: {rainbow_maker} [-h] first second third forth fifth sixth seventh\n'
            '\n'
            'This script is a test for {rainbow_maker}. This description consists of 140\n'
            'chars. It should be able to fit onto two 80 char lines.\n'
            '\n'
            'positional arguments:\n'
            '  first       {color} used when making rainbow, {typically} this would be {red}.\n'
            '  second      {color} used when making rainbow, {typically} this would be {orange}.\n'
            '  third       {color} used when making rainbow, {typically} this would be {yellow}.\n'
            '  forth       {color} used when making rainbow, {typically} this would be {green}.\n'
            '  fifth       {color} used when making rainbow, {typically} this would be {blue}.\n'
            '  sixth       {color} used when making rainbow, {typically} this would be {indigo}.\n'
            '  seventh     {color} used when making rainbow, {typically} this would be {violet}.\n'
            '\n'
            'optional arguments:\n'
            '  -h, --help  displays this {colorful} help text\n'
            '\n'
            'This epilog has some {colorful} escapes in it as well and should not wrap on 80.\n'.format(**color_kwargs)
        )

    def test_color_output_wrapped_as_expected_with_auto_usage_small_width(self):
        try:
            os.environ['COLUMNS'] = '42'
            out = StringIO()
            with redirect_stdout(out):
                self.assertRaises(SystemExit, rainbow_maker_auto_usage, ['-h'])
            out.seek(0)
            self.assertEqual(
                out.read(),
                'usage: {rainbow_maker} [-h]\n'
                '                     first second third\n'
                '                     forth fifth sixth\n'
                '                     seventh\n'
                '\n'
                'This script is a test for {rainbow_maker}.\n'
                'This description consists of 140 chars.\n'
                'It should be able to fit onto two 80\n'
                'char lines.\n'
                '\n'
                'positional arguments:\n'
                '  first       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {red}.\n'
                '  second      {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {orange}.\n'
                '  third       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {yellow}.\n'
                '  forth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {green}.\n'
                '  fifth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {blue}.\n'
                '  sixth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {indigo}.\n'
                '  seventh     {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {violet}.\n'
                '\n'
                'optional arguments:\n'
                '  -h, --help  displays this {colorful}\n'
                '              help text\n'
                '\n'
                'This epilog has some {colorful} escapes in\n'
                'it as well and should not wrap on 80.\n'.format(**color_kwargs)
            )
        finally:
            del os.environ['COLUMNS']

    def test_color_output_wrapped_as_expected_with_auto_usage_short_prog_small_width(self):
        try:
            os.environ['COLUMNS'] = '42'
            out = StringIO()
            with redirect_stdout(out):
                self.assertRaises(SystemExit, rainbow_maker_auto_usage_short_prog, ['-h'])
            out.seek(0)
            self.assertEqual(
                out.read(),
                'usage: {bow} [-h]\n'
                '           first second third forth\n'
                '           fifth sixth seventh\n'
                '\n'
                'This script is a test for {rainbow_maker}.\n'
                'This description consists of 140 chars.\n'
                'It should be able to fit onto two 80\n'
                'char lines.\n'
                '\n'
                'positional arguments:\n'
                '  first       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {red}.\n'
                '  second      {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {orange}.\n'
                '  third       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {yellow}.\n'
                '  forth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {green}.\n'
                '  fifth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {blue}.\n'
                '  sixth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {indigo}.\n'
                '  seventh     {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {violet}.\n'
                '\n'
                'optional arguments:\n'
                '  -h, --help  displays this {colorful}\n'
                '              help text\n'
                '\n'
                'This epilog has some {colorful} escapes in\n'
                'it as well and should not wrap on 80.\n'.format(**color_kwargs)
            )
        finally:
            del os.environ['COLUMNS']

    def test_color_output_wrapped_as_expected_with_auto_usage_long_prog_small_width(self):
        try:
            os.environ['COLUMNS'] = '42'
            out = StringIO()
            with redirect_stdout(out):
                self.assertRaises(SystemExit, rainbow_maker_auto_usage_long_prog, ['-h'])
            out.seek(0)
            self.assertEqual(
                out.read(),
                'usage: {red-orange-yellow-green-blue-indigo-violet}\n'
                '       [-h]\n'
                '       first second third forth fifth\n'
                '       sixth seventh\n'
                '\n'
                'This script is a test for {rainbow_maker}.\n'
                'This description consists of 140 chars.\n'
                'It should be able to fit onto two 80\n'
                'char lines.\n'
                '\n'
                'positional arguments:\n'
                '  first       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {red}.\n'
                '  second      {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {orange}.\n'
                '  third       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {yellow}.\n'
                '  forth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {green}.\n'
                '  fifth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {blue}.\n'
                '  sixth       {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {indigo}.\n'
                '  seventh     {color} used when making\n'
                '              rainbow, {typically} this\n'
                '              would be {violet}.\n'
                '\n'
                'optional arguments:\n'
                '  -h, --help  displays this {colorful}\n'
                '              help text\n'
                '\n'
                'This epilog has some {colorful} escapes in\n'
                'it as well and should not wrap on 80.\n'.format(**color_kwargs)
            )
        finally:
            del os.environ['COLUMNS']

    def test_color_output_wrapped_as_expected_with_no_args(self):
        out = StringIO()
        with redirect_stderr(out):
            self.assertRaises(SystemExit, rainbow_maker_no_args, ['--bad'])
        out.seek(0)
        self.assertEqual(
            out.read(),
            'usage: {rainbow_maker}\n'
            '{rainbow_maker}: error: unrecognized arguments: --bad\n'.format(**color_kwargs)
        )


class TestColorTextWrapper(TestCase):
    def test_bad_width_error(self):
        ctw = ColorTextWrapper(width=-1)
        self.assertRaisesRegexp(
            ValueError,
            r'invalid width -1 \(must be > 0\)',
            lambda: ctw.wrap('This is some text to wrap.')
        )

    def test_starting_whitespace(self):
        ctw = ColorTextWrapper(width=20)
        self.assertEqual(
            ctw.wrap('   01234 56789 01234 56789 01234 56789 01234 56789'),
            ['   01234 56789 01234', '56789 01234 56789', '01234 56789']
        )

    @skipIf(not six.PY34, 'max_lines and placeholder were added in python 3.4')
    def test_max_lines_and_placeholder(self):
        ctw = ColorTextWrapper(width=10, max_lines=2, placeholder='**' * 10)
        self.assertRaisesRegexp(
            ValueError,
            r'placeholder too large for max width',
            lambda: ctw.wrap('01234 56789 01234 56789 01234 56789 01234 56789')
        )

    @skipIf(not six.PY34, 'max_lines was added in python 3.4')
    def test_max_lines_and_indent(self):
        ctw = ColorTextWrapper(width=20, max_lines=2, initial_indent='  ')
        self.assertEqual(
            ctw.wrap('01234 56789 01234 56789 01234 56789 01234 56789'),
            ['  01234 56789 01234', '56789 01234 [...]']
        )

    @skipIf(not six.PY34, 'max_lines was added in python 3.4')
    def test_max_lines_and_subsequence_indent(self):
        ctw = ColorTextWrapper(width=20, max_lines=0, initial_indent='   ', subsequent_indent=' ')
        self.assertEqual(
            ctw.wrap('01234 56789 01234 56789 01234 56789 01234 56789'),
            ['   01234 56789 [...]']
        )

    def test_too_big(self):
        ctw = ColorTextWrapper(width=10)
        self.assertEqual(
            ctw.wrap('0123456789 0123456789 01234567890123456789'),
            ['0123456789', '0123456789', '0123456789', '0123456789']
        )

    @skipIf(not six.PY34, 'max_lines was added in python 3.4')
    def test_placeholder_edge_case(self):
        ctw = ColorTextWrapper(width=4, max_lines=1, placeholder='***')
        self.assertEqual(
            ctw.wrap('0123456789'),
            ['***']
        )

    @skipIf(not six.PY34, 'max_lines was added in python 3.4')
    def test_placeholder_edge_case_2(self):
        ctw = ColorTextWrapper(width=5, max_lines=2, placeholder='****')
        self.assertEqual(
            ctw.wrap('0123456789 ' * 2),
            ['01234', '****']
        )

if __name__ == '__main__':
    rainbow_maker(None)
