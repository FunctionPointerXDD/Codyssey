from flask import Flask, render_template, request
from gtts import gTTS
import io
import base64
import datetime

app = Flask(__name__)

# 허용 언어 코드 목록
ALLOWED_LANGS = {'ko', 'en', 'ja', 'es'}

# 로그 파일 경로
LOG_FILE = 'input_log.txt'


def log_input(text: str, lang: str):
    """사용자 입력(text, lang)과 시간 기록을 로그 파일에 append."""
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f'[{now}] text="{text}" lang={lang}\n'
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(entry)


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    audio = None

    if request.method == 'POST':
        text = request.form.get('input_text', '').strip()
        lang = request.form.get('lang', '').strip()

        # 1) 입력 검사: 빈 텍스트
        if not text:
            error = '텍스트를 입력해주세요.'
        # 2) 언어 코드 검증
        elif lang not in ALLOWED_LANGS:
            error = f'유효하지 않은 언어 코드입니다: {lang}'
        else:
            # 로그 기록
            try:
                log_input(text, lang)
            except Exception:
                app.logger.exception("로그 파일 기록 중 오류")

            # TTS 변환
            try:
                tts = gTTS(text=text, lang=lang)
                buf = io.BytesIO()
                tts.write_to_fp(buf)
                buf.seek(0)
                audio = base64.b64encode(buf.read()).decode('utf-8')
            except Exception:
                app.logger.exception("gTTS 변환 중 오류")
                error = '음성 변환 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.'

    return render_template('index.html', error=error, audio=audio)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

