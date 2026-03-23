FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 소스코드보다 의존성 파일을 먼저 복사하면,
# 의존성이 변경되지 않는 한 Docker가 이 레이어를 캐싱하여 빌드가 빨라집니다.
COPY pyproject.toml uv.lock ./

# --frozen    : uv.lock을 수정하지 않고 그대로 사용.
#               개발자가 로컬에서 검증한 정확한 버전 조합을 보장합니다.
#               만약 pyproject.toml과 uv.lock이 어긋나면 에러를 냅니다.
# --no-dev    : dev 의존성(pytest 등)을 설치하지 않음.
#               프로덕션 이미지에는 개발 도구가 필요 없으므로 이미지 크기를 줄입니다.
RUN uv sync --frozen --no-dev

COPY app/ ./app/

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
