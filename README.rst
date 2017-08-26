ImageSifter
==============================

**Easy-to-use package for downloading originals of images from
web sites such as Instagram, Google Images, Flickr etc.**

Download
########

pip install (recomended) :
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    $ pip install imagesifter

Git clone:
~~~~~~~~~~~~~~~~
.. code:: sh

    $ git clone https://github.com/HedonistAnt/ImageSifter.git



Usage
#####

.. code:: py

    import imagesifter
    import urllib

    quote = 'sifter'
    quoteURL = urllib.quote(quote)
    url = 'http://images.google.com/images?hl=ru&q=' + quoteURL + '&sa=N&start=$p&ndsp=20&sout=1'
    imagesifter.sift_images(url=url, format_list=["jpg", "jpeg", "png"], download_path='img', size_limit=10000000,
                          count_limit=10)


*Note:*
*New folder will be created in current directory. Default folder name is "images". The maximum file size (size_limit) is in bytes.*

Errors and solutions
####################

If you have lxml error: 'DLL load failed' on Windows, just install unoffical build from http://www.lfd.uci.edu/~gohlke/pythonlibs/
