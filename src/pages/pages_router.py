from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.operations.truth_router import get_truths_containing_text

pages_router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")


@pages_router.get("/base")
def get_base_template(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@pages_router.get("/searchTruth/{text_to_search}")
def get_search_template(request: Request, truths=Depends(get_truths_containing_text)):
    return templates.TemplateResponse("searchTruths.html", {"request": request,
                                                      "truths": truths["data"]})


@pages_router.get("/")
def get_search_template(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})\
