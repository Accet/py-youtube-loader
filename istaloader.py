import instaloader
import requests

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    L = instaloader.Instaloader()
    posts = instaloader.Profile.from_username(L.context, "zero_cake_").get_posts()

    shortCode = input("Enter the short code: ")

    for post in posts:
        if post.shortcode == shortCode:
            print(post.video_url)

            r = requests.get(post.video_url, allow_redirects=True)
            fileName = post.shortcode + '.mp4'
            if post.video_url.find('/'):
                fileNameUrl = post.video_url.rsplit('/', 1)[1]
                if fileNameUrl.find('?'):
                    print(fileNameUrl.split('?', 1)[0])
                    fileName = fileNameUrl.split('?', 1)[0]
                else:
                    fileName = fileNameUrl
            open(fileName, 'wb').write(r.content)
            print(post.shortcode)
            print(post.date)
            break
