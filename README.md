# Selenium script that purges your instagram account

## steps:
* archive every post you want to keep (post->menu->archive)
* modify settings.json
  * username: your username
  * password: your password
  * posts: # of posts to delete
  * slowness: adds a multiplier to sleep functions, 1.5 was about right for me on a 8250U and 150Mbps
* install selenium and firefox: `pacman -S firefox geckodriver`
* `pip install selenium --user`
* `python app.py`
