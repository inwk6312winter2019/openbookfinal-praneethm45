def ipreq():
    mopen = open("access.log","r")
    firefox = []
    chrome = []
    x = []
    for mp in mopen:
        if "Firefox/" in mp:
            firefox.append(mp)
        elif "Chrome/" in mp:
            chrome.append(mp)
        else:
            x.append(mp)
    print("No of request per browser:")
    print("Firefox",len(firefox))
    print("Chrome",len(chrome))
    print("x",len(x))

ipreq()
