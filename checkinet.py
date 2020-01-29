try:
    import httplib
except:
    import http.client as httplib

def have_internet():
    conn = httplib.HTTPConnection("www.uni-heidelberg.de", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        print('ok')
        return True
    except:
        conn.close()
        print ('offline')
        return False
have_internet() 
