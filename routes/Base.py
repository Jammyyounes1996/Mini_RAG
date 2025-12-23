from fastapi import FastAPI
app = FastAPI() #creat object from fasatapi
@app.get("/")#انا عملت ديكوريتور من الفانكشن الاساسيةيحث لما حد يطلب ال يو ار ال بتاعى وفى اخره الجملة دى يروح ينفذ ال 
def welcom (): #creat funcation his name 'welcom' whan user calling via api return dictunary contain spacific massage.
    return {
            "message":"Hellow Api"
    }

    
