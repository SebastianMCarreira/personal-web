# Personal Website

![Personal Website](/templates/static/img/personal-web.png)

### Description

A static site to work as online resume for people to know me. Also, this makes my website a recursive website. Which I think it's a pretty cool to say.

</div>

</div>

</div>

<div class="section">

### How it's deployed


![Diagram](/templates/static/img/personal-web-diagram.jpg)


1.  A commit to the CodeCommit repository master branch triggers the CodePipeline workflow.
2.  CodeBuild transforms the templates into the static html files. Also css and js is minified to reduce storage footprint and page load time.
3.  CodeDeploy sends the static files to the bucket test.sebastiancarreira.com where it's served as a S3 static website.
4.  I manually check the test website for errors in the public bucket URL. Once everything is checked, the pipeline continues.
5.  CodeDeploy sends the static files to the bucket me.sebastiancarreira.com where it's served as a S3 static website.
6.  A Route 53 hosted zone maps the me.sebastiancarreira.com name to the me.sebastiancarreira.com bucket public URL name.
7.  CloudFront keeps cached the static content of the site for quick loads in other parts of the world.
8.  S3 maps the me.sebastiancarreira.com bucket public URL to the static site served by it.

### Services & Technologies Used

*   Route 53
*   CloudFront
*   S3
*   CodePipeline
*   StaticJinja
*   Apache (for local development tests)


### Why did I make a static website in 2020?

Nowdays, with frameworks like Flask or Express.js, one can make a dynamic website in mere minutes, literally. All with templates and fetching data from some database. So, why doing a static website today? It sounds so vintage sometimes. But people sometimes forget the strengths of static websites and underestimate the costs of keeping a dynamic website running.

Since all of my content is running in AWS. I need to be smart to keep my costs as low as possible (and within the free tier, if possible) while making my content always available. A dynamic website running 24/7/52 would mean having (at least) one EC2 instance running an application all that time, something which consumes all of the free tier credit for EC2 (making anything else I do over the month with EC2 cost money) or adds like $8 a month to my costs. And that's not even mentioning auto scaling in case of high demand. I could also go serverless and use Lambda, but I also want to play with it and use Lambda for many other things where serverless actually excells, and using it to handle the backend for this website would mean I risk going over my free tier limit too.

Regardless of that, the main question is the following: Is the content static or dynamic? The answer is kind of relative. The site content will definetly change over time. I will add new projects, update existing ones, and probably change some things in the Home and Resume sections. But all of those changes will be done by me, both the sole owner of the site and someone who likes to write documents in HTML. Also, almost no information appears in two places of the site, using placeholders to insert that data would help very little. So, if I made this site dynamic, I would earn the ability to edit (some of) its content in a "friendlier" UI and maybe some data won't be duplicated. On the other hand, I'm getting the trouble of mantaining a backend to serve the site, and that comes not only with costs, but with security implications too.

So I choosed to make the site static. AWS offers the ability to serve a static website straigth from a S3 bucket and the only things that you get charged for are the storage it uses, the GET requests users perform, and the PUT requests I perform. Additionally, CloudFront helps to make the site quick and available in other parts of the world for international visitors. Security is also handled by AWS, I just have to set up the bucket's policy to the standard for hosting a public static website and I won't have to worry who has access to what of my site (other than the security concerns of managing an AWS account).

*   Storage: this is almost laughable. AWS charges S3 storage by GB and it literally charges a few cents per GB stored. This website will probably never weight more than 2MB, that's less than .2% of the storage I will have to pay to even use S3\. And if we are talking about the free tier, I get 5GB for free for the first 12 months, so I'm not even paying for that at the moment.
*   GET Requests: Visitors will use up this resource over time. However, the requests are counted by the literal thousands and AWS charges like $0.0005 per 1000 GET. That's really low, at least for a small website with very few monthly visitors like this one. I would need like 18000 GET requests to reach just 1% of what I'm paying for the domain, I'm pretty sure I won't reach those numbers for a long time. Meanwhile, the free tier covers the first 20000 GET requests for the first 12 months. In addition to all this, CloudFront will cache most of these requests anyway.
*   PUT Requests: I will use these to update the site. However, we are talking about less than 50 PUT requests per update, while these are also charged by the thousand ($0.0007 per 1000 PUT). So I would have to update this site 20 times a month to even get above 1 cent, and I won't update it so many times. The AWS free tier also covers the first 2000 PUT for the first 12 months.
*   CloudFront: Making possible visitors from other parts of the world (anywhere but South America, where the site is currently hosted) wait for the data to be transferred from there to their geographical location is inadmissible. For this, CloudFront will keep cached the site in other AWS sites, shortening the distance between my possible international visitors and this website's content. CloudFront is not that cheap, but because this site is actually pretty small I know this site will stay below the first GB of transfer, meaning something like $0.085 a month. HTTP requests will also not go above the first 10000 (at least for a long time) so I will have to pay around $0.0075 per month for that.

### Why StaticJinja and not some other more popular SSG like Hugo or Jekyll?

The short answer is, I didn't want to learn how to use them for this.

I love learning about technology. But learning a new framework is usually pretty cumbersome, while SSG aren't exactly very exciting to learn (at least for me). I never used one before making this site, all of my experience making websites was with dynamic websites or literally one page. So I went to the Internet looking what SSG should I use, how to use them and so on. I started a Hugo tutorial and began scaffolding this page but, while I was reading documentation I tought "Why can't I use something like Jinja in Flask, that takes some templates and outputs the html files like that?". So I googled "static site generator jinja" and one of the first links was the [StaticJinja](https://github.com/Ceasar/staticjinja) repository in GitHub, the first 3 paragraphs of its README were literally what I was thinking about:

> StaticJinja is a library that makes it easy to build static sites using Jinja2.
> 
> Many static site generators are complex, with long manuals and unnecessary features. But using template engines to build static websites is really useful.
> 
> StaticJinja is designed to be lightweight (under 500 lines of source code), and to be easy to use, learn, and extend, enabling you to focus on making your site.

Using it was extremely easy. The documentation is straightfoward and it had all the features I needed. It's not perfect (I'm thinking about contributing) but it get's the job done. Also, I could use all of the Jinja syntax I'm so familiar with from working with Flask and Django.

In the end, all SSG output the same stuff, a bunch of HTML files (and maybe other static files too). Coming from Hugo or StaticJinja won't make it look much different.
