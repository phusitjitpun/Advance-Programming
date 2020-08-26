from facebook_scraper import get_posts

for post in get_posts('ThailandLiverpoolFC', pages=500):
    Ntext = post['text'][:100]
    if ('ย้อนขมไฮไลต์' in Ntext):
        print(Ntext)
        print('Likes: ', post['likes'])
        print('post: ', post['post_url'])
        print('link: ', post['link'])
        print('------')