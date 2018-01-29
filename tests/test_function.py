import json
from mock import Mock

from video_elf import extract_media_info


def test_extract_media_info():
    event = Mock(
        body=json.dumps({
            'url': 'https://youtu.be/a8MnOv0uxkY'
        })
    )
    response = Mock()
    context = Mock(Response=response)
    media_info = extract_media_urls(context, event)

    args, kwargs = response.call_args

    assert response.called is True
    assert kwargs['content_type'] == 'application/json'
    assert kwargs['status_code'] == 200
    body = json.loads(kwargs['body'])
    assert 'id' in body
