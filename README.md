# u
Use GitHub Pages as a URL shortener (even with a custom domain!). No backend necessary. U provides a command line interface to shorten URLs, then host them on your local GitHub Pages instance.

## Installation & Usage
```
pip install u-github-pages
u https://twitter.com/niraj tw-niraj  # u <url> <optional:shortcode> - Generates shortened URL
# Shortened URL now live at http://niraj.io/u/tw-niraj
u all # u all - View all previous shortened URLs
u setup http://niraj.io # u setup <domain> - Set default domain
```

## License
[MIT License](LICENSE)
