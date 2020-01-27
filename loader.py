from staticjinja import Site

if __name__ == "__main__":
    site = Site.make_site(
        env_globals={
            "site_host":"file:///C:/Users/Sebastián/Desktop/Coding/personal-web-out"
        },
        searchpath="./templates",
        outpath="../personal-web-out",
        staticpaths=["static/"]
    )
    site.render()