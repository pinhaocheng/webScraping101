function main(splash, args)
    headers = {
      ['Accept-Language'] = 'en-US,en',
      ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    splash:set_custom_headers(headers)
    assert(splash:go(args.url))
    assert(splash:wait(0.5))
    return splash:html()
  end