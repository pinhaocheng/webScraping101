function main(splash, args)
    headers = {
      ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
      ['cookie'] = 'AKAM_CLIENTID=5dbdfdaa1a6c037d49fc21ec16f23ebb; ak_bmsc=650ECF01D1F2F4C0F4B54BEC69773727ACE80336C74900003A9AC15ED880A146~plS8phw8h/qv3D72dDTEZKebbWXUiyJJOqvTs37CTkySXXWrLF6lLy9A3gZqBOYYYqWXHvp6ageW40p248V6EX9L1BGm83d4j8BUfyB7ntGKzQuriWcep5u2ZRExzVwoHzIou86yyon5X0r1AIldRnjB+sAUR6zLjmXmHdx68lUQFDN8rouxKuXoFxNEUNjS4UrpfR6HGExCP+dGxZzup8trhqzC0OTmD5vgSd39jYAnI=; gb_lang=en; gb_pipeline=GB; cdn_countryCode=US; gb_currencyCode=USD; _gcl_au=1.1.877717706.1589746237; WEBF_guid=5dbdfdaa1a6c037d49fc21ec16f23ebb_1589746237; WEBF_predate=1589746237; aff_mss_info_bak={"bak":"bak"}; gb_countryCode=US; landingUrl=https://www.gearbest.com/flash-sale.html; _ga=GA1.2.1177086252.1589746239; _gid=GA1.2.1923712058.1589746239; _uetsid=7c8eca13-1f4f-fbab-c8f5-ea184d07454e; gb_vsign=a2cb64c41d5e3562e3618c5733fdce9ce6e1c01a; _fbp=fb.1.1589746242777.1788909896; gb_fcm=0; gb_fcmPipeLine=GB; gb_soa_www_session=eyJpdiI6InJ2MEJXa2JwSFJLcTQrZ3FENTh4Tnc9PSIsInZhbHVlIjoic0JUcktMeHBlK05pZ3NIZVRJc2w5RU1TcmZ0SmRVc3o3M0I2TTdSVVFVMjNWaUpPUWFvakY3eFd1cUNKZmFKT0FMU1VTenVqVVk3T2Yya1ljN0dDVFE9PSIsIm1hYyI6ImU2NTBiMTdmMWI2NzA2ZDA1OTEzOTA3MTk1MDU3Njc5MTVmMDhmYWY1NmMyNDg0YTQ3NmZkMzk3ZjY5NzM5OWEifQ%3D%3D; bm_sv=587B303B3B6DFAFF86D41EC93D277961~1tghBENgOyOcDD0DHvgBGw/d+s1TMWZZSRnMZx530dycBJGLHm3bqurZWPZe14DTqPQVikqz1MAV5MS89Ea8BhpdTWIuMi8zYlJd4ZzWKBptb7zAPCB4Op7EF19/DqTGMUMeWI1tj/lxtf+09wkNdaD3ErVrXrMCPZSaNyAuuCw='
    }
    splash:set_custom_headers(headers)
    splash.private_mode_enabled = false
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(1))
    return splash:html()
  end