---
title: Static Websites
tags: [Cheatsheet, WebDev, Software]
style: border
color: primary
description: Jekyll, Liquid, WSL, Hosting and CDN
---

## Jekyll Webiste Creation
1. WSL Setup: Use `wsl --install` in PowerShell as admin, then install a Linux distribution from Microsoft Store.
2. Install Jekyll and Bundler: `gem install jekyll bundler`
3. Create New Site: `jekyll new my-site`
4. Build Site: `bundle exec jekyll build`
5. Serve Site Locally: `bundle exec jekyll serve`

## Git and GitHub
* Initialize Repository: `git init`
* Stage Changes: `git add .`
* Commit Changes: `git commit -m "commit message"`
* Push to GitHub: `git push origin master`
* Pull from GitHub: `git pull origin master`
* Revert to Previous Commit:
    * `git reset --hard [commit-hash]` for local changes.
    * `git revert [commit-hash]` for shared repositories.

## Cloudinary for Image Hosting
* Upload Images: Upload images to Cloudinary to get URLs.
* Embed Images: Use Cloudinary URLs in HTML with `<img src="cloudinary-url">`.

## Jekyll Customization
* Fork theme and update config to make more substantial changes.
* Modify HTML/CSS: Edit files in _layouts, _includes, and _sass.

## Liquid Templating
![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/f_auto,q_auto/v1/portfolio-site/notes/zm5dzlu5i7axxzxzucqb "Screenshot of liquid code")

<!-- ```liquid
* For Loops: {% for item in collection %}...{% endfor %}
* If Statements: {% if condition %}...{% endif %}
* Variables: {% assign variable = value %}
``` -->

## WSL (Windows Subsystem for Linux)
* Check Status: `wsl -l -v`
* Restart WSL: `wsl --shutdown` then restart the desired distribution.
* High Vmmem usage after hibernating PC:
    * Restart WSL

## Using CDN
* Cloudflare Setup:
    * Update DNS to point to Cloudflare.
    * Configure CDN settings in Cloudflare dashboard.
* CDN Benefits: Faster content delivery, reduced server load, DDoS protection.
