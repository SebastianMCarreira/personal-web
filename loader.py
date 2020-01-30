from staticjinja import Site
import os

OUTPATH = os.environ.get("OUTPATH",default="C:\inetpub\wwwroot")
APPVERSION = os.environ.get("APPVERSION",default="testBuild")

if __name__ == "__main__":
    site = Site.make_site(
        env_globals={
            "app_version":APPVERSION
        },
        searchpath="./templates",
        outpath=OUTPATH,
        staticpaths=["static/"]
    )
    site.render()