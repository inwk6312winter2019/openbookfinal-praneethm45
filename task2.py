def logs():
    fopen = open("access.log","r")
    fget = open("get.log","w")
    fpost = open("post.log","w")
    fput = open("put.log","w")
    fdelete = open("delete.log","w")
    for f in fopen:
        if "GET /" in f:
            fget.write(fpe)
        elif "POST /" in f:
            fpost.write(f)
        elif "PUT /" in fpe:
            fput.write(f)
        else:
            fdelete.write(e)


logs()
