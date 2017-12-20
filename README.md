# u
Use GitHub Pages as a URL shortener (even with a custom domain!). No backend necessary. U provides a command line interface to shorten URLs, then host them on your local GitHub Pages instance.

## Installation & Usage
```sh
$ pip install u-github-pages

# u <url> <optional:shortcode> - Generates shortened URL
$ u https://twitter.com/niraj tw-niraj
# Shortened URL now live at http://niraj.io/u/tw-niraj

# u all - View all previous shortened URLs
$ u all

# u setup <domain> - Set default domain
$ u setup http://niraj.io
```

## License
[MIT License](LICENSE)
