# CRLF Bruter

A simple tool to test for CRLF injection

# Requirements

`python3 -m pip install requests`

# Usage

**The payloads must start with a slash and there must be no slash at the end of the URLs to be tested.**

usage: crlfbruter.py [-h] (-u URL | -ul URLLIST) (-p PAYLOAD | -pl PAYLOADLIST) [-t THREADS] -hn HEADERNAME [-o OUTPUT]

