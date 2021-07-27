# CRLF Bruter

A simple tool to test for CRLF injection

# Requirements

`python3 -m pip install requests`

# Usage

**The payloads must start with a slash and there must be no slash at the end of the URLs to be tested.**

usage: crlfbruter.py [-h] (-u URL | -ul URLLIST) (-p PAYLOAD | -pl PAYLOADLIST) [-t THREADS] -hn HEADERNAME [-o OUTPUT]

A tool to test for CRLF injection

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     One URL to be tested.
  -ul URLLIST, --urllist URLLIST
                        A file containing a list of URLs to be tested.
  -p PAYLOAD, --payload PAYLOAD
                        One payload to be used.
  -pl PAYLOADLIST, --payloadlist PAYLOADLIST
                        A file containing a list of payloads to be tested.
  -t THREADS, --threads THREADS
                        The number of threads to be used. Default is 1.
  -hn HEADERNAME, --headername HEADERNAME
                        The name of the fake header.
  -o OUTPUT, --output OUTPUT
                        A file to save the results for the vulnerable targets.
