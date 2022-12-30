from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI(
    title='GoLinks'
)

class GoLink(BaseModel):
    short: str
    full: str
    created_by: str
    updated_by: str

@app.get('api/v1/links')
async def list_links(start: int, end: int):
    return  {
        'links': [
            {
                'short': 'google',
                'full': 'https://google.com'
            }
        ]
    }

@app.put('api/v1/links/{link_id}')
async def upsert_link(link_id: str, go_link: GoLink):
    pass

@app.delete('api/v1/links/{link_id}')
async def remove_link(link_id: str):
    pass

@app.get('/', response_class=HTMLResponse)
async def display_links(q: str = ""):
    return """
        <h1>hello world</>
    """

@app.get('/{short_url}', response_class=RedirectResponse)
async def redirect_short_url(short_url: str):
    return "https://google.com"
