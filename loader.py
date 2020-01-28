from staticjinja import Site
import os

SITE_HOST = os.environ.get("SITE_HOST",default=".")
OUTPATH = os.environ.get("OUTPATH",default="../personal-web-out")

if __name__ == "__main__":
    site = Site.make_site(
        env_globals={
            "site_host":SITE_HOST
        },
        searchpath="./templates",
        outpath=OUTPATH,
        staticpaths=["static/"]
    )
    site.render()