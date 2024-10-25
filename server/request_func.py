import requests

def send_post_to_fastapi(sentence, url):
    """
    FastAPI로 POST 요청을 보내는 함수
    """

    # FastAPI로 보낼 데이터
    request_data = {
        'sentence': sentence,
    }

    try:
        # FastAPI로 POST 요청 전송
        response = requests.post(url, json=request_data)
        
        # FastAPI 서버의 응답 상태 확인
        if response.status_code == 200:
            return response.json()  # 성공 시 응답 데이터를 반환
        else:
            return {'error': 'FastAPI request failed', 'status_code': response.status_code}
    
    except requests.exceptions.RequestException as e:
        # 요청 실패 시 에러 반환
        return {'error': str(e)}