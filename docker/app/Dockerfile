FROM python:3.10-slim AS builder

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv ${VIRTUAL_ENV}

COPY requirements.txt .
RUN ${VIRTUAL_ENV}/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim AS release

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR app

COPY docker/app/entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]