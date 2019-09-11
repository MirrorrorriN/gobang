def buildSuccess(data):
    resp={}
    resp['data']=data
    resp['errno']=0
    resp['errmsg']='succ'
    return resp

def buildFail(e):
    resp={}
    resp['errno']=9999
    resp['errmsg']=str(e)
    return resp