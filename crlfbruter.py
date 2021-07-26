import threading as th
import queue
import argparse as ap
import requests as r

from requests.packages.urllib3.exceptions import InsecureRequestWarning
r.packages.urllib3.disable_warnings(InsecureRequestWarning)


def loadList():
    
    print('Building URLs to test. Please, wait...')
    wordqueue = queue.Queue()

    if args.url and args.payload:
        if not urllist.startswith('http'):
            wordqueue.put(['http://' + urllist, payloadlist])
        else:
            wordqueue.put([urllist, payloadlist])
    elif args.urllist and args.payload:
        for url in args.urllist:
            if not url.startswith('http'):
                wordqueue.put(['http://' + url.strip(), args.payload])
            wordqueue.put([url.strip(), args.payload])
    elif args.url and args.payloadlist:
        for payload in args.payloadlist:
            if not args.url.startswith('http'):
                wordqueue.put(['http://' + args.url, payload.strip()])
            wordqueue.put([args.url, payload.strip()])
    elif args.urllist and args.payloadlist:
        for url in args.urllist:
            for payload in args.payloadlist:
                if not url.startswith('http'):
                    wordqueue.put(['http://' + url.strip(), payload.strip()])
                wordqueue.put([url.strip(), payload.strip()])

    return wordqueue

def bruter(wordqueue, headername):
    while not wordqueue.empty():
        url, payload = wordqueue.get()
        attempt = url + payload

        print(f'Trying {attempt}...' + ' '*30, end='\r')

        try:
            resp = r.get(attempt, verify=False, allow_redirects=False)
            
            eheader = resp.headers[headername]
            if eheader != '':
                print(f'[+] URL {url} is vulnerable with the payload {payload}')
                
        except KeyError:
            pass
        except KeyboardInterrupt:
            print('Tarefa cancelada pelo usuário...')
            exit(0)
        except ConnectionError:
            print('Erro de conexão...')
        except Exception as e:
            print(e)
        wordqueue.task_done()

if __name__ == '__main__':
    parser = ap.ArgumentParser(description='A tool for testing CRLF injection')
    urlgroup = parser.add_mutually_exclusive_group(required=True)
    urlgroup.add_argument('-u', '--url', 
        help='One URL to be tested.')
    urlgroup.add_argument('-ul', '--urllist', 
        help='A file containing a list of URLs to be tested.', type=ap.FileType(mode='r', encoding='latin'))
    payloadgroup = parser.add_mutually_exclusive_group(required=True)
    payloadgroup.add_argument('-pl', '--payloadlist', type=ap.FileType(mode='r', encoding='latin'),
        help='A file containing a list of payloads to be tested.')
    payloadgroup.add_argument('-p', '--payload', type=ap.FileType(mode='r', encoding='latin'),
        help='One payload to be used.')
    parser.add_argument('-t', '--threads', default=1, type=int, 
        help='The number of threads to be used. Default is 1.')
    parser.add_argument('-hn', '--headername', type=str, 
        help='The name of the fake header.', required=True)
    args = parser.parse_args()

    if args.url and not args.url.startswith('http'):
        args.url = 'http://'+args.url
    
    wordqueue = loadList()

    for _ in range(args.threads):
        th.Thread(target=bruter, 
            args=(wordqueue, args.headername)).start()

    wordqueue.join()
    print('All URLs and payloads have been tested.' + ' '*30)
