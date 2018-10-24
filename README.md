# Template Static Website
This is a template website using [Pelican](http://docs.getpelican.com/en/stable/index.html). You can get it working, make it your own and publish it in less than an hour.

See the demo [here](https://otso-andersen.github.io/website-template-pelican/).

## I) How to install 

Here's how to install and run it on your own:

### 1. Install git and pip (if not currently installed):

Run the following command in your preferred terminal, prefixing with sudo if permissions warrant:

```bash
sudo apt-get install git
sudo apt-get install python-pip
```

### 2. Install Pelican, Markdown and PyCrypto:

```bash
pip install pelican markdown pycrypto
```
(pycrypto is for using [pelican-encrypt-content
](https://github.com/mindcruzer/pelican-encrypt-content), a plugin that allows you to write password protected articles)

### 3. Copy this repository (git clone source code):

First, choose a name for your project, create an appropriately-named directory for your site, and switch to that directory

```bash
mkdir -p ~/path_to_my_folder
cd ~/path_to_my_folder
git clone https://github.com/otso-andersen/website.git
```

### 4. Generate the site:

From your site directory, run the `pelican` command to generate your site:

```bash
pelican content
```

This create a folder `output` with the generated website. 

Alternatively, you can use the `make` command:

```bashrc
make html
```

### 5. Preview your site:

Open a new terminal session and run the following commands to switch to your output directory and launch Pelican’s web server:

```bash
cd ~/path_to_my_folder/website/output
python -m pelican.server
```
Preview your site by navigating to http://localhost:8000/ in your browser.

If you’d prefer to have Pelican automatically regenerate your site every time a change is detected (which is handy when testing locally), the best way is to use the following `make` command instead:

```bashrc
make devserver
```
The above command will simultaneously run Pelican in regeneration mode as well as serve the output at http://localhost:8000. Once you are done testing your changes, you should stop the development server via (after `ctrl+C`):
```bashrc
./develop_server.sh stop
```


## II) How to write content

### 1. Write an article

Use your preferred text editor to create your first article with the following content:

```markdown
Title: My article title

This is the content of my article
```

This is as simple as that! Given that this example article is in Markdown format, save it as `~/path_to_my_folder/website/content/myarticle.md`.  
You can learn how to write in Mardown in 5 min, for example [here](https://en.wikipedia.org/wiki/Markdown#Example).

`Title` is the only required metadata. Other options can be passed:

```markdown
Title: My article title
Status: draft / published (default)
SubTitle: My subtitle will only appear on the article page [this is a theme metadata]
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: My Category
Tags: tag 1, tag 2
Slug: my-super-post [the article will have an url as websiteadress/category/slug, if not specified the slug is autogenerated from the title]
Authors: author 1, author 2, author 3
Summary: Short version for index and feeds
Lang: fr (en is default)
Cover: path/to/image (or link to an image on the web) [this will appear on the article page - this is a theme metadata]
Thumbnail: path/to/image (or link to an image on the web) [this will appear on the category page - this is a theme metadata]
Password: thisIsMyPassword [this works with pelican-encrypt-content]
```
Theme metadata are metadata that are not directly understood by Pelican but are specific to the theme used in that particular blog and would not be used should you change the theme.   
You don't need to supply a Cover or Thumbnail in your posts, but category pages will look better if you supply Thumbnail in all of your posts.

For more information on how to write content see the [Pelican documentation](http://docs.getpelican.com/en/stable/content.html).

### 2. Difference between articles and pages

Pelican considers “articles” to be chronological content, such as posts on a blog, and thus associated with a date.

The idea behind “pages” is that they are usually not temporal in nature and are used for content that does not change very often (e.g., “About” or “Contact” pages). 

Write your pages inside the folder `content/pages`.  
Write your articles inside the folder `content/category_name`, where `category_name` is the name of your article category. This will automatically generate the category of your article (you don't have to write `Category: My Category`inside the file).  

### 3. How to include images

If you want to include images, put them inside a folder `content/images` or inside `content/category_name` (or wherever you want really, as long as it is inside `content`).  
Then copy this line inside `pelicanconf.py`, with the appropriate names of your categories:
```python
STATIC_PATHS = ['images', 'category_name','another_category_name']
```

To add your image to your article, link to it where you want it to appear inside the markdown file:

```markdown
![alt-text for the picture](../category_name/picture.jpg)
```

## III) Customize the settings

### 1. pelicanconf.py

* Change the name of your website, the author and the quote on the home page:
```python
AUTHOR = u'John Smith'
SITENAME = u'name'
SITESUBTITLE = u'To see a World in a Grain of Sand And a Heaven in a Wild Flower'
SITEURL = ''
```

* If you want your article to have `Status: draft`by default (instead of being published), add this line of code inside pelicanconf.py:
```python
# By default, new articles will be drafts. To publish them, add [Status: published] to its .md
DEFAULT_METADATA = {
    'status': 'draft',
}
```

* Special Theme settings:

To change the picture appearing on the home page:
```python
THEME_HEADERPICTURE = SITEURL + 'images/header_photo.png'
```
To add a description, a logo to your categories (and a default thumbnail for the articles of that categories):
```python
THEME_CATEGORIES = {
    'Category Name': {
        'description': 'this description will appear at the bottom of every article page from that category',
        'logo': SITEURL + '/category_1/logo.png',
        'thumbnail': SITEURL + '/category/picture.jpg',
    }
}
```
To add information about the authors contributing to your blog:
```python
THEME_AUTHORS = {
    'John Smith': {
        'description': """
            The lion is in the contract.
        """,
        'cover': 'https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e002152/GSFC_20171208_Archive_e002152~orig.jpg',
        'image': SITEURL + '/images/picture.jpg',
        'links': (('github', 'https://github.com/otso-andersen'),
                  ('twitter-square', 'https://twitter.com/oasln')),
    }
}
```
Links must be a list of tuples. [Font Awesome](https://fontawesome.com/) is used for the link icons. First element must contain the name of the icon without fa prefix (see fontawesome.com) and second element must be URL for this icon.

### 2. Theme

The theme itself is a modified version of [Medius](https://github.com/onur/medius) and can be changed by accessing the folder `theme`.

If you want to change the appearance of your website, this is where to go.

For more information, see the Pelican documentation: [creating themes](http://docs.getpelican.com/en/stable/themes.html).

## IV) Publish your website

### 1. publishconf.py

```python

```

### 2. Publish on GitHub Pages

For more information on this process, see [how to publish on GitHub](http://docs.getpelican.com/en/stable/tips.html#publishing-to-github) and [GitHub Pages](https://pages.github.com/).

We use [ghp-import](https://github.com/davisp/ghp-import) to automatically add commits using the output folder:

```bash
pip install ghp-import
```

If not already the case, you have to initialize git inside your folder:
```bash
git init
```

Go to [GitHub Pages](https://pages.github.com/ and follow the procedure to create a GitHub page.

Then, for a User page, do:

```bash
make publish
ghp-import output
git remote add origin git@github.com:username/username.github.io.git
git push origin gh-pages:master
```

Or for a Project page, use:

```bash
make publish
ghp-import output
git remote add origin git@github.com:username/project.git
git push origin gh-pages
```

This only publishes the generated output folder of your website. In particular, this ensures that all your password protected articles are safe, even if hosted on a public repository (the generated content is hashed).

If you want, you can create an alias in `.bashrc` to do this process more efficiently:

```
alias generate="pelican content -o output -s pelicanconf.py"
alias publish="make publish && ghp-import output && git push origin gh-pages:master"
```
















     
