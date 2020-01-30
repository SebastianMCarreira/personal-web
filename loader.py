from staticjinja import Site
import os

OUTPATH = os.environ.get("OUTPATH",default="../personal-web-out")
APPVERSION = os.environ.get("APPVERSION",default="testBuild")
ISLOCALDEV = bool(os.environ.get("ISLOCALDEV", default=True))

if __name__ == "__main__":
    site = Site.make_site(
        env_globals={
            "app_version":APPVERSION,
            "abs_path": os.path.abspath(OUTPATH) if ISLOCALDEV else ""
        },
        searchpath="./templates",
        outpath=OUTPATH,
        staticpaths=["static/"]
    )
    site.render()