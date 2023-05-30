
def test_open_main_page(main_page):
    pass

def test_search_with_keyboard(main_page):
    main_page.click_search()
    main_page.input_to_search("test")
    main_page.press_enter_to_search()



def test_search_with_click(main_page):
    main_page.click_search()
    main_page.input_to_search("promt fo prom")
    main_page.click_button_to_search()

def test_search_and_back_to_main(main_page):
    main_page.click_search()
    main_page.input_to_search("promt fo prom")
    main_page.click_button_to_search()
    main_page.click_go_to_main()

def test_byers_support(main_page):
    main_page.bottom()
    main_page.click_byers_support_locator()

def test_about_us_locator(main_page):
    main_page.bottom()
    main_page.click_about_us_locator()

def test_info_for_sellers(main_page):
    main_page.bottom()
    main_page.click_info_for_sellers_locator()