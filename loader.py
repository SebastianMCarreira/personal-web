from staticjinja import Site
import os

OUTPATH = os.environ.get("OUTPATH",default="../personal-web-out")

if __name__ == "__main__":
    site = Site.make_site(
        searchpath="./templates",
        outpath=OUTPATH,
        staticpaths=["static/"]
    )
    site.render()