RSD 1: rsd
==========

:Header: Copyright (c) 2023 bellrise
:Name: rsd-1
:Desc: Reference Specification Documents
:Revision: 1


Abstract
--------

This document describes how RSDs (Reference Specification Documents) should be
formed. When a specification arises in mini-rose, it is defined using a RSD and
moved into the mini-rose/docs repository. Regular program documentation is
still written in regular reStructuredText without any specific rules. RSDs must
be very specific in what they define, so here is a couple rules that must be
adhered to.


1. Layout
---------

[a] The document is written in reStructuredText format, which allows for
in-place reading and generating HTML pages from it. The first two lines contain
the name and index number of the document::

        RSD <number>: <name>
        ====================

[b] After the title, some metadata is required to easily identify the document,
like the header with copyright information, field with the full RSD name along
with a description. Additionally, any changes in the document requires that the
author increments a "Revision" counter so that a user will know exactly what
version of the spec is used::

        :Header: Copyright (c) <year> <author>
        :Name: <name>-<id>
        :Desc: <short description>
        :Revision: <number>

[c] After the metadata block, an "Abstract" is required summarizing the
document itself. You may read the abstract in this document to get an idea of
what it might look like.

[d] The following sections should be numbered starting from 1, representing
differing concepts::

        1. Concept
        ----------

[e] Each concept may have subsections, marked with square brackets and a lower
case letter from the English alphabet, starting from a. If you run out of
letters, the next subsections after 'z' should be named 'aa', 'ab' and so on::

        [a] <text>
        [b] <text>
        ...
        [z] <text>
        [aa] <text>
        [ab] <text>
        ...


2. Referencing
--------------

You may reference a certain subsection in code in a comment by providing a
relevant ID, which may be represented in 2 forms::

        /* RSD 3/2a */
         or
        /* RSD cmdline/2a */
