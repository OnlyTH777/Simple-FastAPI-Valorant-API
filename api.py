from fastapi import FastAPI

app = FastAPI()


@app.get('/agents')
async def root():
    agents = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 'Fade', 'Harbor', 'Jett', 'KAY/O', 'Killjoy', 'Neon', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']
    return agents


@app.get('/agentsIds')
async def root():
    agentsIds = {
        'Astra': '41FB69C1-4189-7B37-F117-BCAF1E96F1BF',
        'Breach': '5F8D3A7F-467B-97F3-062C-13ACF203C006',
        'Brimstone': '9F0D8BA9-4140-B941-57D3-A7AD57C6B417',
        'Chamber': '22697A3D-45BF-8DD7-4FEC-84A9E28C69D7',
        'Cypher': '117ED9E3-49F3-6512-3CCF-0CADA7E3823B',
        'Fade': 'DADE69B4-4F5A-8528-247B-219E5A1FACD6',
        'Harbor': '95B78ED7-4637-86D9-7E41-71BA8C293152',
        'Jett': 'ADD6443A-41BD-E414-F6AD-E58D267F4E95',
        'KAY/O': '601DBBE7-43CE-BE57-2A40-4ABD24953621',
        'Killjoy': '1E58DE9C-4950-5125-93E9-A0AEE9F98746',
        'Neon': 'BB2A4828-46EB-8CD1-E765-15848195D751',
        'Omen': '8E253930-4C05-31DD-1B6C-968525494517',
        'Phoenix': 'EB93336A-449B-9C1B-0A54-A891F7921D69',
        'Raze': 'F94C3B30-42BE-E959-889C-5AA313DBA261',
        'Reyna': 'A3BFB853-43B2-7238-A4F1-AD90E9E46BCC',
        'Sage': '569FDD95-4D10-43AB-CA70-79BECC718B46',
        'Skye': '6F2A04CA-43E0-BE17-7F36-B3908627744D',
        'Sova': 'DED3520F-4264-BFED-162D-B080E2ABCCF9',
        'Viper': '707EAB51-4836-F488-046A-CDA6BF494859',
        'Yoru': '7F94D92C-4234-0A36-9646-3A87EB8B5C89'}
    return agentsIds


@app.get('/')
async def root():
    message = "Simple Valorant API"
    return message
