import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from routers import apportionment, itemized_taxes, unemployment_county

load_dotenv()

app = FastAPI()
trusted_origins = os.getenv("ALLOWED_ORIGINS").split(",")
# trusted_hosts = os.getenv("ALLOWED_HOSTS").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=trusted_origins,
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"]
)
# app.add_middleware(TrustedHostMiddleware, allowed_hosts=trusted_hosts)
app.include_router(apportionment.router)
app.include_router(itemized_taxes.router)
app.include_router(unemployment_county.router)


@app.get("/", response_class=RedirectResponse, status_code=302)
async def root():
    """
    Redirect to the documentation page for understanding of all routes and usage
    :return: Redirect
    """
    return os.getenv("DOMAIN_NAME") + "docs"
