from staticjinja import Site

if __name__ == "__main__":
    site = Site.make_site(
        env_globals={
            "site_host":"."
        },
        searchpath="./templates",
        outpath="../personal-web-out",
        staticpaths=["static/"]
    )
    site.render()