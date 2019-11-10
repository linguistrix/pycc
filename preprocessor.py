#!/usr/bin/env python3

"""
pycc/preprocessor.py -- Preprocess C source.

"""

from .detail.stage import pipeline_stage, line_reader

###############################################################################
## Preprocessor stages
##

# The C preprocessor is made up of multiple phases, which are invoked in this
# order:
#  - Trigraph replacement
#  - Line splicing
#  - Comment removal (in fact, replacement with a single space)
#  - Preprocessing directives
#  - Escape sequence replacement
#  - 
#
# We've written a pipeline_stage for each of the above phases. These are
# finally chained to create a preprocessor, and combined with a source and a
# sink.
#

class replace_trigraphs(pipeline_stage):
    pass


class splice_lines(pipeline_stage):
    pass


class remove_comments(pipeline_stage):
    pass


class apply_directives(pipeline_stage):
    pass


class substitute_escape_sequences(pipeline_stage):
    pass


###############################################################################
## Preprocessor pipeline
##

def make_preprocessor(source_file, defines=[], user_include_dirs=[],
    system_include_dirs=[]):
    """
    Creates a pipeline for preprocessing `source_file`. `defines` is a list of
    preprocessor definitions provided via the command line. Each element in
    `defines` is a tuple containing 1 element (for -DSYMBOL definitions) or 2
    elements (for -DSYMBOL=value definitions).

    """
    return substitute_escape_sequences(
        apply_directives(
            remove_comments(
                splice_lines(
                    replace_trigraphs(
                        line_reader(source_file)
                    )
                )
            )
        )
    )


###############################################################################
## Entry point
##

if __name__ == "__main__":
    # TODO: Write an argparse instance that accumulates arguments of -I,
    # -D, and -isystem types, passes them to make_preprocessor, and runs it
    # on the input file.
    pass


###############################################################################
