#!/usr/bin/env python3

"""
pycc/detail/stage.py -- Pipeline stage.

"""

################################################################################
## Pipeline interfaces
##

class pipeline_stage(object):
    """
    Phases in the compiler toolchain are modeled in the form of a pipeline.
    This class describes the interface that such a pipeline stage would
    follow.

    """
    def __init__(self, source):
        """
        Initializes this pipeline stage with a source pipeline stage.

        """
        self._source = source


    @property
    def source(self):
        """
        Returns the source for this pipeline stage.

        """
        return self._source


    def __next__(self):
        """
        Process and return the next unit of computational result. When no more
        units can be generated, StopIteration is raised. Implementations are
        expected to acquire the next item(s) from the source, accumulating
        enough items to make the computation, and then return the result.

        """
        pass


################################################################################
## Common helpers
##

class line_reader(pipeline_stage):
    """
    Reads contents from a file line-by-line.

    """
    def __init__(self, file):
        """
        Instantiate a reader that reads lines from `file`.

        """
        self._file = file
    

    def __iter__(self):
        """
        Returns an iterator that returns lines from the associated file.

        """
        return iter(self._file)


def pipe_to_file(pipeline, file):
    """
    Writes the results of the pipeline to the given file. Results are expected
    to have a representation that can be written to a file.

    TODO[susmits]: This will probably see some rework.

    """
    for result in pipeline:
        file.write(result)


################################################################################
