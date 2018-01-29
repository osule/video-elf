import json

from youtube_dl import YoutubeDL


youtube_dl = YoutubeDL()

def extract_media_info(context, event):
    context.logger.info('Extracting media information from Youtube url')

    body = json.loads(event.body)
    url = body['url']

    media_info = youtube_dl.extract_info(url, download=False)
    body = json.dumps(media_info)

    return context.Response(
        body=body,
        headers={},
        content_type='application/json',
        status_code=200
    )
