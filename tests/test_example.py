from pages.google_page import GooglePage



def test_search(page, playwright, browser, context):
    gp = GooglePage(page)
    gp.search_on_page('Булки с маком')
    gp.check_results('Булочки с маком')