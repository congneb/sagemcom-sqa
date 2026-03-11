class LoginPage:
    def __init__(self, page, url):
        self.page = page
        self.url = url
        self.user_input = "input[name='username']"
        self.pass_input = "input[name='password']"
        self.login_btn = "button[type='submit']"

    def navigate(self):
        self.page.goto(self.url)

    def login(self, user, pwd):
        self.page.fill(self.user_input, user)
        self.page.fill(self.pass_input, pwd)
        self.page.click(self.login_btn)
        self.page.wait_for_load_state("networkidle")
