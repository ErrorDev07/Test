import urllib

import mechanize

import os

import datetime

import sys

def login_to_facebook(email, password):

    browser = mechanize.Browser()

    browser.set_handle_robots(False)

    browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')]

    browser.set_handle_refresh(False)

    browser.open("https://m.facebook.com/login.php")

    browser.select_form(nr=0)

    browser.form['email'] = email

    browser.form['pass'] = password

    response = browser.submit()

    # Handle 2-step verification if required

    if response.geturl().startswith("https://m.facebook.com/checkpoint"):

        code = input("Enter the 2-step verification code: ")

        browser.select_form(nr=0)

        browser.form['approvals_code'] = code

        browser.submit()

    return browser

def post_comment(browser, post_link, comment):

    browser.open(post_link)

    browser.select_form(nr=0)

    browser.form['comment_text'] = comment

    browser.submit()

    print("Comment posted: ", comment)

def main():

    email = input("Enter your Facebook email: ")

    password = input("Enter your Facebook password: ")

    post_link = input("Enter the post link: ")

    notepad_link = input("Enter the notepad link containing comments: ")

    time_interval = int(input("Enter the time interval between comments (in seconds): "))

    browser = login_to_facebook(email, password)

    with urllib.request.urlopen(notepad_link) as response:

        comments = response.read().decode('utf-8').split('\n')

    for comment in comments:

        comment = comment.strip()

        if comment:

            post_comment(browser, post_link, comment)

            time.sleep(time_interval)

if __name__ == "__main__":

    main()

