# go.py: My python shortlink manager

This is a preliminary shortlink engine, which enables
authenticated users to create and renew shortlinks,
and enables all users to *use* shortlinks.

The basic premise of this is along the lines of,
"I've got a bunch of users who would want to have nice,
customized short links they can share with people, but
I don't want to give up all the good links."  In service
of that idea, this project aims to enable users to request
whatever link they'd like on its subdomain (except /admin\*),
with the caveat that a link has an expiration and must always
be tied to its requester.  Much like a domain, a link expiring
makes it immediately available to new users.

For quick-and-easy use, I also intend to include the ability
to have a unique shortlink generated *for* you, much like
original shortlink functionality.

This program is likely to end up with several sibling
repositories of lower level, moving from python w/flask
to pure python to C++ cgi to C++ server, maybe getting
to a point of pure C server, if I get bored enough
