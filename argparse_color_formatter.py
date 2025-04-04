# -*- coding: utf-8 -*-
# original implementations of the methods below are
#  Copyright © 2001-2017 Python Software Foundation; All Rights Reserved
# they are licensed under the PSF LICENSE AGREEMENT FOR PYTHON 3.5.4

# changes were applied to allow these methods to deal with ansi color escape codes. These changes are
#  Copyright (c) 2017, Emergence by Design Inc.
#  Copyright (c) 2024, Arrai Innovations Inc.


__version__ = "2.0.0.post1"
import re as _re
from argparse import SUPPRESS
from argparse import ArgumentDefaultsHelpFormatter
from argparse import HelpFormatter


try:
    from argparse import MetavarTypeHelpFormatter
except ImportError:
    pass
from argparse import ZERO_OR_MORE
from argparse import RawDescriptionHelpFormatter
from argparse import RawTextHelpFormatter
from gettext import gettext as _
from textwrap import TextWrapper

from colors import strip_color


def color_aware_pad(text, width, char=" "):
    return text + char * (width - len(strip_color(text)))


class ColorHelpFormatterMixin(object):
    def _fill_text(self, text, width, indent):
        text = self._whitespace_matcher.sub(" ", text).strip()
        return ColorTextWrapper(width=width, initial_indent=indent, subsequent_indent=indent).fill(text)

    def _split_lines(self, text, width):
        text = self._whitespace_matcher.sub(" ", text).strip()
        return ColorTextWrapper(width=width).wrap(text)

    def add_argument(self, action):
        old_max = self._action_max_length
        super(ColorHelpFormatterMixin, self).add_argument(action)
        # the self._action_max_length updated above won't account for color codes,
        #  so we need to update it here as well
        if action.help is not SUPPRESS:
            self._action_max_length = old_max
            get_invocation = self._format_action_invocation
            invocations = [get_invocation(action)]
            for subaction in self._iter_indented_subactions(action):
                invocations.append(get_invocation(subaction))

            invocation_length = max(len(strip_color(invocation)) for invocation in invocations)
            action_length = invocation_length + self._current_indent
            self._action_max_length = max(self._action_max_length, action_length)

    def _format_args(self, action, default_metavar):
        result = super()._format_args(action, default_metavar)
        if action.nargs == ZERO_OR_MORE:
            metavar = self._metavar_formatter(action, default_metavar)(1)
            if len(strip_color(metavar)) == 2:
                result = "[%s [%s ...]]" % metavar
            else:
                result = "[%s ...]" % metavar
        return result

    # modified upstream code
    # fmt: off
    def _format_action(self, action):
        # determine the required width and the entry label
        help_position = min(self._action_max_length + 2,
                            self._max_help_position)
        help_width = max(self._width - help_position, 11)
        action_width = help_position - self._current_indent - 2
        action_header = self._format_action_invocation(action)

        # no help; start on same line and add a final newline
        if not action.help:
            tup = self._current_indent, '', action_header
            action_header = '%*s%s\n' % tup

        # short action name; start on the same line and pad two spaces
        elif len(strip_color(action_header)) <= action_width:
            tup = self._current_indent, '', color_aware_pad(action_header, action_width)
            action_header = '%*s%s  ' % tup
            indent_first = 0

        # long action name; start on the next line
        else:
            tup = self._current_indent, '', action_header
            action_header = '%*s%s\n' % tup
            indent_first = help_position

        # collect the pieces of the action help
        parts = [action_header]

        # if there was help for the action, add lines of help text
        if action.help and action.help.strip():
            help_text = self._expand_help(action)
            if help_text:
                help_lines = self._split_lines(help_text, help_width)
                parts.append('%*s%s\n' % (indent_first, '', help_lines[0]))
                for line in help_lines[1:]:
                    parts.append('%*s%s\n' % (help_position, '', line))

        # or add a newline if the description doesn't end with one
        elif not action_header.endswith('\n'):
            parts.append('\n')

        # if there are any sub-actions, add their help as well
        for subaction in self._iter_indented_subactions(action):
            parts.append(self._format_action(subaction))

        # return a single string
        return self._join_parts(parts)
    # fmt: on

    # modified upstream code, not going to refactor for complexity.
    # fmt: off
    def _format_usage(self, usage, actions, groups, prefix):  # noqa: C901
        if prefix is None:
            prefix = _("usage: ")
        prefix_len = len(strip_color(prefix))

        # if usage is specified, use that
        if usage is not None:
            usage = usage % {"prog": self._prog}

        # if no optionals or positionals are available, usage is just prog
        elif usage is None and not actions:
            usage = "%(prog)s" % {"prog": self._prog}

        # if optionals and positionals are available, calculate usage
        elif usage is None:
            prog = "%(prog)s" % {"prog": self._prog}

            # split optionals from positionals
            optionals = []
            positionals = []
            for action in actions:
                if action.option_strings:
                    optionals.append(action)
                else:
                    positionals.append(action)

            # build full usage string
            format = self._format_actions_usage
            action_usage = format(optionals + positionals, groups)
            usage = " ".join([s for s in [prog, action_usage] if s])

            # wrap the usage parts if it's too long
            text_width = self._width - self._current_indent
            if prefix_len + len(strip_color(usage)) > text_width:

                # break usage into wrappable parts
                part_regexp = (
                    r'\(.*?\)+(?=\s|$)|'
                    r'\[.*?\]+(?=\s|$)|'
                    r'\S+'
                )
                opt_usage = format(optionals, groups)
                pos_usage = format(positionals, groups)
                opt_parts = _re.findall(part_regexp, opt_usage)
                pos_parts = _re.findall(part_regexp, pos_usage)
                assert " ".join(opt_parts) == opt_usage
                assert " ".join(pos_parts) == pos_usage

                # helper for wrapping lines
                def get_lines(parts, indent, prefix=None):
                    lines = []
                    line = []
                    indent_length = len(indent)
                    if prefix is not None:
                        line_len = prefix_len - 1
                    else:
                        line_len = indent_length - 1
                    for part in parts:
                        part_len = len(strip_color(part))
                        if line_len + 1 + part_len > text_width and line:
                            lines.append(indent + " ".join(line))
                            line = []
                            line_len = indent_length - 1
                        line.append(part)
                        line_len += part_len + 1
                    if line:
                        lines.append(indent + " ".join(line))
                    if prefix is not None:
                        lines[0] = lines[0][indent_length:]
                    return lines

                # if prog is short, follow it with optionals or positionals
                len_prog = len(strip_color(prog))
                if prefix_len + len_prog <= 0.75 * text_width:
                    indent = " " * (prefix_len + len_prog + 1)
                    if opt_parts:
                        lines = get_lines([prog] + opt_parts, indent, prefix)
                        lines.extend(get_lines(pos_parts, indent))
                    elif pos_parts:
                        lines = get_lines([prog] + pos_parts, indent, prefix)
                    else:
                        lines = [prog]

                # if prog is long, put it on its own line
                else:
                    indent = " " * prefix_len
                    parts = opt_parts + pos_parts
                    lines = get_lines(parts, indent)
                    if len(lines) > 1:
                        lines = []
                        lines.extend(get_lines(opt_parts, indent))
                        lines.extend(get_lines(pos_parts, indent))
                    lines = [prog] + lines

                # join lines into usage
                usage = "\n".join(lines)

        # prefix with 'usage:'
        return "%s%s\n\n" % (prefix, usage)


# fmt: on
class ColorHelpFormatter(ColorHelpFormatterMixin, HelpFormatter):
    pass


class ColorTextWrapper(TextWrapper):
    # modified upstream code, not going to refactor for complexity.
    # fmt: off
    def _wrap_chunks(self, chunks):  # noqa: C901
        """_wrap_chunks(chunks : [string]) -> [string]

        Wrap a sequence of text chunks and return a list of lines of
        length 'self.width' or less.  (If 'break_long_words' is false,
        some lines may be longer than this.)  Chunks correspond roughly
        to words and the whitespace between them: each chunk is
        indivisible (modulo 'break_long_words'), but a line break can
        come between any two chunks.  Chunks should not have internal
        whitespace; ie. a chunk is either all whitespace or a "word".
        Whitespace chunks will be removed from the beginning and end of
        lines, but apart from that whitespace is preserved.
        """
        lines = []
        if self.width <= 0:
            raise ValueError("invalid width %r (must be > 0)" % self.width)
        if self.max_lines is not None:
            if self.max_lines > 1:
                indent = self.subsequent_indent
            else:
                indent = self.initial_indent
            if len(indent) + len(self.placeholder.lstrip()) > self.width:
                raise ValueError("placeholder too large for max width")

        # Arrange in reverse order so items can be efficiently popped
        # from a stack of chucks.
        chunks.reverse()

        while chunks:

            # Start the list of chunks that will make up the current line.
            # cur_len is just the length of all the chunks in cur_line.
            cur_line = []
            cur_len = 0

            # Figure out which static string will prefix this line.
            if lines:
                indent = self.subsequent_indent
            else:
                indent = self.initial_indent

            # Maximum width for this line.
            width = self.width - len(indent)

            # First chunk on line is whitespace -- drop it, unless this
            # is the very beginning of the text (ie. no lines started yet).
            if self.drop_whitespace and strip_color(chunks[-1]).strip() == "" and lines:
                del chunks[-1]

            while chunks:
                # modified upstream code, not going to refactor for ambiguous variable name.
                l = len(strip_color(chunks[-1]))  # noqa: E741

                # Can at least squeeze this chunk onto the current line.
                # modified upstream code, not going to refactor for ambiguous variable name.
                if cur_len + l <= width:
                    cur_line.append(chunks.pop())
                    cur_len += l

                # Nope, this line is full.
                else:
                    break

            # The current line is full, and the next chunk is too big to
            # fit on *any* line (not just this one).
            if chunks and len(strip_color(chunks[-1])) > width:
                self._handle_long_word(chunks, cur_line, cur_len, width)
                cur_len = sum(map(len, cur_line))

            # If the last chunk on this line is all whitespace, drop it.
            if self.drop_whitespace and cur_line and strip_color(cur_line[-1]).strip() == "":
                cur_len -= len(strip_color(cur_line[-1]))
                del cur_line[-1]

            if cur_line:
                if (
                    self.max_lines is None
                    or len(lines) + 1 < self.max_lines
                    or (not chunks or self.drop_whitespace and len(chunks) == 1 and not chunks[0].strip())
                    and cur_len <= width
                ):
                    # Convert current line back to a string and store it in
                    # list of all lines (return value).
                    lines.append(indent + "".join(cur_line))
                else:
                    while cur_line:
                        if strip_color(cur_line[-1]).strip() and cur_len + len(self.placeholder) <= width:
                            cur_line.append(self.placeholder)
                            lines.append(indent + "".join(cur_line))
                            break
                        cur_len -= len(strip_color(cur_line[-1]))
                        del cur_line[-1]
                    else:
                        if lines:
                            prev_line = lines[-1].rstrip()
                            if len(strip_color(prev_line)) + len(self.placeholder) <= self.width:
                                lines[-1] = prev_line + self.placeholder
                                break
                        lines.append(indent + self.placeholder.lstrip())
                    break

        return lines


# fmt: on


class ColorRawDescriptionHelpFormatter(ColorHelpFormatterMixin, RawDescriptionHelpFormatter):
    def _fill_text(self, text, width, indent):
        return super(RawDescriptionHelpFormatter, self)._fill_text(text, width, indent)


class ColorRawTextHelpFormatter(ColorHelpFormatterMixin, RawTextHelpFormatter):
    def _split_lines(self, text, width):
        return super(RawTextHelpFormatter, self)._split_lines(text, width)


class ColorArgumentDefaultsHelpFormatter(ColorHelpFormatterMixin, ArgumentDefaultsHelpFormatter):
    pass


if "MetavarTypeHelpFormatter" in globals():

    class ColorMetavarTypeHelpFormatter(ColorHelpFormatterMixin, MetavarTypeHelpFormatter):
        pass
