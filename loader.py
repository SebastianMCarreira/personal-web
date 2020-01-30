from staticjinja import Site
import os

OUTPATH = os.environ.get("OUTPATH",default="../personal-web-out")
APPVERSION = os.environ.get("APPVERSION",default="testBuild")
SITEPATH = os.environ.get("SITEPATH", default=os.path.abspath(OUTPATH))

if __name__ == "__main__":
    site = Site.make_site(
        env_globals={
            "app_version":APPVERSION,
            "site_path": SITEPATH
        },
        searchpath="./templates",
        outpath=OUTPATH,
        staticpaths=["static/"]
    )
    site.render()