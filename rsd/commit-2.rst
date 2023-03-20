RSD 2: commit
=============

:Header: Copyright (c) 2023 bellrise
:Name: commit-2
:Desc: Commit message style
:Revision: 1


Abstract
--------

This document specifies the commit message format.


1. Message
----------

[a] The title is made with 2 parts, a topic and short description::

        <topic>: <description>

Both the topic and description are lowercase without any interpuction. The
topic may be a file name or general topic, like `parser`. If the change affects
everything or some non-code related issue, usually [b] `meta` for the topic is
used.


2. Content
----------

[a] The content of the commit message (below the title line) is basically free
form, but readable English text with real sentences are prefferable.
